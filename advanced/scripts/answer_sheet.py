"""Build the per-question grading sheet for a run (pass/fail is decided by reading, not by these hints).

Usage: .venv/Scripts/python -X utf8 advanced/scripts/answer_sheet.py advanced/results/runs/a1_hybrid_dev.jsonl
Output: advanced/results/review/<run>.csv with, per question: status, answer, cited ids and their PDF pages,
expected answer / behaviour, gold evidence pages, and two automatic hints:
  key_numbers  numbers of the expected answer found / total in the answer (formatting-insensitive)
  cites_gold   every gold evidence page is among the cited pages
Label columns (empty): ai_label (pass/fail), ai_reason, human_label, human_note.
Pass rules (ADVANCED.md): answerable -> right and complete, right unit/condition/calculation, citations identify
the page and region and support the whole answer; partial, wrong citation or abstention = fail.
Unanswerable -> abstains or clearly says there is not enough evidence, no unsupported claim. Errors = fail.
"""
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BENCH = ROOT / "advanced" / "benchmark" / "questions.json"


def nums(s: str) -> set[str]:
    out = set()
    for m in re.finditer(r"[–−-]?\d[\d,]*(?:\.\d+)?", s or ""):
        v = m.group(0).replace(",", "").replace("–", "-").replace("−", "-").lstrip("-")
        if re.fullmatch(r"(19|20)\d\d", v) or len(v.replace(".", "")) < 2:
            continue
        out.add(v.rstrip("0").rstrip(".") if "." in v else v)
    return out


def main():
    run = Path(sys.argv[1])
    lines = run.read_text(encoding="utf-8").splitlines()
    rows = [json.loads(l) for l in lines[1:]]
    gold = {q["id"]: q for q in json.loads(BENCH.read_text(encoding="utf-8"))["questions"]}
    out_dir = ROOT / "advanced" / "results" / "review"
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / (run.stem + ".csv")
    with open(out, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["id", "group", "status", "question", "answer", "cited", "cited_pdf_pages", "expected",
                    "gold_pdf_pages", "key_numbers", "cites_gold", "evidence_in_context", "seconds",
                    "ai_label", "ai_reason", "human_label", "human_note"])
        for r in rows:
            q = gold[r["id"]]
            cited_pages = sorted({int(c[1:4]) for c in r.get("citations", [])})
            if q["answerable"]:
                exp = q["expected_answer"]
                gp = sorted({e["pdf_page"] for e in q["evidence"]})
                en = nums(exp)
                hit = len(en & nums(r.get("answer") or ""))
                key = f"{hit}/{len(en)}"
                cg = all(p in cited_pages for p in gp)
            else:
                exp, gp, key, cg = "ABSTAIN (" + q["absence_check"]["result"][:120] + ")", [], "", ""
            w.writerow([r["id"], r["group"], r["status"], r["question"], r.get("answer") or r.get("error"),
                        " ".join(r.get("citations", [])), " ".join(map(str, cited_pages)), exp, " ".join(map(str, gp)),
                        key, cg, r.get("evidence_in_context", ""), r["seconds"], "", "", "", ""])
    print(f"{len(rows)} rows -> {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
