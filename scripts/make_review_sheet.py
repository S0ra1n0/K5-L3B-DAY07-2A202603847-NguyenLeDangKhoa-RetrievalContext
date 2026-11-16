"""Build a labeling sheet (CSV for editing + Markdown for reading) from agent traces of one split.

One row per (config, question). Columns ai_* are drafted by Claude; human_* are filled by the student
(roadmap H4/H6). Final labels = human_* when filled, otherwise ai_* (reported as "AI draft, not reviewed").
Run: .venv/Scripts/python -X utf8 scripts/make_review_sheet.py dev agent_dense_k3 agent_hybrid_rrf ...
Outputs: results/review/agent_review_<split>.csv (UTF-8 with BOM for Excel) and .md
Existing labels in the CSV are kept when the sheet is rebuilt.
"""
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.data_io import load_benchmark, load_chunks  # noqa: E402

COLS = ["config", "query_id", "answerable", "question", "expected", "status", "answer", "citations",
        "ai_answer_grade", "ai_citation_support", "ai_abstention_correct", "ai_reason",
        "human_answer_grade", "human_citation_support", "human_abstention_correct", "human_reason", "reviewed"]
LABEL_COLS = [c for c in COLS if c.startswith(("ai_", "human_")) or c == "reviewed"]


def main():
    split, cfgs = sys.argv[1], sys.argv[2:]
    questions = {q["id"]: q for q in load_benchmark(split=split)}
    chunks = {c["id"]: c for c in load_chunks()}
    out = ROOT / "results" / "review" / f"agent_review_{split}.csv"
    old = {}
    if out.exists():
        with open(out, encoding="utf-8-sig", newline="") as f:
            old = {(r["config"], r["query_id"]): r for r in csv.DictReader(f)}
    rows, md = [], [f"# Phiếu chấm agent · {split}", "",
                    "Đọc từng câu: so câu trả lời với đáp án/lý do thiếu bằng chứng, rồi mở đoạn được cite (in ngay bên dưới) "
                    "để xác nhận đoạn đó thực sự chứa khẳng định. Sửa nhãn trong file CSV cùng tên (cột human_*).", ""]
    for cfg in cfgs:
        traces = json.loads((ROOT / "results" / "agent" / f"{cfg}_{split}" / "traces.json").read_text(encoding="utf-8"))
        for t in traces:
            q = questions[t["query_id"]]
            expected = q["expected_answer"] if q["answerable"] else f"(thiếu bằng chứng) {q['absence_reason']}"
            row = {"config": cfg, "query_id": t["query_id"], "answerable": q["answerable"], "question": q["question"],
                   "expected": expected, "status": t["status"], "answer": t.get("answer") or t.get("error", ""),
                   "citations": ";".join(t.get("citations", []))}
            prev = old.get((cfg, t["query_id"]), {})
            for c in LABEL_COLS:
                row[c] = prev.get(c, "")
            rows.append(row)
            md += [f"## {cfg} · {t['query_id']} · status `{t['status']}`", "",
                   f"**Câu hỏi:** {q['question']}", "", f"**Kỳ vọng:** {expected}", "",
                   f"**Agent trả lời:** {row['answer']}", "",
                   f"**Lượt tìm:** " + "; ".join(f"`{e['query']}` (filter {e['filter']}, {e['filter_source']})"
                                                for e in t.get("events", []) if e.get("event") == "search"), ""]
            for cid in t.get("citations", []):
                c = chunks[cid]
                md += [f"> **[{cid}]** {c['source_id']} · Điều {c['metadata'].get('article')} · trang {c['pages']}", ">",
                       "> " + c["text"].replace("\n", " ")[:900], ""]
            if row["ai_reason"]:
                md += [f"*Nháp AI:* grade={row['ai_answer_grade']} · citation={row['ai_citation_support']} · "
                       f"abstention={row['ai_abstention_correct']} · {row['ai_reason']}", ""]
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        w.writeheader()
        w.writerows(rows)
    out.with_suffix(".md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"{len(rows)} rows -> {out}")


if __name__ == "__main__":
    main()
