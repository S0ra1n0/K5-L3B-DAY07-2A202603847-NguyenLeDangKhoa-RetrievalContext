"""Compare retrieval runs on one split: summary table + per-question first-hit rank (for error analysis).

Run: .venv/Scripts/python -X utf8 scripts/compare_retrieval.py dev dense_k3 bm25_syllable ...
Writes results/retrieval/comparison_<split>.md
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(cfg, split):
    d = ROOT / "results" / "retrieval" / f"{cfg}_{split}"
    summary = json.loads((d / "summary.json").read_text(encoding="utf-8"))
    traces = {t["query_id"]: t for t in map(json.loads, (d / "traces.jsonl").read_text(encoding="utf-8").splitlines())}
    return summary, traces


def main():
    split, cfgs = sys.argv[1], sys.argv[2:]
    runs = {c: load(c, split) for c in cfgs}
    f = lambda m: f"{m['n']}/{m['N']} ({m['rate']:.0%})"
    lines = [f"# Retrieval comparison · {split}", "",
             f"Benchmark commit `{runs[cfgs[0]][0]['benchmark_commit']}`. Same corpus (chunk set B, 552 chunks), index, "
             "questions, gold and hit definition for every row. Query = original question; filter = user-provided `filter`.", "",
             "| Config | Hit@1 | Evidence Hit@3 | Context Evidence Rate | MRR@10 | Avg context (chars) | Median latency (ms) | Setup (s) | Cost |",
             "|---|---|---|---|---|---|---|---|---|"]
    for c in cfgs:
        s = runs[c][0]
        lines.append(f"| {c} | {f(s['hit@1'])} | {f(s['evidence_hit@3'])} | {f(s['context_evidence_rate'])} | {s['mrr@10']} | "
                     f"{s['avg_context_chars']} | {s['median_latency_ms']} | {s['setup_seconds']} | 0 USD |")
    ids = [i for i, t in runs[cfgs[0]][1].items() if t.get("answerable")]
    lines += ["", "## First hit rank per question (only questions where some config is not rank 1)", "",
              "| Query | " + " | ".join(cfgs) + " | dense top-1 (year/article) | question |", "|---" * (len(cfgs) + 3) + "|"]
    for i in ids:
        ranks = [runs[c][1][i].get("first_hit_rank") for c in cfgs]
        if any(r != 1 for r in ranks):
            t = runs[cfgs[0]][1][i]
            top = t["results"][0]
            lines.append(f"| {i} | " + " | ".join(str(r) for r in ranks) +
                         f" | {top['year']}/Đ{top['article']} ({top['part']}) | {t['question'][:80]} |")
    out = ROOT / "results" / "retrieval" / f"comparison_{split}.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
