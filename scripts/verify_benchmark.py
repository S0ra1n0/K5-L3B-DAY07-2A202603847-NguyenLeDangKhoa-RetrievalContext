"""Check benchmark/questions.json against the corpus before any retrieval run.

Checks: split counts (dev >= 15+2, test >= 5+2); unique IDs; every evidence quote is verbatim
on the gold page (whitespace collapsed) and some chunk of the gold article holds it; each gold
alternative is a hit for at least one chunk (so Hit@k is reachable); filter.year is written in
the question text; dev and test share no gold article; unanswerable questions have
absence_reason + keywords. Writes results/setup/benchmark_verification.json.
Run: python -X utf8 scripts/verify_benchmark.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.data_io import load_benchmark, load_chunks, load_pages  # noqa: E402
from src.metrics import chunk_hit, squash  # noqa: E402

MINIMUM = {"dev": (15, 2), "test": (5, 2)}


def main():
    questions = load_benchmark()
    chunks, pages = load_chunks(), load_pages()
    page_text = {(p["document_id"], p["page"]): squash(p["text"]) for p in pages}
    problems, checked = [], 0
    ids = [q["id"] for q in questions]
    if len(ids) != len(set(ids)):
        problems.append("duplicate ids")
    for split, (min_a, min_u) in MINIMUM.items():
        rows = [q for q in questions if q["split"] == split]
        a, u = sum(q["answerable"] for q in rows), sum(not q["answerable"] for q in rows)
        if a < min_a or u < min_u:
            problems.append(f"{split}: {a} answerable / {u} unanswerable, need {min_a}/{min_u}")
    articles = {"dev": set(), "test": set()}
    for q in questions:
        if q.get("filter", {}).get("year") and str(q["filter"]["year"]) not in q["question"]:
            problems.append(f"{q['id']}: filter year not written in the question")
        if not q["answerable"]:
            if not q.get("absence_reason") or not q.get("absence_check", {}).get("keywords"):
                problems.append(f"{q['id']}: missing absence_reason/keywords")
            if q.get("gold") or q.get("expected_answer"):
                problems.append(f"{q['id']}: unanswerable question must not carry gold/expected_answer")
            continue
        for g in q["gold"]:
            articles[q["split"]].add((g["source_id"], g.get("article")))
            text = page_text.get((g["source_id"], g["page"]))
            for quote in g["evidence"]:
                checked += 1
                if text is None or squash(quote) not in text:
                    found = [pg for (doc, pg), t in page_text.items() if doc == g["source_id"] and squash(quote) in t]
                    problems.append(f"{q['id']}: quote not on {g['source_id']}#p{g['page']} (found on pages {found}): {quote[:60]}")
            art_chunks = [c for c in chunks if c["source_id"] == g["source_id"] and c["metadata"].get("article") == g.get("article")]
            if not any(chunk_hit(c, [g]) for c in chunks):
                note = "quotes split across chunks" if art_chunks else "article not found"
                problems.append(f"{q['id']}: no single chunk hits gold {g['source_id']}#p{g['page']} ({note})")
    overlap = articles["dev"] & articles["test"]
    if overlap:
        problems.append(f"dev/test share gold articles: {sorted(overlap)}")
    report = {"questions": len(questions), "quotes_checked": checked,
              "counts": {s: {"answerable": sum(q["answerable"] for q in questions if q["split"] == s),
                             "unanswerable": sum(not q["answerable"] for q in questions if q["split"] == s)}
                         for s in ("dev", "test")},
              "problems": problems, "ok": not problems}
    out = ROOT / "results" / "setup" / "benchmark_verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    sys.exit(0 if not problems else 1)


if __name__ == "__main__":
    main()
