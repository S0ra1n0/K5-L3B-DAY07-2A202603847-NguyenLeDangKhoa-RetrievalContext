"""Second, independent labeling pass by rule-based text checks; compared with the first (reading-based) AI draft.

This is NOT a human review. It is a different method used to catch contradictions in the first pass:
- required numbers: numbers of the main clause of the expected answer (0/1 ignored) must appear in the answer;
- unsupported numbers: numbers in the answer that appear nowhere in the final context (law years ignored);
- citation check: for each [id], the answer segment ending at that id must (a) mention no other Điều number than
  the cited chunk's, (b) have all its numbers present in the chunk, (c) share >= 50% of its content syllables with it;
- unanswerable: abstain and no numbers in the answer besides law years/article numbers.
auto grade: 2 = required numbers present, none unsupported, final context has evidence; 1 = present but one problem;
0 = required numbers missing or answerable question abstained.
Run: .venv/Scripts/python -X utf8 scripts/second_pass_check.py dev
Writes results/review/second_pass_<split>.csv and conflicts_<split>.md
"""
import csv
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.data_io import load_benchmark, load_chunks  # noqa: E402

YEARS = {"2012", "2019"}
CIT = re.compile(r"\[([0-9a-f]{16}(?:\s*[,;]\s*[0-9a-f]{16})*)\]")  # [id] or grouped [id, id]


def nums(text):
    """Numbers in text, leading zeros dropped; citation IDs ([16 hex chars]) are removed first."""
    out = set()
    for m in re.finditer(r"\d+", CIT.sub(" ", text)):
        out.add(str(int(m.group())))
    return out


def required_numbers(expected):
    """Numbers of the main clause of the expected answer (before '(' or ';'); 0/1 ignored ('01 tháng' = 'một tháng')."""
    main = re.split(r"[(;]", expected)[0]
    return nums(main) - YEARS - {"0", "1"}


def article_refs(text):
    return {str(int(x)) for x in re.findall(r"Điều\s+(\d+)", text)}


def syllables(text):
    return {w for w in re.findall(r"\w+", unicodedata.normalize("NFC", text).casefold()) if len(w) > 2 and not w.isdigit()}


def check_citation(segment, chunk):
    art = chunk["metadata"].get("article")
    refs = article_refs(segment)
    if refs and art is not None and str(art) not in refs:
        return False, f"câu nhắc Điều {sorted(refs)} nhưng cite Điều {art}"
    seg_nums = nums(segment) - YEARS - refs
    missing = {n for n in seg_nums if n not in nums(chunk["text"])}
    if missing:
        return False, f"số {sorted(missing)} không có trong đoạn"
    s = syllables(segment)
    overlap = len(s & syllables(chunk["text"])) / len(s) if s else 1
    if overlap < 0.5:
        return False, f"trùng từ thấp ({overlap:.0%})"
    return True, ""


def main():
    split = sys.argv[1]
    questions = {q["id"]: q for q in load_benchmark(split=split)}
    chunks = {c["id"]: c for c in load_chunks()}
    with open(ROOT / "results" / "review" / f"agent_review_{split}.csv", encoding="utf-8-sig", newline="") as f:
        sheet = list(csv.DictReader(f))
    out_rows, conflicts = [], []
    for r in sheet:
        t = next(x for x in json.loads((ROOT / "results" / "agent" / f"{r['config']}_{split}" / "traces.json").read_text(encoding="utf-8"))
                 if x["query_id"] == r["query_id"])
        q = questions[r["query_id"]]
        answer = t.get("answer") or ""
        ctx_text = " ".join(chunks[i]["text"] for i in t.get("final_context_ids", []))
        notes = []
        # citations
        support, pos, prev_seg = [], 0, ""
        for m in CIT.finditer(answer):
            seg = answer[pos:m.start()]
            if len(syllables(seg)) < 6:   # short connector ("và Điều 106 ... 2019 [id]") continues the previous claim
                seg = prev_seg + " " + seg
            for cid in re.split(r"\s*[,;]\s*", m.group(1)):
                if cid in t.get("citations", []):
                    ok, why = check_citation(seg, chunks[cid])
                    support.append((cid, ok, why))
            prev_seg, pos = seg, m.end()
        by_id = {}
        for cid, ok, why in support:  # one label per cited id: false if any attached segment fails
            prev = by_id.get(cid, (True, ""))
            by_id[cid] = (prev[0] and ok, prev[1] or why)
        cit_labels = [by_id.get(c, (True, ""))[0] for c in t.get("citations", [])]
        notes += [f"[{c[:6]}] {by_id[c][1]}" for c in t.get("citations", []) if c in by_id and not by_id[c][0]]
        if q["answerable"]:
            required = required_numbers(q["expected_answer"])
            missing = {n for n in required if n not in nums(answer)}
            unsupported = (nums(answer) - YEARS - article_refs(answer)) - nums(ctx_text)
            if t["status"] != "answered":
                grade = 0
                notes.append("từ chối câu có đáp án")
            elif missing:
                grade = 0
                notes.append(f"thiếu số bắt buộc {sorted(missing)}")
            else:
                problems = (["số không có trong context " + str(sorted(unsupported))] if unsupported else []) + \
                           ([] if t.get("final_context_has_evidence") else ["context cuối không đủ evidence"])
                grade = 2 if not problems else 1
                notes += problems
            abst = ""
        else:
            grade = ""
            extra = nums(answer) - YEARS - article_refs(answer)
            abst = "true" if t["status"] == "abstain" and not extra else "false"
            if t["status"] != "abstain":
                notes.append("không từ chối (status answered)")
            if extra:
                notes.append(f"có con số {sorted(extra)}")
        row = {"config": r["config"], "query_id": r["query_id"], "auto_answer_grade": grade,
               "auto_citation_support": ";".join("true" if x else "false" for x in cit_labels),
               "auto_abstention_correct": abst, "auto_notes": "; ".join(notes),
               "ai_answer_grade": r["ai_answer_grade"], "ai_citation_support": r["ai_citation_support"],
               "ai_abstention_correct": r["ai_abstention_correct"]}
        diff = [k for k in ("answer_grade", "citation_support", "abstention_correct")
                if str(row[f"auto_{k}"]) != str(row[f"ai_{k}"])]
        row["conflict"] = ",".join(diff)
        out_rows.append(row)
        if diff:
            conflicts.append((row, r["ai_reason"], answer))
    out = ROOT / "results" / "review" / f"second_pass_{split}.csv"
    with open(out, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(out_rows[0]))
        w.writeheader()
        w.writerows(out_rows)
    md = [f"# Mâu thuẫn giữa lượt 1 (AI đọc) và lượt 2 (kiểm tra tự động) · {split}", "",
          f"{len(conflicts)}/{len(out_rows)} dòng khác nhau ở ít nhất một nhãn.", "",
          "| Config | Query | Khác ở | Lượt 1 grade/cit/abst | Lượt 2 grade/cit/abst | Ghi chú lượt 2 |", "|---|---|---|---|---|---|"]
    for row, _, _ in conflicts:
        md.append(f"| {row['config']} | {row['query_id']} | {row['conflict']} | {row['ai_answer_grade']}/{row['ai_citation_support']}/"
                  f"{row['ai_abstention_correct']} | {row['auto_answer_grade']}/{row['auto_citation_support']}/"
                  f"{row['auto_abstention_correct']} | {row['auto_notes']} |")
    (ROOT / "results" / "review" / f"conflicts_{split}.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
