"""Context 0/1/2 review sheet for test (BENCHMARK §2: >= 5 answerable test questions, baseline and chosen config).

AI draft rule (checked by reading the contexts on 2026-11-16): 2 = every evidence quote of one gold is in the
final retrieval context AND each block header gives id, year, page and article; 1 = right source/article present
but a required quote (condition/exception) missing, or header lacks the source; 0 = no evidence.
human_* columns are left for the student. Output: results/review/context_review_test.csv
Run: .venv/Scripts/python -X utf8 scripts/context_review_sheet.py test dense_k3 rerank_hybrid
"""
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.data_io import load_benchmark  # noqa: E402
from src.metrics import squash  # noqa: E402


def main():
    split, cfgs = sys.argv[1], sys.argv[2:]
    qs = {q["id"]: q for q in load_benchmark(split=split) if q["answerable"]}
    rows = []
    for cfg in cfgs:
        for line in (ROOT / "results" / "retrieval" / f"{cfg}_{split}" / "traces.jsonl").read_text(encoding="utf-8").splitlines():
            t = json.loads(line)
            if t["query_id"] not in qs:
                continue
            q, ctx = qs[t["query_id"]], squash(t["context"])
            found = [[squash(e) in ctx for e in g["evidence"]] for g in q["gold"]]
            same_place = any(g["source_id"] in t["context"] and f"Điều {g['article']}" in t["context"] for g in q["gold"])
            if t["context_hit"]:
                score, why = 2, "Đủ mọi quote của một gold trong context; header ghi id, năm, trang, Điều."
            elif same_place and any(any(f) for f in found):
                score, why = 1, f"Có đúng nguồn/Điều nhưng thiếu quote: {found}"
            else:
                score, why = 0, "Không có evidence của gold trong context."
            rows.append({"config": cfg, "query_id": t["query_id"], "question": q["question"],
                         "gold_evidence": " || ".join(" + ".join(g["evidence"]) for g in q["gold"]),
                         "context_ids": ";".join(t["context_ids"]), "ai_score": score, "ai_reason": why,
                         "human_score": "", "human_reason": ""})
    out = ROOT / "results" / "review" / f"context_review_{split}.csv"
    with open(out, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    for cfg in cfgs:
        sc = [r["ai_score"] for r in rows if r["config"] == cfg]
        print(cfg, {s: sc.count(s) for s in (0, 1, 2)}, f"n={len(sc)}")


if __name__ == "__main__":
    main()
