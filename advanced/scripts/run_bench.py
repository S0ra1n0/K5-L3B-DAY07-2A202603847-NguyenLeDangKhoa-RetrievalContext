"""Run one advanced config on one split and save a full trace per question.

Usage: .venv/Scripts/python -X utf8 advanced/scripts/run_bench.py --config advanced/configs/a1_hybrid.json --split dev
Guards (same spirit as the base lab):
- advanced/benchmark/questions.json must be tracked by git with no uncommitted change (frozen before any run);
- --split test needs advanced/results/selection.json (config chosen on dev) and refuses to run a config twice.
The agent only receives the question text. Gold evidence is used afterwards, only for the retrieval check
`evidence_in_context` (every gold evidence region/page is in the final context) -- never inside the run.
Errors are recorded per question (status "error"), never replaced by a fake answer; they count as failures.
"""
import argparse
import datetime as dt
import json
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
BENCH = ROOT / "advanced" / "benchmark" / "questions.json"
RESULTS = ROOT / "advanced" / "results"
RUNS = RESULTS / "runs"


def git(*args) -> str:
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, check=True).stdout


def guard(split: str, config_name: str):
    rel = BENCH.relative_to(ROOT).as_posix()
    if not git("ls-files", rel).strip():
        raise SystemExit(f"{rel} is not committed: review and commit (freeze) the benchmark before any run")
    if git("status", "--porcelain", "--", rel).strip():
        raise SystemExit(f"{rel} has uncommitted changes: the benchmark must stay frozen")
    if split == "test":
        if not (RESULTS / "selection.json").exists():
            raise SystemExit("test is locked until advanced/results/selection.json exists (choose the config on dev)")
        if (RUNS / f"{config_name}_test.jsonl").exists():
            raise SystemExit(f"{config_name} already ran on test once; not running again")


def evidence_check(q: dict, out: dict, chunks_by_id: dict) -> dict:
    """Retrieval-side check only: is every gold evidence (region if given, else page) in the final context?"""
    if not q["answerable"]:
        return {}
    ctx = [chunks_by_id.get(i, {"page": int(i[1:4]), "metadata": {}}) for i in out.get("final_context_ids", [])]
    ctx_regions = {c["metadata"].get("region") for c in ctx}
    ctx_pages = {c["page"] for c in ctx}
    found = []
    for ev in q["evidence"]:
        found.append(ev.get("region") in ctx_regions if ev.get("region") else ev["pdf_page"] in ctx_pages)
    return {"evidence_in_context": all(found), "evidence_found": found}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True, type=Path)
    ap.add_argument("--split", required=True, choices=["dev", "test"])
    ap.add_argument("--only", help="comma-separated question ids (debugging a dev question)")
    args = ap.parse_args()
    cfg = json.loads(args.config.read_text(encoding="utf-8"))
    name = cfg["name"]
    guard(args.split, name)
    from advanced.rag.agent import Context, run_agent
    from advanced.rag.retrieval import build_retriever, load_chunks
    from src.llm import OllamaChat
    qs = [q for q in json.loads(BENCH.read_text(encoding="utf-8"))["questions"] if q["split"] == args.split]
    if args.only:
        qs = [q for q in qs if q["id"] in args.only.split(",")]
    chunks_by_id = {c["id"]: c for c in load_chunks()}
    retriever = build_retriever(cfg["retriever"])
    llm = OllamaChat(options=cfg.get("llm_options"))
    builder = Context(budget=cfg.get("budget", 7000))
    RUNS.mkdir(parents=True, exist_ok=True)
    out_path = RUNS / f"{name}_{args.split}{'_partial' if args.only else ''}.jsonl"
    meta = {"config": cfg, "split": args.split, "started": dt.datetime.now().isoformat(timespec="seconds"),
            "benchmark_commit": git("log", "-1", "--format=%H", "--", BENCH.relative_to(ROOT).as_posix()).strip(),
            "llm": llm.describe(), "retriever": retriever.name}
    rows = []
    for n, q in enumerate(qs, 1):
        t = time.perf_counter()
        out = run_agent(q["question"], llm, retriever, builder, max_searches=cfg.get("max_searches", 3),
                        top_k=cfg.get("top_k", 5), view_page=cfg.get("view_page", False),
                        max_views=cfg.get("max_views", 2), citation_retry=cfg.get("citation_retry", False))
        row = {"id": q["id"], "split": q["split"], "group": q["group"], "answerable": q["answerable"],
               "question": q["question"], **out, **evidence_check(q, out, chunks_by_id)}
        rows.append(row)
        print(f"[{n}/{len(qs)}] {q['id']} {q['group']:<12} {row['status']:<8} ev_in_ctx={row.get('evidence_in_context', '-')} "
              f"{time.perf_counter() - t:5.1f}s {('ERROR ' + row['error']) if row.get('error') else ''}", flush=True)
        out_path.write_text(json.dumps({"meta": meta}, ensure_ascii=False) + "\n"
                            + "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
    ans = [r for r in rows if r["answerable"]]
    summary = {"n": len(rows), "errors": sum(r["status"] == "error" for r in rows),
               "answered": sum(r["status"] == "answered" for r in rows),
               "evidence_in_context": f"{sum(bool(r.get('evidence_in_context')) for r in ans)}/{len(ans)}",
               "unanswerable_abstained": f"{sum(r['status'] == 'abstain' for r in rows if not r['answerable'])}/"
                                         f"{sum(not r['answerable'] for r in rows)}",
               "seconds_total": round(sum(r["seconds"] for r in rows), 1)}
    print(json.dumps(summary, ensure_ascii=False))
    print(f"-> {out_path.relative_to(ROOT)} (answers still need pass/fail labels against the PDF)")


if __name__ == "__main__":
    main()
