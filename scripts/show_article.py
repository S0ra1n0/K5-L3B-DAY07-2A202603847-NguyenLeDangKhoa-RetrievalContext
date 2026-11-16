"""Print every chunk of one article (all parts), with pages, for benchmark authoring/review.

Usage: python -X utf8 scripts/show_article.py 2019 111 [2012 110 ...]
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHUNKS = ROOT / "data" / "day6" / "chunks_B.jsonl"


def main(argv):
    if len(argv) < 2 or len(argv) % 2:
        raise SystemExit("usage: show_article.py YEAR ARTICLE [YEAR ARTICLE ...]")
    rows = [json.loads(l) for l in CHUNKS.read_text(encoding="utf-8").splitlines() if l.strip()]
    for year, article in zip(argv[::2], argv[1::2]):
        hits = [r for r in rows if r["metadata"]["year"] == int(year) and r["metadata"].get("article") == int(article)]
        print(f"===== {year} Điều {article}: {len(hits)} chunk")
        for r in sorted(hits, key=lambda r: r["metadata"].get("part", 1)):
            m = r["metadata"]
            print(f"--- id={r['chunk_id']} doc={r['document_id']} pages={m['pages']} part={m.get('part')}/{m.get('parts')}")
            print(r["text"])


if __name__ == "__main__":
    main(sys.argv[1:])
