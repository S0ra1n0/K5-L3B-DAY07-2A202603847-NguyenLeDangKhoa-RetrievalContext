"""Compare dev runs: pass/fail labels (by group), evidence in context, time and tokens -> advanced/results/dev_comparison.md
Usage: .venv/Scripts/python -X utf8 advanced/scripts/compare_dev.py
Labels come from advanced/results/review/dev_labels_v*.json (written by reading each answer); runs from results/runs.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RES = ROOT / "advanced" / "results"
GROUPS = ["table", "figure", "chart", "multihop", "text", "unanswerable"]


def main():
    labels = {}
    for f in sorted((RES / "review").glob("dev_labels_v*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        for qid, lab in d["labels"].items():
            for cfg, v in lab.items():
                if cfg != "reason":
                    labels.setdefault(cfg, {})[qid] = v
    runs = {"a0_dense": "a0_dense_dev_v1", "a1_hybrid": "a1_hybrid_dev_v1", "a2_rerank": "a2_rerank_dev_v1",
            "a3_hybrid_view": "a3_hybrid_view_dev_v1", "b0_dense": "b0_dense_dev", "b1_hybrid": "b1_hybrid_dev",
            "b2_rerank": "b2_rerank_dev", "c0_dense": "c0_dense_dev", "c2_rerank": "c2_rerank_dev"}
    head = ("| config | index/agent | pass | " + " | ".join(GROUPS) +
            " | evidence in context | errors | avg s/question | avg LLM calls | avg prompt tok | avg output tok |")
    lines = ["# Dev comparison (18 questions: 15 answerable + 3 unanswerable)", "",
             "Labels: AI reading against the gold evidence and the PDF (`review/dev_labels_v1.json`, `v2.json`, `v3.json`); human check pending.",
             "v1 = first index/agent; v2 = after dev v1 error analysis (table_row chunks, creditor rule, citation repair); v3 = v2 + profile cards mark segments named in the legend, guide page read by columns (after dev v2).", "",
             head, "|" + "---|" * (head.count("|") - 1)]
    for cfg, stem in runs.items():
        rows = [json.loads(l) for l in (RES / "runs" / f"{stem}.jsonl").read_text(encoding="utf-8").splitlines()[1:]]
        lab = labels[cfg]
        by = []
        for g in GROUPS:
            ids = [r["id"] for r in rows if r["group"] == g]
            by.append(f"{sum(lab[i] == 'pass' for i in ids)}/{len(ids)}")
        ans = [r for r in rows if r["answerable"]]
        n = len(rows)
        u = [r["usage"] for r in rows]
        lines.append(f"| {cfg} | { {"a": "v1", "b": "v2", "c": "v3"}[cfg[0]] } | **{sum(v == 'pass' for v in lab.values())}/{n}** | "
                     + " | ".join(by)
                     + f" | {sum(bool(r.get('evidence_in_context')) for r in ans)}/{len(ans)} | {sum(r['status'] == 'error' for r in rows)}"
                     f" | {sum(r['seconds'] for r in rows) / n:.1f} | {sum(x['llm_calls'] for x in u) / n:.2f}"
                     f" | {sum(x['prompt_tokens'] for x in u) / n:.0f} | {sum(x['output_tokens'] for x in u) / n:.0f} |")
    lines += ["", "Cost: all models run locally (Ollama `qwen3.5:9b`, e5-base, bge-reranker-v2-m3 on CPU): US$0 API cost; "
              "time measured on an RTX 3070 Laptop GPU that was thermally throttled during the runs."]
    out = RES / "dev_comparison.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
