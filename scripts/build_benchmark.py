"""Build benchmark/questions.json = 20 Day 6 questions (q16-q20 moved to dev) + Day 7 new questions.

Why q16-q20 move to dev: their Day 6 test results were already seen, and a Day 6 fix idea
(Điều 219 quoting the Social Insurance Law) came from them, so they are no longer an
independent test (RUBRIC/RULES). The Day 7 test set is new: t01-t11.
Run: python -X utf8 scripts/build_benchmark.py
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.data_io import convert_day6_question  # noqa: E402

DAY6 = ROOT / "data" / "day6" / "day6_questions.json"
NEW = ROOT / "benchmark" / "day7_new_questions.json"
OUT = ROOT / "benchmark" / "questions.json"


def main():
    day6 = json.loads(DAY6.read_text(encoding="utf-8"))["questions"]
    new = json.loads(NEW.read_text(encoding="utf-8"))["questions"]
    questions = [convert_day6_question(q, split="dev") for q in day6] + new
    ids = [q["id"] for q in questions]
    if len(ids) != len(set(ids)):
        raise SystemExit("duplicate question id")
    out = {"version": "2026-11-16",
           "corpus": "data/day6/chunks_B.jsonl + pages.jsonl (BLLĐ 2012 + 2019, OCR đã làm sạch, Day 6)",
           "split_policy": "q01-q20 (Day 6) + u01-u03 = dev; t01-t11 (new, Day 7) = test. "
                           "q16-q20 were Day 6 test and moved to dev because their results were already seen.",
           "questions": questions}
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for split in ("dev", "test"):
        rows = [q for q in questions if q["split"] == split]
        print(split, "answerable", sum(q["answerable"] for q in rows),
              "unanswerable", sum(not q["answerable"] for q in rows))


if __name__ == "__main__":
    main()
