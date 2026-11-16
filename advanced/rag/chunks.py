"""Build the index units (chunks) from the P8.2 extraction outputs. Every chunk keeps its link to the PDF:
pdf_page, printed page label, kind, region id and bbox (PDF points, top-left origin).

kinds
  text     body text of a page with every figure/table region cut out (pdfplumber outside_bbox), split into
           paragraph groups of <= MAX_CHARS. Box text is ordinary text.
  figure   one per figure region: caption title + the words printed inside the figure (labels, data labels,
           axis ticks) + the vision-model description (marked as model-generated; '~' = approximate reading).
  table    one per table: row list + the parsed table as Markdown (cells as printed) + parser notes (source typos).
  table_row one per table row: table title, unit, row path in the hierarchy, values by year (added after dev v1).
  profile  one per country/aggregate profile page: a card rendered from the layout parse (profiles.jsonl):
           header tags, total, Figure 2 creditor blocks, Figure 3 ratios, Figure 4 terms, unit.
Chunk ids are readable and stable: p028-table-1, p030-figure-1, p260-profile, p019-text-2.
No benchmark data is read here.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROC = ROOT / "advanced" / "data" / "processed"
INDEX = ROOT / "advanced" / "data" / "index"
CHUNKS = INDEX / "chunks.jsonl"
MAX_CHARS = 1200
MAX_DESC, MAX_WORDS = 1800, 900  # caps for figure chunks (one scatter-plot description was 11k chars)
GUIDE_SPLIT_X, GUIDE_SPLIT_Y = 316, 392  # p136 layout (points): left text column | sample page; full width below
SOURCE_ID = "idr-2026"


def _jsonl(path: Path) -> list[dict]:
    return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]


def _chunk(cid, kind, page, label, text, **meta):
    return {"id": cid, "kind": kind, "source_id": SOURCE_ID, "page": page, "pages": [page], "page_label": label,
            "text": text.strip(), "metadata": {"kind": kind, **meta}}


def _join(lines: list[str]) -> str:
    """Join wrapped lines; a line ending in '-' continues the word ('IDA-' + 'eligible'). A mid-line
    suspended hyphen ('Low- and Middle-Income') is left as printed."""
    out = ""
    for s in lines:
        cont = out.endswith("-") and not s.startswith(("and ", "or ", "to "))  # 'low-' / 'and middle-income'
        out = out + s if cont else (out + " " + s if out else s)
    return out


def _split_paragraphs(text: str) -> list[str]:
    """Group lines into paragraphs (blank line, bullet, or a short line ending a sentence), then pack <= MAX_CHARS."""
    paras, cur = [], []
    for line in text.splitlines():
        s = line.strip()
        if not s:
            continue
        if cur and (s.startswith(("•", "Box ")) or (len(cur[-1]) < 60 and cur[-1].endswith((".", ":")))):
            paras.append(_join(cur))
            cur = []
        cur.append(s)
    if cur:
        paras.append(_join(cur))
    out, buf = [], ""
    for p in paras:
        if buf and len(buf) + 1 + len(p) > MAX_CHARS:
            out.append(buf)
            buf = ""
        while len(p) > MAX_CHARS:  # very long paragraph: cut at a sentence end
            cut = p.rfind(". ", 0, MAX_CHARS) + 1 or MAX_CHARS
            out.append((buf + " " + p[:cut]).strip())
            buf, p = "", p[cut:].strip()
        buf = (buf + " " + p).strip()
    if buf:
        out.append(buf)
    return out


def _table_row_chunks(cid: str, pg: int, label: str, r: dict, tab: dict) -> list[dict]:
    """One small chunk per table row (added after dev v1: the number-only Markdown table was never retrieved -
    BM25 length penalty, weak embedding). Each row names the table, unit, row path and every year's value as printed."""
    out, stack = [], []
    for k, row in enumerate(tab["rows"], 1):
        while stack and stack[-1][0] >= row["level"]:
            stack.pop()
        path = " > ".join([s[1] for s in stack] + [row["row"]])
        stack.append((row["level"], row["row"]))
        vals = "; ".join(f"{y}: {v}" for y, v in zip(tab["years"], row["raw"]))
        notes = [i for i in tab["issues"] if i.startswith(repr(row["row"]))]
        text = (f"{r['title']} ({tab['unit']}). Row: {path}" + (f" [{row['section']}]" if row["section"] else "")
                + f". Values by year as printed: {vals}." + (" Note: " + " ".join(notes) if notes else ""))
        out.append(_chunk(f"{cid}-row{k:02d}", "table_row", pg, label, text, region=r["id"], bbox=r["bbox"],
                          title=f"{r['title']} - {row['row']}"))
    return out


def _profile_card(p: dict) -> str:
    name = p["entity"].title().replace("And ", "and ").replace("Of", "of").replace("’S", "’s")
    lines = [f"{name}: country/aggregate profile page ({p['entity']}). {p['unit']}.", f"Tags: {p['header']}",
             f"TOTAL EXTERNAL DEBT STOCK, 2025: {p['total_external_debt_2025']} ({p['change_from_2024']}).",
             "Figure 2 External debt by creditor and creditor type in 2025 (block diagram):"]
    for sec, v in p["figure2"].items():
        place = v.get("placement", {})
        items = "; ".join(f"{k} {val if val is not None else '(value not printed)'}"
                          + (f" [{place[k]}]" if place.get(k, "labelled block") != "labelled block" else "")
                          for k, val in v["items"].items())
        lines.append(f"- {sec} {v['total']}: {items}")
    if p["figure3_ratios_2025"]:
        lines.append("Figure 3 Debt ratios, 2025 value (change): " + "; ".join(
            f"{k} {v['value']} ({v['change']})" for k, v in p["figure3_ratios_2025"].items()))
    if p["figure4_terms_2025_official_then_private"]:
        lines.append("Figure 4 Average terms on new commitments, 2025, official creditors then private creditors "
                     "(maturity, grace period, interest rate; '..' = no new commitments): "
                     + p["figure4_terms_2025_official_then_private"])
    if p["issues"]:
        lines.append("Extraction note: some Figure 2 blocks are too small to show a value on the page.")
    return "\n".join(lines)


def build_chunks() -> list[dict]:
    import pdfplumber
    source = json.loads((ROOT / "advanced" / "data" / "source.json").read_text(encoding="utf-8"))
    pages = {p["pdf_page"]: p for p in _jsonl(PROC / "pages.jsonl")}
    regions = json.loads((PROC / "regions.json").read_text(encoding="utf-8"))
    figs = {f["id"]: f for f in _jsonl(PROC / "figures.jsonl")}
    profiles = {p["pdf_page"]: p for p in _jsonl(PROC / "profiles.jsonl")}
    by_page: dict[int, list[dict]] = {}
    for r in regions:
        by_page.setdefault(r["pdf_page"], []).append(r)
    chunks: list[dict] = []
    with pdfplumber.open(ROOT / source["local_file"]) as pdf:
        for pg, meta in pages.items():
            label = meta["page_label"]
            regs = by_page.get(pg, [])
            if pg in profiles:
                p = profiles[pg]
                chunks.append(_chunk(f"p{pg:03d}-profile", "profile", pg, label, _profile_card(p),
                                     region=p["id"], bbox=[0, 0, 612, 792], title=p["entity"]))
                continue
            # body text outside every region on the page
            page = pdf.pages[pg - 1]
            for r in regs:
                if r["kind"] in ("figure", "table") and r["bbox"][3] - r["bbox"][1] < 780:
                    page = page.outside_bbox(r["bbox"])
            full_page_fig = any(r["bbox"][3] - r["bbox"][1] >= 780 for r in regs)
            text = "" if full_page_fig else (page.extract_text() or "")
            for n, part in enumerate(_split_paragraphs(text), 1):
                if len(part) < 40:  # running heads / page numbers only
                    continue
                chunks.append(_chunk(f"p{pg:03d}-text-{n}", "text", pg, label, part))
            counters = {"figure": 0, "table": 0}
            for r in regs:
                counters[r["kind"]] += 1
                cid = f"p{pg:03d}-{r['kind']}-{counters[r['kind']]}"
                if r["kind"] == "table":
                    md = (PROC / "tables" / f"{r['id']}.md").read_text(encoding="utf-8")
                    tab = json.loads((PROC / "tables" / f"{r['id']}.json").read_text(encoding="utf-8"))
                    rows_line = "Rows: " + "; ".join(x["row"] for x in tab["rows"]) + f". Columns: years {tab['years'][0]}-{tab['years'][-1]}."
                    chunks.append(_chunk(cid, "table", pg, label, f"{rows_line}\n{md}", region=r["id"], bbox=r["bbox"],
                                         title=r["title"]))
                    chunks += _table_row_chunks(cid, pg, label, r, tab)
                elif r["id"].startswith("guide_"):
                    # annotated guide page: explanations in the left column + full-width bottom part, read in
                    # reading order (the raw text layer interleaves them with the miniature sample page; dev v2 ad04)
                    pgobj = pdf.pages[pg - 1]
                    left = pgobj.crop((0, 100, GUIDE_SPLIT_X, GUIDE_SPLIT_Y)).extract_text() or ""
                    bottom = pgobj.crop((0, GUIDE_SPLIT_Y, pgobj.width, pgobj.height)).extract_text() or ""
                    body = (f"{r['title']} (annotated layout of every profile page; the right side shows a miniature "
                            f"sample page for Belize)\n{_join([l for l in left.splitlines() if l.strip()])}\n"
                            f"{_join([l for l in bottom.splitlines() if l.strip()])}")
                    chunks.append(_chunk(cid, "figure", pg, label, body, region=r["id"], bbox=r["bbox"], title=r["title"]))
                else:
                    f = figs.get(r["id"], {})
                    desc = f.get("description") or "(no model description)"
                    if len(desc) > MAX_DESC:  # scatter plots: the model lists every point; keep the head
                        desc = desc[:MAX_DESC].rsplit("\n", 1)[0] + "\n[... description truncated]"
                    body = (f"{r['title']}\nWords printed in the figure: {re.sub(r'\s+', ' ', r['text'])[:MAX_WORDS]}\n"
                            f"Model-generated description ({f.get('model', 'n/a')}; '~' = approximate reading from the axis):\n{desc}")
                    chunks.append(_chunk(cid, "figure", pg, label, body, region=r["id"], bbox=r["bbox"], title=r["title"]))
    return chunks


def main():
    INDEX.mkdir(parents=True, exist_ok=True)
    chunks = build_chunks()
    ids = [c["id"] for c in chunks]
    assert len(ids) == len(set(ids)), "duplicate chunk ids"
    CHUNKS.write_text("".join(json.dumps(c, ensure_ascii=False) + "\n" for c in chunks), encoding="utf-8")
    kinds = {}
    for c in chunks:
        kinds[c["kind"]] = kinds.get(c["kind"], 0) + 1
    lens = sorted(len(c["text"]) for c in chunks)
    print(f"{len(chunks)} chunks -> {CHUNKS.relative_to(ROOT)}; by kind {kinds}; chars median {lens[len(lens)//2]}, max {lens[-1]}")


if __name__ == "__main__":
    main()
