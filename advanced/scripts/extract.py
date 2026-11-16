"""P8.2 extraction for the advanced document (International Debt Report 2026).

Stages (run in order; each reads the previous stage's output):
  text     -> processed/pages.jsonl      text of every page (pdfplumber), PDF page index + printed page label
  regions  -> processed/regions.json     numbered Figure/Table regions (caption .. end of Source/Note block, bbox in PDF points)
                                         + one region per country/aggregate profile page
  render   -> processed/pages_img/*.png  full-page renders (gitignored); processed/figures/<id>.png crops of every region
  tables   -> processed/tables/<id>.csv/.md  rows x years parsed from the text layer inside each Table bbox
  describe -> processed/figures.jsonl    vision-model description of every region crop (Ollama, local)
  report   -> processed/extraction_stats.json  coverage stats + numbers the model states that are not in the text layer

Usage: .venv/Scripts/python -X utf8 advanced/scripts/extract.py <stage> [--only id1,id2] [--limit N]
Coordinates: bbox = [x0, top, x1, bottom] in PDF points, origin top-left (pdfplumber convention), page 612x792.
"""
import argparse
import base64
import csv
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ADV = ROOT / "advanced"
SOURCE = ADV / "data" / "source.json"
PROC = ADV / "data" / "processed"
PAGES = PROC / "pages.jsonl"
REGIONS = PROC / "regions.json"
PAGE_IMG = PROC / "pages_img"
FIG_DIR = PROC / "figures"
TAB_DIR = PROC / "tables"
FIGURES = PROC / "figures.jsonl"

CAPTION = re.compile(r"^(Figure|Table)\s+(\d+[A-Z]?\.\d+)\s+(\S.*)$")
SOURCE_LINE = re.compile(r"^(Sources?|Note|Notes|a\.|b\.|c\.|d\.)[:\s]")
PROFILE_MARK = "TOTAL EXTERNAL DEBT STOCK, 2025"
# crop render scale (1.0 = 72 dpi). Figures/tables 3.0 (216 dpi). Profile pages are whole pages: 1.5 (108 dpi,
# 918x1188 px) keeps their large labels readable at about 1/4 of the vision tokens of 3.0 (~4,300 tokens per page,
# ~85 s/page on the throttled laptop GPU); most profile numbers are also in the text layer.
CROP_SCALE = {"figure": 3.0, "table": 3.0, "profile": 1.5}


def pdf_path() -> Path:
    return ROOT / json.loads(SOURCE.read_text(encoding="utf-8"))["local_file"]


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")


# ---------------------------------------------------------------- text
def stage_text(args):
    import pdfplumber
    from pypdf import PdfReader
    labels = PdfReader(str(pdf_path())).page_labels
    rows = []
    with pdfplumber.open(pdf_path()) as pdf:
        for i, p in enumerate(pdf.pages, 1):
            text = p.extract_text() or ""
            kind = "profile" if PROFILE_MARK in text else "body"
            rows.append({"pdf_page": i, "page_label": labels[i - 1], "kind": kind,
                         "chars": len(text.strip()), "text": text})
    write_jsonl(PAGES, rows)
    empty = [r["pdf_page"] for r in rows if r["chars"] < 30]
    print(f"{len(rows)} pages -> {PAGES.relative_to(ROOT)}; profiles={sum(r['kind'] == 'profile' for r in rows)}; "
          f"near-empty pages={empty}")


# ---------------------------------------------------------------- regions
def _region_from_caption(lines, k, page_w):
    """Caption line k .. last line of the Source/Note block that follows it."""
    cap = lines[k]
    title = cap["text"]
    # caption title may wrap onto the next line (same left edge, tight spacing)
    if k + 1 < len(lines):
        nxt = lines[k + 1]
        if abs(nxt["x0"] - cap["x0"]) < 3 and nxt["top"] - cap["bottom"] < 4 and not SOURCE_LINE.match(nxt["text"]):
            if len(cap["text"]) > 60 and nxt["x1"] - nxt["x0"] < 0.9 * (cap["x1"] - cap["x0"]) + 200:
                title += " " + nxt["text"]
    end = None
    for j in range(k + 1, len(lines)):
        if CAPTION.match(lines[j]["text"]):
            break
        if lines[j]["text"].startswith(("Source", "Sources")):
            end = j
            # continue through the Source/Note block: consecutive tightly spaced lines
            while end + 1 < len(lines) and lines[end + 1]["top"] - lines[end]["bottom"] < 6 \
                    and not CAPTION.match(lines[end + 1]["text"]) and lines[end + 1]["x0"] < cap["x0"] + 40:
                end += 1
            break
    if end is None:
        # figure continues on the next page ("(continued)" part carries the Source line):
        # take everything down to the last body line above the running footer / page number
        body = [j for j in range(k + 1, len(lines))
                if not re.fullmatch(r"[\divxlc]+", lines[j]["text"].strip()) and lines[j]["bottom"] < 750]
        nxt_cap = next((j for j in body if CAPTION.match(lines[j]["text"])), None)
        body = [j for j in body if nxt_cap is None or j < nxt_cap]
        if not body:
            return None, title
        end = body[-1]
    sub = lines[k:end + 1]
    x0 = min(cap["x0"], 40.0) if cap["x0"] < 60 else cap["x0"] - 4
    bbox = [round(x0, 1), round(cap["top"] - 4, 1), round(page_w - 36, 1),
            round(max(l["bottom"] for l in sub) + 4, 1)]
    return bbox, title


def stage_regions(args):
    import pdfplumber
    pages = {r["pdf_page"]: r for r in read_jsonl(PAGES)}
    regions, seen = [], set()
    with pdfplumber.open(pdf_path()) as pdf:
        for i, p in enumerate(pdf.pages, 1):
            meta = pages[i]
            first = (meta["text"].splitlines() or [""])[0].strip()
            if first.startswith("HOW TO READ"):  # annotated layout diagram, not a country profile
                regions.append({"id": f"guide_p{i:03d}", "kind": "figure", "number": None,
                                "title": "How to Read the Aggregate and Country Profiles", "pdf_page": i,
                                "page_label": meta["page_label"],
                                "bbox": [0, 0, round(p.width, 1), round(p.height, 1)], "text": meta["text"]})
                continue
            if meta["kind"] == "profile":
                regions.append({"id": f"profile_p{i:03d}", "kind": "profile", "number": None, "title": first,
                                "pdf_page": i, "page_label": meta["page_label"],
                                "bbox": [0, 0, round(p.width, 1), round(p.height, 1)],
                                "text": meta["text"]})
                continue
            lines = p.extract_text_lines()
            for k, ln in enumerate(lines):
                m = CAPTION.match(ln["text"])
                if not m:
                    continue
                kind, num = m.group(1).lower(), m.group(2)
                if (kind, num, i) in seen:
                    continue
                bbox, title = _region_from_caption(lines, k, p.width)
                if bbox is None:
                    print(f"  p{i}: {kind} {num}: region end not found, skipped (check by hand)")
                    continue
                seen.add((kind, num, i))
                crop = p.crop((bbox[0], bbox[1], bbox[2], bbox[3]))
                regions.append({"id": f"{'fig' if kind == 'figure' else 'tab'}_{num.replace('.', '_')}",
                                "continued": "(continued)" in title,
                                "kind": kind, "number": num, "title": title, "pdf_page": i,
                                "page_label": meta["page_label"], "bbox": bbox,
                                "text": crop.extract_text() or ""})
    # a figure split over two pages -> one region per page, ids suffixed with the PDF page
    counts = {}
    for r in regions:
        counts[r["id"]] = counts.get(r["id"], 0) + 1
    for r in regions:
        if counts[r["id"]] > 1:
            r["id"] = f"{r['id']}_p{r['pdf_page']:03d}"
    REGIONS.write_text(json.dumps(regions, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    by = {}
    for r in regions:
        by[r["kind"]] = by.get(r["kind"], 0) + 1
    print(f"{len(regions)} regions -> {REGIONS.relative_to(ROOT)}: {by}")


# ---------------------------------------------------------------- render
def stage_render(args):
    import pypdfium2 as pdfium
    PAGE_IMG.mkdir(parents=True, exist_ok=True)
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    regions = json.loads(REGIONS.read_text(encoding="utf-8"))
    doc = pdfium.PdfDocument(str(pdf_path()))
    page_scale = 2.0  # 144 dpi full pages
    for i in range(len(doc)):
        out = PAGE_IMG / f"p{i + 1:03d}.png"
        if not out.exists():
            doc[i].render(scale=page_scale).to_pil().save(out)
    if args.kinds:
        regions = [r for r in regions if r["kind"] in args.kinds.split(",")]
    for r in regions:
        out = FIG_DIR / f"{r['id']}.png"
        if out.exists() and not args.force:
            continue
        crop_scale = CROP_SCALE.get(r["kind"], 3.0)
        img = doc[r["pdf_page"] - 1].render(scale=crop_scale).to_pil()
        x0, t, x1, b = r["bbox"]
        img.crop((int(x0 * crop_scale), int(t * crop_scale), int(x1 * crop_scale), int(b * crop_scale))).save(out)
    print(f"rendered {len(doc)} pages -> {PAGE_IMG.relative_to(ROOT)}; {len(regions)} crops -> {FIG_DIR.relative_to(ROOT)}")


# ---------------------------------------------------------------- tables
NUM = r"[–−-]?\d[\d,\.]*|\.\."          # the report prints minus as an en dash (–)
VALS_TAIL = re.compile(rf"((?:\s*(?:{NUM}))+)\s*$")


def to_number(raw: str):
    """Printed cell -> float. '8.182.1' (two dots, a typo in the source for 8,182.1) is read as thousands-dot."""
    if raw == "..":
        return None
    s = raw.replace("–", "-").replace("−", "-")
    if re.fullmatch(r"-?\d{1,3}\.\d{3}\.\d+", s):
        head, tail = s.rsplit(".", 1)
        s = head.replace(".", "") + "." + tail
    return float(s.replace(",", ""))


def stage_tables(args):
    """Rows from the text lines inside each Table bbox. Keeps each cell as printed (raw) plus a parsed number.
    The label's left edge (x0) gives the row's level in the hierarchy. A label wrapped over several lines
    (e.g. 'World Bank' / numbers / '(IBRD and IDA)') is joined onto the numeric line it surrounds; label-only
    lines that belong to no numeric line are section headings (e.g. 'Memorandum item')."""
    import pdfplumber
    TAB_DIR.mkdir(parents=True, exist_ok=True)
    regions = [r for r in json.loads(REGIONS.read_text(encoding="utf-8")) if r["kind"] == "table"]
    with pdfplumber.open(pdf_path()) as pdf:
        for r in regions:
            lines = pdf.pages[r["pdf_page"] - 1].crop(r["bbox"]).extract_text_lines()
            texts = [l["text"].strip() for l in lines]
            hi = next(i for i, t in enumerate(texts) if re.fullmatch(r"(?:\d{4}\s*)+", t))
            years = texts[hi].split()
            unit = next((t for t in texts[:hi] if "US$" in t or "percent" in t.lower()), "")
            stop = next((i for i, t in enumerate(texts) if t.startswith(("Source", "Note"))), len(lines))
            body = lines[hi + 1:stop]
            numeric, labels, issues = [], [], []
            for l in body:  # pass 1: split into numeric lines and label-only lines
                t = l["text"].strip()
                m = VALS_TAIL.search(t)
                vals = re.findall(NUM, m.group(1)) if m else []
                if len(vals) == len(years):
                    numeric.append({"line": l, "label": t[:m.start()].strip(), "raw": vals})
                elif not vals:
                    labels.append(l)
                else:
                    issues.append(f"{t[:50]!r}: {len(vals)} values for {len(years)} years, row skipped")
            used = set()
            for n in numeric:  # pass 2: a numeric line without a label takes the label lines around it
                if n["label"]:
                    n["x0"] = n["line"]["x0"]
                    continue
                near = [lab for lab in labels if abs(lab["top"] - n["line"]["top"]) < 16]
                used.update(id(lab) for lab in near)
                n["label"] = " ".join(lab["text"].strip() for lab in sorted(near, key=lambda x: x["top"]))
                n["x0"] = min((lab["x0"] for lab in near), default=n["line"]["x0"])
            headings = [lab for lab in labels if id(lab) not in used]
            label_x = sorted({round(n["x0"]) for n in numeric if n["label"]})
            levels = {x: i for i, x in enumerate(_cluster(label_x))}
            rows = []
            for n in numeric:
                head = [h["text"].strip() for h in headings if h["top"] < n["line"]["top"]]
                nums = [to_number(v) for v in n["raw"]]
                for v, num in zip(n["raw"], nums):
                    if re.fullmatch(r"[–−-]?\d{1,3}\.\d{3}\.\d+", v):
                        issues.append(f"{n['label']!r}: printed {v!r} (separator typo in the source), read as {num}")
                rows.append({"row": n["label"], "level": levels[_snap(round(n["x0"]), levels)],
                             "section": head[-1] if head else "", "raw": n["raw"], "values": nums})
            with open(TAB_DIR / f"{r['id']}.csv", "w", newline="", encoding="utf-8") as f:
                w = csv.writer(f)
                w.writerow(["row", "level", "section"] + years)
                for row in rows:
                    w.writerow([row["row"], row["level"], row["section"]] + row["raw"])
            md = [f"# {r['title']}", "",
                  f"PDF page {r['pdf_page']} (printed page {r['page_label']}), bbox {r['bbox']}. Unit: {unit or 'see caption'}. "
                  "Cells copied as printed (the source prints minus as –). Indentation = row hierarchy.", "",
                  "| row | " + " | ".join(years) + " |", "|---|" + "---:|" * len(years)]
            md += ["| " + "&nbsp;&nbsp;" * row["level"] + (f"[{row['section']}] " if row["section"] else "") + row["row"]
                   + " | " + " | ".join(row["raw"]) + " |" for row in rows]
            if issues:
                md += ["", "Parser notes:"] + [f"- {x}" for x in issues]
            (TAB_DIR / f"{r['id']}.md").write_text("\n".join(md) + "\n", encoding="utf-8")
            (TAB_DIR / f"{r['id']}.json").write_text(json.dumps(
                {"id": r["id"], "title": r["title"], "pdf_page": r["pdf_page"], "page_label": r["page_label"],
                 "bbox": r["bbox"], "unit": unit, "years": years, "rows": rows, "issues": issues},
                ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
            print(f"{r['id']}: {len(rows)} rows x {len(years)} years; issues={issues}")


def _cluster(xs: list[int], tol: int = 3) -> list[int]:
    """Indent positions closer than tol points are the same level."""
    out = []
    for x in sorted(xs):
        if not out or x - out[-1] > tol:
            out.append(x)
    return out


def _snap(x: int, levels: dict) -> int:
    return min(levels, key=lambda c: abs(c - x))


# ---------------------------------------------------------------- describe (vision)
PROMPT = """You are extracting content from one figure/table region of a World Bank report page, for a search index.
Write plain English, no preamble. Use exactly these sections:
TITLE: the figure/table title as printed.
TYPE: chart type(s) (bar, stacked bar, line, area, scatter, pie, map, diagram, table, ...); list panels a/b/c if any.
AXES_AND_UNITS: x axis, y axis(es), units, scale.
LEGEND: every series/category name.
PRINTED_VALUES: every number printed on the image, each with what it labels (series, year/category, unit). Copy digits exactly.
READ_VALUES: for bars/lines WITHOUT printed numbers, approximate readings from the axis, marked with "~" (e.g. "~350 in 2020").
TRENDS: 2-5 short factual statements of what the figure shows (highest/lowest, direction of change, comparisons).
Do not guess anything that is not visible. If text is unreadable, say so."""

PROFILE_PROMPT = """This is one country (or aggregate) profile page from the World Bank International Debt Report 2026.
Write plain English, no preamble. Sections:
ENTITY: country/aggregate name, region, income group, lending category, population, GNI as printed.
FIGURE_1: total external debt 2015-25: chart type, printed values (copy exactly), and the direction of change; approximate unlabelled years with "~".
FIGURE_2: external debt by creditor and creditor type in 2025: every printed category and value.
FIGURE_3: debt ratios 2015-25: each ratio's printed 2025 value and change, and whether the country line is above, inside or below the shaded 25th-75th percentile band.
FIGURE_4: average terms on new commitments (official vs private): maturity, grace period, interest rate.
UNIT: the unit line printed on the page.
Do not guess anything that is not visible."""


def ollama_vision(image: Path, prompt: str, model: str, base_url: str, timeout: int = 900) -> tuple[str, dict]:
    body = {"model": model, "stream": False, "think": False,
            "options": {"temperature": 0, "presence_penalty": 0, "repeat_penalty": 1.0, "num_ctx": 8192, "seed": 7},
            "messages": [{"role": "user", "content": prompt,
                          "images": [base64.b64encode(image.read_bytes()).decode()]}]}
    req = urllib.request.Request(base_url.rstrip("/") + "/api/chat", data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        out = json.loads(r.read())
    usage = {k: out.get(k) for k in ("prompt_eval_count", "eval_count", "total_duration")}
    return out["message"]["content"].strip(), usage


def stage_describe(args):
    sys.path.insert(0, str(ROOT))
    from src import config
    regions = json.loads(REGIONS.read_text(encoding="utf-8"))
    done = {r["id"]: r for r in read_jsonl(FIGURES)} if FIGURES.exists() else {}
    todo = [r for r in regions if (args.only is None or r["id"] in args.only.split(","))
            and (args.force or r["id"] not in done or done[r["id"]].get("error"))]
    if args.kinds:
        todo = [r for r in todo if r["kind"] in args.kinds.split(",")]
    if args.limit:
        todo = todo[:args.limit]
    print(f"describing {len(todo)} regions with {args.model} (already done: {len(done)})", flush=True)
    for n, r in enumerate(todo, 1):
        img = FIG_DIR / f"{r['id']}.png"
        prompt = PROFILE_PROMPT if r["kind"] == "profile" else PROMPT
        t0 = time.time()
        rec = {"id": r["id"], "kind": r["kind"], "pdf_page": r["pdf_page"], "page_label": r["page_label"],
               "bbox": r["bbox"], "title": r["title"], "image": str(img.relative_to(ROOT)).replace("\\", "/"),
               "model": args.model, "prompt_version": "v1", "crop_scale": CROP_SCALE.get(r["kind"], 3.0)}
        try:
            text, usage = ollama_vision(img, prompt, args.model, config.OLLAMA_BASE_URL)
            rec.update({"description": text, "usage": usage, "error": None})
        except Exception as e:  # record the failure; never invent a description
            rec.update({"description": None, "usage": None, "error": f"{type(e).__name__}: {e}"})
        rec["seconds"] = round(time.time() - t0, 1)
        done[r["id"]] = rec
        order = {x["id"]: k for k, x in enumerate(regions)}
        write_jsonl(FIGURES, sorted(done.values(), key=lambda x: order.get(x["id"], 1e9)))
        print(f"[{n}/{len(todo)}] {r['id']} p{r['pdf_page']} {rec['seconds']}s {'ERROR ' + rec['error'] if rec['error'] else ''}",
              flush=True)


# ---------------------------------------------------------------- profiles (layout parse, no model)
PROFILES = PROC / "profiles.jsonl"
NUM_WORD = re.compile(r"^[–−-]?\d[\d,]*(?:\.\d+)?%?$")


def _is_num(w):
    return bool(NUM_WORD.match(w["text"]))


def _parse_figure2(page, top2, top3):
    """Figure 2 block diagram -> {section: {"total": v, "items": {label: v}}}, from the drawn shapes.
    Measured layout: every block is a filled rectangle (23 or ~42 pt high); its label and value are printed inside it.
    A block too narrow for its label prints only the value (or nothing); its label (and value, if not inside)
    is then a legend entry: a small square of the SAME fill colour followed by the label (and value).
    Section headers (TOTAL EXTERNAL DEBT, PUBLIC & ... BY CREDITOR TYPE, MULTILATERAL, BILATERAL) are caps
    text with the section total printed in a larger font (~8.5) on the same line; a row can hold two."""
    words = [w for w in page.extract_words(extra_attrs=["size"]) if top2 < w["top"] < top3]
    rects = [r for r in page.rects if top2 < r["top"] < top3]
    blocks = [r for r in rects if r["height"] > 15]  # blocks are 23 or ~42 pt high depending on the page
    squares = [r for r in rects if r["height"] < 12 and r["width"] < 12]
    colour = lambda r: tuple(round(c, 2) for c in (r.get("non_stroking_color") or ()))

    heads = []
    for w in words:
        if w["size"] > 8.3 and _is_num(w):
            same = sorted([x for x in words if abs(x["top"] - w["top"]) < 1.5 and not _is_num(x) and x["x0"] < w["x0"]],
                          key=lambda x: x["x0"])
            run, prev = [], None
            for x in reversed(same):  # the caps run nearest to the total (two sections can share a row)
                if prev is not None and prev["x0"] - x["x1"] > 15:
                    break
                run.insert(0, x)
                prev = x
            if run:
                heads.append({"name": " ".join(x["text"] for x in run), "x0": run[0]["x0"], "top": w["top"],
                              "total": w["text"], "items": {}})

    def section_for(x0, top):
        cands = [h for h in heads if h["top"] < top]
        if not cands:
            return None
        row = max(h["top"] for h in cands)
        row_heads = [h for h in cands if abs(h["top"] - row) < 2]
        left = [h for h in row_heads if h["x0"] <= x0 + 8]
        return max(left, key=lambda h: h["x0"]) if left else min(row_heads, key=lambda h: h["x0"])

    inside = lambda w, r: r["x0"] - 1 <= (w["x0"] + w["x1"]) / 2 <= r["x1"] + 1 and r["top"] - 1 <= (w["top"] + w["bottom"]) / 2 <= r["bottom"] + 1
    used = set()
    legend = {}  # colour -> (label, value or None)
    for sq in squares:
        line = sorted([w for w in words if abs((w["top"] + w["bottom"]) / 2 - (sq["top"] + sq["bottom"]) / 2) < 4
                       and w["x0"] > sq["x1"] - 1], key=lambda w: w["x0"])
        run = []
        for w in line:  # stop at the next legend square on the same row
            if any(s is not sq and sq["x1"] < s["x0"] < w["x0"] and abs(s["top"] - sq["top"]) < 4 for s in squares):
                break
            run.append(w)
        used.update(id(w) for w in run)
        val = run[-1]["text"] if run and _is_num(run[-1]) else None
        lab = " ".join(w["text"] for w in (run[:-1] if val else run))
        legend[colour(sq)] = (lab, val, sq)
    issues, seen_colours = [], set()
    for b in sorted(blocks, key=lambda r: (r["top"], r["x0"])):
        ws = sorted([w for w in words if inside(w, b) and id(w) not in used], key=lambda w: (round(w["top"]), w["x0"]))
        nums = [w for w in ws if _is_num(w)]
        lab = " ".join(w["text"] for w in ws if not _is_num(w))
        val = nums[-1]["text"] if nums else None
        if not lab and colour(b) in legend:
            lab, lval, _ = legend[colour(b)]
            seen_colours.add(colour(b))
            val = val or lval
        sec = section_for(b["x0"], b["top"])
        if sec is None or not lab:
            if val:
                issues.append(f"block at x={b['x0']:.0f},y={b['top']:.0f} value {val} without label/section")
            continue
        sec["items"][lab] = val
    for col, (lab, val, sq) in legend.items():  # legend entries whose block is too thin to be drawn as a block
        if col in seen_colours or not val:
            continue
        sec = section_for(sq["x0"], sq["top"] - 30)
        if sec is not None and lab not in sec["items"]:
            sec["items"][lab] = val
    out = {}
    for h in sorted(heads, key=lambda h: (h["top"], h["x0"])):
        out[h["name"]] = {"total": h["total"], "items": h["items"]}
        vals = [v for v in h["items"].values() if v]
        if vals:
            s = sum(float(v.replace(",", "")) for v in vals)
            t = float(h["total"].replace(",", ""))
            if abs(s - t) > max(3, 0.002 * t):
                issues.append(f"{h['name']}: items sum {s:g} != total {t:g}")
        if any(v is None for v in h["items"].values()):
            issues.append(f"{h['name']}: item without value")
    return out, issues


def stage_profiles(args):
    """Structured record per profile page from the text layer + word positions (no vision model)."""
    import pdfplumber
    regions = [r for r in json.loads(REGIONS.read_text(encoding="utf-8")) if r["kind"] == "profile"]
    rows, bad = [], 0
    with pdfplumber.open(pdf_path()) as pdf:
        for r in regions:
            p = pdf.pages[r["pdf_page"] - 1]
            lines = p.extract_text_lines()
            words = p.extract_words(extra_attrs=["size"])
            top2 = next(l["bottom"] for l in lines if l["text"].startswith("Figure 2"))
            top3 = next(l["top"] for l in lines if l["text"].startswith("Figure 3"))
            fig2, issues = _parse_figure2(p, top2, top3)
            text = r["text"]
            unit = next((l for l in text.splitlines() if "unless otherwise indicated" in l), "")
            m = re.search(r"TOTAL EXTERNAL DEBT STOCK, 2025.*?\n.*?([\d,]+)\s*\n?.*?([+\-–]?[\d.]+% from 2024)", text, re.S)
            rl = re.search(r"Debt service / GNI\s*\n(.*?)\n", text)
            ratio_vals = re.findall(r"(\d+%)\s+([+\-–]?[\d.]+%)", rl.group(1)) if rl else []
            names = ["External debt / exports", "External debt / GNI", "Debt service / exports", "Debt service / GNI"]
            terms = re.search(r"Official creditors Private creditors\s*\n(.*?)\n", text)
            first = text.splitlines()[0].strip()
            tags = text.splitlines()[2] if first and len(text.splitlines()) > 2 else ""
            rec = {"id": r["id"], "pdf_page": r["pdf_page"], "page_label": r["page_label"], "entity": first,
                   "unit": unit.strip(), "header": tags.strip(),
                   "total_external_debt_2025": m.group(1) if m else None, "change_from_2024": m.group(2) if m else None,
                   "figure2": fig2,
                   "figure3_ratios_2025": {n: {"value": v, "change": c} for n, (v, c) in zip(names, ratio_vals)},
                   "figure4_terms_2025_official_then_private": terms.group(1).strip() if terms else None,
                   "issues": issues}
            bad += bool(issues)
            rows.append(rec)
    write_jsonl(PROFILES, rows)
    print(f"{len(rows)} profiles -> {PROFILES.relative_to(ROOT)}; with issues: {bad}")
    for rec in rows:
        if rec["issues"] and (args.only is None or rec["id"] in args.only.split(",")):
            print(f"  {rec['id']} {rec['entity']}: {rec['issues']}")


# ---------------------------------------------------------------- report (automatic checks + stats)
def _numbers(s: str) -> list[str]:
    """Numbers in a text, normalised (no thousands commas, ASCII minus); years and tiny integers dropped."""
    out = []
    for m in re.finditer(r"(?<![\w.])[–−-]?\d[\d,]*(?:\.\d+)?", s):
        v = m.group(0).replace("–", "-").replace("−", "-").replace(",", "")
        if re.fullmatch(r"(19|20)\d\d", v) or re.fullmatch(r"-?\d", v):
            continue
        out.append(v.rstrip("."))
    return out


def stage_report(args):
    """Every number the vision model states as printed (not '~' readings) must appear in the region's text layer.
    Unsupported numbers are listed for the P8.3 human check; this does not prove the description is right."""
    pages = read_jsonl(PAGES)
    regions = {r["id"]: r for r in json.loads(REGIONS.read_text(encoding="utf-8"))}
    figs = read_jsonl(FIGURES) if FIGURES.exists() else []
    checks = []
    for f in figs:
        if f.get("error") or not f.get("description"):
            checks.append({"id": f["id"], "status": "error", "error": f.get("error")})
            continue
        text_nums = set(_numbers(regions[f["id"]]["text"]))
        text_nums |= {n.lstrip("-") for n in text_nums}
        stated = []
        for line in f["description"].splitlines():
            if line.strip().upper().startswith(("READ_VALUES", "TRENDS", "TITLE")):
                continue
            stated += [n for n in _numbers(re.sub(r"~\s*[–−-]?\d[\d,.]*", "", line))]
        unsupported = sorted({n for n in stated if n not in text_nums and n.lstrip("-") not in text_nums})
        checks.append({"id": f["id"], "kind": f["kind"], "pdf_page": f["pdf_page"], "stated_numbers": len(set(stated)),
                       "unsupported": unsupported, "seconds": f.get("seconds")})
    ok = [c for c in checks if c.get("status") != "error"]
    stats = {
        "document_pages": len(pages),
        "pages_with_text": sum(p["chars"] >= 30 for p in pages),
        "near_empty_pages": [p["pdf_page"] for p in pages if p["chars"] < 30],
        "profile_pages": sum(p["kind"] == "profile" for p in pages),
        "regions": {k: sum(r["kind"] == k for r in regions.values()) for k in ("figure", "table", "profile")},
        "tables": {p.stem: {"rows": len(json.loads(p.read_text(encoding='utf-8'))["rows"]),
                            "issues": json.loads(p.read_text(encoding='utf-8'))["issues"]}
                   for p in sorted(TAB_DIR.glob("*.json"))},
        "described": len(ok), "describe_errors": len(checks) - len(ok),
        "describe_seconds_total": round(sum(c.get("seconds") or 0 for c in ok), 1),
        "regions_with_unsupported_numbers": sum(bool(c["unsupported"]) for c in ok),
        "stated_numbers_total": sum(c["stated_numbers"] for c in ok),
        "unsupported_numbers_total": sum(len(c["unsupported"]) for c in ok),
    }
    (PROC / "extraction_stats.json").write_text(json.dumps({"stats": stats, "checks": checks}, ensure_ascii=False,
                                                           indent=1) + "\n", encoding="utf-8")
    print(json.dumps(stats, ensure_ascii=False, indent=1))
    for c in ok:
        if c["unsupported"]:
            print(f"  {c['id']} p{c['pdf_page']}: {c['unsupported'][:12]}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("stage", choices=["text", "regions", "render", "tables", "describe", "profiles", "report"])
    ap.add_argument("--only", help="comma-separated region ids")
    ap.add_argument("--kinds", help="comma-separated kinds: figure,table,profile")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--model", default="qwen3.5:9b")
    args = ap.parse_args()
    PROC.mkdir(parents=True, exist_ok=True)
    {"text": stage_text, "regions": stage_regions, "render": stage_render,
     "tables": stage_tables, "describe": stage_describe, "profiles": stage_profiles, "report": stage_report}[args.stage](args)


if __name__ == "__main__":
    main()
