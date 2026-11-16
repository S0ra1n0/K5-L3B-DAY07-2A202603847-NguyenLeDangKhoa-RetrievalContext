"""Run the real agent (local Ollama + Day 6 retrieval) on a split, or on one ad-hoc question.

Benchmark mode: .venv/Scripts/python -X utf8 scripts/run_agent_bench.py --split dev configs/agent_dense_k3.json [...]
Ad-hoc mode   : .venv/Scripts/python -X utf8 scripts/run_agent_bench.py --question "..." configs/agent_dense_k3.json
                (no benchmark access; used for smoke tests before the benchmark is frozen)

Benchmark outputs per config: results/agent/<name>_<split>/
  traces.json   one record per question (query_id, status, events, citations, answer, final context, usage)
                -> the format starter/agent_metrics.py expects (retrieval turns are `search` events)
  cases.json    id, split, answerable
  summary.json  status counts, searches per question, Context Evidence Rate of the final context,
                latency and tokens. Answer quality is NOT judged here: humans label it (roadmap H4).
The agent only receives data_io.public_view(question); gold is used after the run, for metrics only.
"""
import argparse
import collections
import json
import statistics
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src import config  # noqa: E402
from src.agent import run_agent  # noqa: E402
from src.context import ContextBuilder  # noqa: E402
from src.data_io import load_benchmark, public_view  # noqa: E402
from src.guards import benchmark_frozen, check_split_allowed  # noqa: E402
from src.llm import OllamaChat  # noqa: E402
from src.metrics import context_has_evidence, ratio  # noqa: E402
from src.retrievers import build_retriever  # noqa: E402


def setup(cfg, cache):
    retriever = build_retriever(cfg["retriever"], cache=cache)
    builder = ContextBuilder(cache["chunks"], budget=cfg["context"]["budget_chars"],
                             expand_parts=cfg["context"].get("expand_parts", False))
    return retriever, builder, OllamaChat(model=cfg.get("llm_model"))


def run_one(view, cfg, retriever, builder, llm):
    return run_agent(view, llm, retriever, builder, max_searches=cfg["max_searches"],
                     top_k=cfg["search_top_k"], filter_policy=cfg["filter_policy"])


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--split", choices=("dev", "test"))
    g.add_argument("--question")
    ap.add_argument("--year", type=int, help="ad-hoc mode: user-provided year filter")
    ap.add_argument("configs", nargs="+", type=Path)
    args = ap.parse_args()
    cache = {}
    if args.question:
        cfg = json.loads(args.configs[0].read_text(encoding="utf-8"))
        retriever, builder, llm = setup(cfg, cache)
        view = {"id": "adhoc", "question": args.question, **({"filter": {"year": args.year}} if args.year else {})}
        print(json.dumps(run_one(view, cfg, retriever, builder, llm), ensure_ascii=False, indent=2))
        return
    commit = benchmark_frozen()
    questions = load_benchmark(split=args.split)
    for path in args.configs:
        cfg = json.loads(path.read_text(encoding="utf-8"))
        out_dir = config.RESULTS_DIR / "agent" / f"{cfg['name']}_{args.split}"
        check_split_allowed(args.split, out_dir)
        retriever, builder, llm = setup(cfg, cache)
        traces, t0 = [], time.perf_counter()
        for q in questions:
            result = run_one(public_view(q), cfg, retriever, builder, llm)
            rec = {"query_id": q["id"], "split": args.split, "type": q["type"], "answerable": q["answerable"],
                   "question": q["question"], "config": cfg["name"], "model": llm.describe(), **result}
            if q["answerable"] and result["status"] != "error":
                ctx_chunks = [cache_by_id(cache)[i] for i in result["final_context_ids"]]
                rec["final_context_has_evidence"] = context_has_evidence(ctx_chunks, q["gold"])
            traces.append(rec)
            print(f"{cfg['name']} {q['id']:<4} {result['status']:<8} searches={result['searches']} "
                  f"{result['seconds']:>5}s cites={result['citations']}", flush=True)
        ok = [t for t in traces if t["status"] != "error"]
        ans = [t for t in ok if t["answerable"]]
        summary = {"config": cfg["name"], "split": args.split, "benchmark_commit": commit, "model": llm.describe(),
                   "agent": {k: cfg[k] for k in ("max_searches", "search_top_k", "filter_policy")},
                   "retriever": cfg["retriever"], "context": cfg["context"], "questions": len(traces),
                   "status": dict(collections.Counter(t["status"] for t in traces)),
                   "errors": [{"query_id": t["query_id"], "error": t["error"]} for t in traces if t["status"] == "error"],
                   "tool_use": ratio(sum(t["searches"] > 0 for t in ok), len(ok)),
                   "searches_distribution": dict(sorted(collections.Counter(t["searches"] for t in ok).items())),
                   "context_evidence_rate_final": ratio(sum(t.get("final_context_has_evidence", False) for t in ans), len(ans)),
                   "answered_with_citation": ratio(sum(t["status"] == "answered" for t in ok), len(ok)),
                   "abstained_answerable": ratio(sum(t["status"] == "abstain" for t in ans), len(ans)),
                   "abstained_unanswerable": ratio(sum(t["status"] == "abstain" for t in ok if not t["answerable"]),
                                                   sum(not t["answerable"] for t in ok)),
                   "filter_sources": dict(collections.Counter(e["filter_source"] for t in ok for e in t["events"] if e["event"] == "search")),
                   "median_seconds": round(statistics.median(t["seconds"] for t in traces), 2),
                   "total_seconds": round(time.perf_counter() - t0, 1),
                   "tokens": {"prompt": sum(t["usage"]["prompt_tokens"] for t in traces),
                              "output": sum(t["usage"]["output_tokens"] for t in traces)},
                   "service_cost_usd": 0.0,
                   "note": "Answer quality, citation support and abstention correctness come from human labels (roadmap H4)."}
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "traces.json").write_text(json.dumps(traces, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (out_dir / "cases.json").write_text(json.dumps([{"id": q["id"], "split": q["split"], "answerable": q["answerable"]}
                                                        for q in questions], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (out_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps({k: summary[k] for k in ("config", "status", "tool_use", "context_evidence_rate_final",
                                                  "abstained_answerable", "abstained_unanswerable", "median_seconds")},
                         ensure_ascii=False))


def cache_by_id(cache):
    if "by_id" not in cache:
        cache["by_id"] = {c["id"]: c for c in cache["chunks"]}
    return cache["by_id"]


if __name__ == "__main__":
    main()
