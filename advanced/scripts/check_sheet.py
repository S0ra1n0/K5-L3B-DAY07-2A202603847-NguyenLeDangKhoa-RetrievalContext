"""P8.3: build the human check sheet comparing extracted content with the original PDF.

Sample (fixed seed, stratified): every region whose vision description states a number missing from the text
layer, plus random figures, both tables, random profile pages and random body text pages.
Output: advanced/results/extraction_check.csv (human columns empty) and .md (how to check).
Usage: .venv/Scripts/python -X utf8 advanced/scripts/check_sheet.py
"""
import csv
import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROC = ROOT / "advanced" / "data" / "processed"
OUT = ROOT / "advanced" / "results"


def main():
    rng = random.Random(7)
    regions = {r["id"]: r for r in json.loads((PROC / "regions.json").read_text(encoding="utf-8"))}
    figs = {json.loads(l)["id"]: json.loads(l) for l in (PROC / "figures.jsonl").read_text(encoding="utf-8").splitlines()}
    checks = {c["id"]: c for c in json.loads((PROC / "extraction_stats.json").read_text(encoding="utf-8"))["checks"]}
    pages = [json.loads(l) for l in (PROC / "pages.jsonl").read_text(encoding="utf-8").splitlines()]
    rows = []

    def add(item, kind, page, label, what, extracted, flag=""):
        rows.append({"item": item, "kind": kind, "pdf_page": page, "printed_page": label, "what_to_check": what,
                     "extracted": extracted, "auto_flag": flag, "human_ok": "", "human_note": ""})

    flagged = [i for i, c in checks.items() if (c.get("unsupported") or c.get("status") == "error")
               and regions[i]["kind"] != "profile"]
    fig_ids = [i for i, r in regions.items() if r["kind"] in ("figure", "table") and i not in flagged and i in figs]
    sample = flagged + rng.sample(fig_ids, min(8, len(fig_ids)))
    # profile pages are indexed from the layout parse (profiles.jsonl), not from vision descriptions
    profs = {json.loads(l)["id"]: json.loads(l) for l in (PROC / "profiles.jsonl").read_text(encoding="utf-8").splitlines()}
    prof_flag = [i for i, p in profs.items() if p["issues"]]
    prof_ok = [i for i, p in profs.items() if not p["issues"]]
    for i in prof_flag + rng.sample(prof_ok, 6):
        p = profs[i]
        add(i, "profile", p["pdf_page"], p["page_label"],
            "Figure 2 blocks: every label paired with the right value (compare with the page image); totals, "
            "Figure 3 ratio values/changes, Figure 4 terms, unit line",
            json.dumps({k: p[k] for k in ("entity", "unit", "total_external_debt_2025", "change_from_2024", "figure2",
                                          "figure3_ratios_2025", "figure4_terms_2025_official_then_private")},
                       ensure_ascii=False)[:1500],
            "; ".join(p["issues"]))
    for i in sample:
        r, f, c = regions[i], figs.get(i, {}), checks.get(i, {})
        flag = ("unsupported numbers: " + ", ".join(c["unsupported"][:10])) if c.get("unsupported") else (c.get("error") or "")
        add(i, r["kind"], r["pdf_page"], r["page_label"],
            "Crop covers the whole figure (title..Source); TITLE/TYPE/LEGEND right; every PRINTED_VALUES number "
            "matches the PDF; '~' readings within ~10% of the axis; TRENDS true",
            (f.get("description") or "")[:1500], flag)
    for t in ("tab_1_1", "tab_1_2"):
        tab = json.loads((PROC / "tables" / f"{t}.json").read_text(encoding="utf-8"))
        cells = [(row["row"], y, v) for row in tab["rows"] for y, v in zip(tab["years"], row["raw"])]
        pick = rng.sample(cells, 5)
        add(t, "table", tab["pdf_page"], tab["page_label"],
            f"All {len(tab['rows'])} rows present with the right labels; these 5 cells match the PDF",
            "; ".join(f"{r} / {y} = {v}" for r, y, v in pick), "; ".join(tab["issues"]))
    body = [p for p in pages if p["kind"] == "body" and p["chars"] > 1500]
    for p in rng.sample(body, 5):
        add(f"page_{p['pdf_page']:03d}", "text", p["pdf_page"], p["page_label"],
            "Text matches the page (no missing paragraphs, numbers copied right); note any broken words",
            p["text"][:600])
    OUT.mkdir(parents=True, exist_ok=True)
    with open(OUT / "extraction_check.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print(f"{len(rows)} rows ({len(flagged)} auto-flagged) -> {(OUT / 'extraction_check.csv').relative_to(ROOT)}")


if __name__ == "__main__":
    main()
