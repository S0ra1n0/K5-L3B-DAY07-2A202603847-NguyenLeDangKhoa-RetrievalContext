"""Retrieval + context benchmark for one or more configs on one split (no LLM involved).

Per answerable question: top-10 ranking (Hit@1, Evidence Hit@3, MRR@10 use the SAME hit definition
and cutoffs for every method), then the context the agent would get from the first
`context.top_k` results (Context Evidence Rate). Unanswerable questions are run and traced but
excluded from these denominators. The query is the ORIGINAL question; the filter is the
benchmark `filter` (user-provided) when the config says filter_source = "user".

Run: .venv/Scripts/python -X utf8 scripts/eval_retrieval.py --split dev configs/dense_k3.json configs/bm25_syllable.json ...
Outputs: results/retrieval/<config>_<split>/{traces.jsonl, summary.json}
"""
import argparse
import json
import statistics
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src import config  # noqa: E402
from src.context import ContextBuilder  # noqa: E402
from src.data_io import load_benchmark, public_view  # noqa: E402
from src.guards import benchmark_frozen, check_split_allowed  # noqa: E402
from src.metrics import chunk_hit, context_has_evidence, first_hit_rank, summarize_retrieval  # noqa: E402
from src.retrievers import build_retriever  # noqa: E402

RANK_DEPTH = 10


def slim(r, golds):
    keep = {k: r[k] for k in ("rank", "id", "source_id", "page", "pages", "score", "strategy")}
    keep["year"], keep["article"] = r["metadata"].get("year"), r["metadata"].get("article")
    keep["part"] = f"{r['metadata'].get('part')}/{r['metadata'].get('parts')}"
    for extra in ("components", "before_rerank"):
        if extra in r:
            keep[extra] = r[extra]
    if golds is not None:
        keep["hit"] = chunk_hit(r, golds)
    return keep


def run_config(cfg, split, questions, cache, commit):
    out_dir = config.RESULTS_DIR / "retrieval" / f"{cfg['name']}_{split}"
    check_split_allowed(split, out_dir)
    t0 = time.perf_counter()
    retriever = build_retriever(cfg["retriever"], cache=cache)
    setup_s = time.perf_counter() - t0
    ctx_cfg = cfg["context"]
    builder = ContextBuilder(cache["chunks"], budget=ctx_cfg["budget_chars"], expand_parts=ctx_cfg.get("expand_parts", False))
    traces, rows, latencies, errors = [], [], [], []
    for q in questions:
        view = public_view(q)                       # the retriever never sees gold
        filters = view.get("filter") if cfg.get("filter_source") == "user" else None
        t = time.perf_counter()
        try:
            results = retriever.search(view["question"], filters=filters, top_k=max(RANK_DEPTH, ctx_cfg["top_k"]))
        except Exception as exc:                    # reported, never replaced by fake results
            errors.append({"query_id": q["id"], "error": repr(exc)})
            traces.append({"query_id": q["id"], "status": "error", "error": repr(exc)})
            continue
        ctx = builder.build(results[:ctx_cfg["top_k"]])
        ms = (time.perf_counter() - t) * 1000
        latencies.append(ms)
        golds = q["gold"] if q["answerable"] else None
        trace = {"query_id": q["id"], "split": split, "type": q["type"], "answerable": q["answerable"],
                 "question": view["question"], "query": view["question"], "filter": filters,
                 "results": [slim(r, golds) for r in results[:RANK_DEPTH]],
                 "context_ids": ctx["context_ids"], "context_chars": ctx["chars"],
                 "skipped_for_budget": ctx["skipped_for_budget"], "added_by_expansion": ctx["added_by_expansion"],
                 "context": ctx["context"], "latency_ms": round(ms, 1), "status": "ok"}
        if golds is not None:
            rank = first_hit_rank(results[:RANK_DEPTH], golds)
            trace.update(hit1=rank == 1, hit3=rank is not None and rank <= 3, first_hit_rank=rank,
                         context_hit=context_has_evidence(ctx["chunks"], golds))
            rows.append({"hit1": trace["hit1"], "hit3": trace["hit3"], "context_hit": trace["context_hit"],
                         "rr": 1 / rank if rank else 0.0})
        traces.append(trace)
    answerable = [q for q in questions if q["answerable"]]
    summary = {"config": cfg["name"], "description": cfg.get("description"), "split": split,
               "benchmark_commit": commit, "retriever": cfg["retriever"], "context": ctx_cfg,
               "filter_source": cfg.get("filter_source"), "questions": len(questions),
               "answerable_N": len(answerable), "errors": errors,
               **summarize_retrieval(rows),
               "avg_context_chars": round(statistics.mean(t["context_chars"] for t in traces if t["status"] == "ok"), 1),
               "median_latency_ms": round(statistics.median(latencies), 1) if latencies else None,
               "setup_seconds": round(setup_s, 2), "service_cost_usd": 0.0,
               "missed_ids": [t["query_id"] for t in traces if t.get("answerable") and not t.get("hit3")],
               "context_missed_ids": [t["query_id"] for t in traces if t.get("answerable") and not t.get("context_hit")]}
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "traces.jsonl", "w", encoding="utf-8") as f:
        for t in traces:
            f.write(json.dumps(t, ensure_ascii=False) + "\n")
    (out_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return summary


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--split", required=True, choices=("dev", "test"))
    ap.add_argument("configs", nargs="+", type=Path)
    args = ap.parse_args()
    commit = benchmark_frozen()
    questions = load_benchmark(split=args.split)    # only the requested split is loaded
    cache = {}
    for path in args.configs:
        cfg = json.loads(path.read_text(encoding="utf-8"))
        s = run_config(cfg, args.split, questions, cache, commit)
        fmt = lambda m: f"{s[m]['n']}/{s[m]['N']}"
        print(f"{s['config']:<24} Hit@1 {fmt('hit@1'):>6}  Hit@3 {fmt('evidence_hit@3'):>6}  "
              f"CtxEvid {fmt('context_evidence_rate'):>6}  MRR {s['mrr@10']}  ctx {s['avg_context_chars']} ch  "
              f"{s['median_latency_ms']} ms  errors {len(s['errors'])}")


if __name__ == "__main__":
    main()
