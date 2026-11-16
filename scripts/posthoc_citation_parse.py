"""POST-HOC analysis only: which test outcomes would change if the citation parser also accepted '|' separators
and copied context headers ([id | blld-2012 | năm 2012 | ...]). Found by reading TEST answers, so this is NOT
used to change the official test numbers (RULES: no tuning on test). Official results stay as run.
Run: .venv/Scripts/python -X utf8 scripts/posthoc_citation_parse.py test agent_dense_k3 agent_rerank_hybrid
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ID = re.compile(r"[0-9a-f]{16}")
BRACKET = re.compile(r"\[([^\]]*)\]")


def tolerant_ids(answer):
    ids = []
    for group in BRACKET.findall(answer):
        found = ID.findall(group)
        if found and all(ID.fullmatch(tok) or not re.search(r"[0-9a-f]{16}", tok) for tok in re.split(r"[\s,;|]+", group)):
            ids += found
    return list(dict.fromkeys(ids))


def main():
    split, cfgs = sys.argv[1], sys.argv[2:]
    lines = [f"# Hậu kiểm bộ đọc citation · {split} (KHÔNG dùng để thay kết quả chính thức)", "",
             "Lỗi được phát hiện khi đọc câu trả lời của test: model cite dạng `[id | id]` hoặc chép nguyên header "
             "`[id | blld-2012 | năm 2012 | trang … | Điều …]`. Bộ đọc của agent (commit 446525a) chỉ nhận `[id]` hoặc `[id, id]`, nên "
             "những câu này bị gán `no_citation`, tức là từ chối. Bảng dưới cho thấy câu nào sẽ đổi status nếu bộ đọc chấp nhận các dạng trên.", "",
             "| Config | Query | Answerable | Status chính thức | Status hậu kiểm | Citation hậu kiểm nằm trong context |", "|---|---|---|---|---|---|"]
    for cfg in cfgs:
        for t in json.loads((ROOT / "results" / "agent" / f"{cfg}_{split}" / "traces.json").read_text(encoding="utf-8")):
            if t["status"] == "error":
                continue
            ids = tolerant_ids(t["answer"])
            in_ctx = all(i in t["final_context_ids"] for i in ids)
            says_no = re.search(r"không\s+đủ\s+(bằng\s+chứng|thông\s+tin|căn\s+cứ)", t["answer"], re.I)
            status = "abstain" if (says_no or not ids or not in_ctx) else "answered"
            if status != t["status"]:
                lines.append(f"| {cfg} | {t['query_id']} | {t['answerable']} | {t['status']} ({t.get('abstain_reason')}) | {status} | "
                             f"{in_ctx} ({len(ids)} id) |")
    out = ROOT / "results" / "review" / f"posthoc_citation_parse_{split}.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
