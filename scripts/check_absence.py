"""List every passage of the corpus that contains a keyword of an unanswerable question.

A human reads each hit and confirms none answers the question (roadmap H2). Absence is
judged on the WHOLE corpus (151 pages), never on what top-k retrieval returned.
Usage: python -X utf8 scripts/check_absence.py [--id u01] [--width 110]
Writes results/setup/absence_check.json.
"""
import argparse
import json
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.data_io import load_benchmark, load_pages  # noqa: E402


def norm(s):
    return " ".join(unicodedata.normalize("NFC", s).split()).casefold()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--id")
    ap.add_argument("--width", type=int, default=110)
    args = ap.parse_args()
    pages = load_pages()
    questions = [q for q in load_benchmark() if not q["answerable"] and (not args.id or q["id"] == args.id)]
    report = []
    for q in questions:
        print(f"\n######## {q['id']} [{q['split']}] {q['question']}\n   reason: {q['absence_reason']}")
        entry = {"id": q["id"], "keywords": {}}
        for kw in q["absence_check"]["keywords"]:
            hits = []
            for p in pages:
                text = " ".join(p["text"].split())
                low = norm(text)
                start = low.find(norm(kw))
                while start != -1:
                    a, b = max(0, start - args.width), start + len(kw) + args.width
                    hits.append({"doc": p["document_id"], "page": p["page"], "snippet": text[a:b]})
                    start = low.find(norm(kw), start + 1)
            entry["keywords"][kw] = hits
            print(f"  -- '{kw}': {len(hits)} hit(s)")
            for h in hits[:12]:
                print(f"     {h['doc']}#p{h['page']}: …{h['snippet']}…")
            if len(hits) > 12:
                print(f"     (+{len(hits) - 12} more in results/setup/absence_check.json)")
        report.append(entry)
    out = ROOT / "results" / "setup" / "absence_check.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    if args.id and out.exists():  # merge: a single-question run must not drop the other questions' evidence
        kept = [e for e in json.loads(out.read_text(encoding="utf-8")) if e["id"] != args.id]
        order = [q["id"] for q in load_benchmark() if not q["answerable"]]
        report = sorted(kept + report, key=lambda e: order.index(e["id"]) if e["id"] in order else 99)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
