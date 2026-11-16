"""Take in the advanced-challenge document (a local PDF, or a URL you approved) and record its provenance.

Usage (from the repo root):
  .venv/Scripts/python -X utf8 advanced/scripts/intake.py --file "C:/path/report.pdf" --title "..." --publisher "..." --license "..."
  .venv/Scripts/python -X utf8 advanced/scripts/intake.py --url "https://.../report.pdf" --title "..." --publisher "..." --license "..."

What it does: copies/downloads the PDF to advanced/data/raw/ (gitignored), computes sha256, counts pages,
reads PDF metadata, measures how many pages have a text layer (scanned pages need OCR), counts embedded
images per page, and writes advanced/data/source.json. It does not extract or index anything yet.
Checks ADVANCED.md: >= 100 pages. Tables/images/charts must still be confirmed by reading the document.
"""
import argparse
import datetime as dt
import hashlib
import json
import shutil
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "advanced" / "data" / "raw"
SOURCE = ROOT / "advanced" / "data" / "source.json"
MAX_BYTES = 300 * 1024 * 1024


def fetch(url: str, dest: Path) -> None:
    req = urllib.request.Request(url, headers={"User-Agent": "day7-lab-intake/1.0"})
    with urllib.request.urlopen(req, timeout=120) as r, open(dest, "wb") as f:
        ctype = r.headers.get("Content-Type", "")
        if "pdf" not in ctype.lower() and not url.lower().endswith(".pdf"):
            raise SystemExit(f"URL does not look like a PDF (Content-Type: {ctype!r})")
        total = 0
        while chunk := r.read(1 << 20):
            total += len(chunk)
            if total > MAX_BYTES:
                raise SystemExit("file larger than 300 MB, stopped")
            f.write(chunk)


def main():
    ap = argparse.ArgumentParser()
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--file", type=Path)
    src.add_argument("--url")
    ap.add_argument("--title", required=True)
    ap.add_argument("--publisher", required=True)
    ap.add_argument("--license", required=True, help="usage rights / license text or link")
    ap.add_argument("--version", default="", help="edition, year or publication date")
    args = ap.parse_args()
    RAW.mkdir(parents=True, exist_ok=True)
    name = (args.file.name if args.file else args.url.rstrip("/").split("/")[-1].split("?")[0]) or "document.pdf"
    if not name.lower().endswith(".pdf"):
        name += ".pdf"
    dest = RAW / name
    if args.file:
        shutil.copyfile(args.file, dest)
    else:
        fetch(args.url, dest)
    data = dest.read_bytes()
    if not data.startswith(b"%PDF"):
        dest.unlink()
        raise SystemExit("not a PDF file (missing %PDF header); removed")
    from pypdf import PdfReader
    reader = PdfReader(str(dest))
    pages, text_pages, image_counts = len(reader.pages), 0, []
    for p in reader.pages:
        if len((p.extract_text() or "").strip()) >= 200:
            text_pages += 1
        try:
            image_counts.append(len(p.images))
        except Exception:
            image_counts.append(None)
    meta = {k.lstrip("/"): str(v) for k, v in (reader.metadata or {}).items()}
    record = {"title": args.title, "publisher": args.publisher, "version": args.version, "license": args.license,
              "source_url": args.url, "local_file": str(dest.relative_to(ROOT)).replace("\\", "/"),
              "original_filename": args.file.name if args.file else None,
              "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data), "pages": pages,
              "pages_with_text_layer": text_pages,
              "pages_with_embedded_images": sum(1 for c in image_counts if c),
              "pdf_metadata": meta, "taken_in_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
              "meets_100_pages": pages >= 100}
    SOURCE.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: record[k] for k in ("local_file", "pages", "pages_with_text_layer",
                                             "pages_with_embedded_images", "meets_100_pages", "sha256")},
                     ensure_ascii=False, indent=2))
    if pages < 100:
        print("WARNING: fewer than 100 pages; ADVANCED.md requires >= 100", file=sys.stderr)


if __name__ == "__main__":
    main()
