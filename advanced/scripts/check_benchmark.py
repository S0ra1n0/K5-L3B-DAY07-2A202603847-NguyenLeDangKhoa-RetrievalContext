"""Check advanced/benchmark/questions.json against ADVANCED.md quotas and against the extracted document.

- quotas: dev >= 15 answerable + 3 unanswerable covering all groups; test >= 24 + 6 with
  table >= 6, figure >= 5, chart >= 5, multihop >= 4, text >= 4 (one primary group per question)
- every evidence: pdf_page exists, region (if any) is on that page, and each part of quote_or_value
  (split on ' ; ') is found in the region/page text layer: 'exact' (verbatim after whitespace/dash
  normalisation) or 'tokens' (all its numbers/words present, e.g. block-diagram labels and values
  printed apart). Parts marked '~' or '(visual' are visual readings -> must be checked on the image by a human.
- unanswerable: re-runs the absence_check patterns over all pages and prints the hit pages
- dev/test overlap: same evidence value on the same page in both splits
- fills evidence bbox from regions.json (writes the file back only with --write)
Usage: .venv/Scripts/python -X utf8 advanced/scripts/check_benchmark.py [--write]
"""
import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BENCH = ROOT / "advanced" / "benchmark" / "questions.json"
PROC = ROOT / "advanced" / "data" / "processed"
TEST_MIN = {"table": 6, "figure": 5, "chart": 5, "multihop": 4, "text": 4}
GROUPS = set(TEST_MIN) | {"unanswerable"}


def norm(s: str) -> str:
    s = s.replace("–", "-").replace("−", "-").replace("’", "'").replace("“", '"').replace("”", '"')
    s = re.sub(r"-\s*\n\s*", "-", s)          # hyphenated line breaks
    return re.sub(r"\s+", " ", s).strip().lower()


def find(part: str, text: str) -> str:
    if norm(part) in norm(text):
        return "exact"
    toks = re.findall(r"[\w.,%$-]+", norm(part))
    hay = norm(text)
    if toks and all(t.strip(".,") in hay for t in toks):
        return "tokens"
    return "missing"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true", help="write evidence bbox back into questions.json")
    args = ap.parse_args()
    data = json.loads(BENCH.read_text(encoding="utf-8"))
    qs = data["questions"]
    pages = {json.loads(l)["pdf_page"]: json.loads(l) for l in (PROC / "pages.jsonl").read_text(encoding="utf-8").splitlines()}
    regions = {r["id"]: r for r in json.loads((PROC / "regions.json").read_text(encoding="utf-8"))}
    problems, visual, token_only = [], [], []

    ids = Counter(q["id"] for q in qs)
    problems += [f"duplicate id {i}" for i, n in ids.items() if n > 1]
    for q in qs:
        need = ["id", "split", "group", "question", "answerable", "reason"]
        need += ["expected_answer", "evidence"] if q.get("answerable") else ["expected_behavior", "absence_check"]
        problems += [f"{q.get('id')}: missing field {f}" for f in need if f not in q]
        if q.get("group") not in GROUPS:
            problems.append(f"{q['id']}: unknown group {q.get('group')}")
        if q.get("answerable") is False and q.get("group") != "unanswerable":
            problems.append(f"{q['id']}: unanswerable question must use group 'unanswerable'")

    # quotas
    for split in ("dev", "test"):
        sq = [q for q in qs if q["split"] == split]
        ans = [q for q in sq if q["answerable"]]
        una = [q for q in sq if not q["answerable"]]
        by = Counter(q["group"] for q in ans)
        print(f"{split}: {len(ans)} answerable + {len(una)} unanswerable = {len(sq)}; by group {dict(by)}")
        if split == "test":
            if len(ans) < 24 or len(una) < 6:
                problems.append(f"test needs >= 24 answerable and >= 6 unanswerable")
            problems += [f"test group {g}: {by.get(g, 0)} < {m}" for g, m in TEST_MIN.items() if by.get(g, 0) < m]
        else:
            if len(ans) < 15 or len(una) < 3:
                problems.append("dev needs >= 15 answerable and >= 3 unanswerable")
            problems += [f"dev has no {g} question" for g in TEST_MIN if not by.get(g)]

    # evidence
    seen = {}
    for q in qs:
        for ev in q.get("evidence", []):
            pg = ev["pdf_page"]
            if pg not in pages:
                problems.append(f"{q['id']}: pdf_page {pg} does not exist")
                continue
            if str(pages[pg]["page_label"]) != str(ev.get("printed_page")):
                problems.append(f"{q['id']}: printed_page {ev.get('printed_page')} != label {pages[pg]['page_label']} of pdf p{pg}")
            text = pages[pg]["text"]
            if ev.get("region"):
                r = regions.get(ev["region"])
                if not r or r["pdf_page"] != pg:
                    problems.append(f"{q['id']}: region {ev['region']} not on pdf p{pg}")
                else:
                    ev["bbox"] = r["bbox"]
                    text = r["text"] or text
            for part in [p.strip() for p in ev["quote_or_value"].split(" ; ")]:
                if "~" in part or "(visual" in part:
                    visual.append(f"{q['id']} p{pg}: {part}")
                    continue
                res = find(part, text)
                if res == "missing":
                    res2 = find(part, pages[pg]["text"])
                    if res2 == "missing":
                        problems.append(f"{q['id']} p{pg}: evidence not found in text layer: {part!r}")
                        continue
                    res = res2
                if res == "tokens":
                    token_only.append(f"{q['id']} p{pg}: {part}")
                key = (pg, norm(part))
                if key in seen and seen[key][1] != q["split"]:
                    problems.append(f"dev/test overlap: {q['id']} and {seen[key][0]} share evidence {part!r} on p{pg}")
                seen.setdefault(key, (q["id"], q["split"]))

    # absence checks
    print("\nAbsence checks (hit pages per pattern):")
    for q in qs:
        if q["answerable"]:
            continue
        for pat in q["absence_check"]["patterns"]:
            hits = sorted({p for p, v in pages.items() if re.search(pat, v["text"], re.I | re.M)})
            print(f"  {q['id']} /{pat}/: {len(hits)} pages {hits[:25]}")

    print(f"\nVisual-only values to confirm on the page image ({len(visual)}):")
    for v in visual:
        print("  ", v)
    print(f"\nFound only as separate tokens (label and value printed apart; confirm pairing on the image) ({len(token_only)}):")
    for v in token_only:
        print("  ", v)
    flagged = [q["id"] for q in qs if q.get("needs_visual_check")]
    print(f"\nQuestions with needs_visual_check: {flagged}")
    print(f"\nPROBLEMS ({len(problems)}):")
    for p in problems:
        print("  ", p)
    if args.write:
        BENCH.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(f"wrote bbox into {BENCH.relative_to(ROOT)}")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
