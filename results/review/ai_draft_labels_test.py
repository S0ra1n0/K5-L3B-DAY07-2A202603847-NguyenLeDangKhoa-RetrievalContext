"""Claude's DRAFT labels for the TEST agent runs (P6.4), written after reading every answer and cited chunk on
2026-11-16. Official status/citations are the ones produced at run time (parser as committed in 446525a); the
pipe-citation parsing failure found on test is NOT fixed for these labels (see posthoc_citation_parse_test.md).
Fills ai_* columns only; human_* columns are left for the student.
Run: .venv/Scripts/python -X utf8 results/review/ai_draft_labels_test.py
"""
import csv
from pathlib import Path

SHEET = Path(__file__).with_name("agent_review_test.csv")
D, R = "agent_dense_k3", "agent_rerank_hybrid"

OVERRIDE = {
    (D, "t02"): (1, "true;true", "", "Kết luận 'không được' đúng và Điều 39/2012, Điều 37/2019 hỗ trợ, nhưng BỎ ngoại lệ 'trừ trường hợp điểm b khoản 1 Điều 38/36' có ngay trong đoạn được cite, nên chỉ đúng một phần. CẦN NGƯỜI DUYỆT (thiếu ngoại lệ là 1 hay 2)."),
    (R, "t02"): (1, "true;true", "", "Kết luận 'không được' đúng, có giải thích ngoại lệ 12/06 tháng (đúng nội dung điểm b khoản 1 Điều 38/2012, 36/2019). Nhưng khẳng định 'NSDLĐ CHỈ được đơn phương chấm dứt khi…' là sai (Điều 36 còn các căn cứ khác), và context thiếu Điều 37 (final_context_has_evidence=false). Citation đúng với phần nội dung 12/06 tháng. CẦN NGƯỜI DUYỆT."),
    (D, "t05"): (0, "", "", "Nội dung ĐÚNG ('ít nhất 24 giờ liên tục') nhưng model cite dạng [id | id]; bộ đọc citation không nhận nên status = abstain (no_citation). Theo BENCHMARK, từ chối câu có đáp án chấm 0. Lỗi định dạng citation phát hiện trên test, xem hậu kiểm."),
    (R, "t05"): (0, "", "", "Giống agent_dense_k3: nội dung đúng nhưng cite [id | id] nên bị chuyển thành từ chối; chấm 0."),
    (R, "t08"): (2, "true;true", "", "Đủ cả hai trường hợp của Điều 199. Ý thêm 'không được đình công trong thời gian Hội đồng trọng tài đang giải quyết' đúng với khoản 4 Điều 197 được cite."),
    (D, "t09"): ("", "true", "false", "Không đưa số ngày, nói rõ thời gian do pháp luật BHXH quy định, tức nội dung đúng là thiếu bằng chứng. Nhưng agent TRẢ LỜI có citation (status answered) thay vì từ chối theo quy ước, nên abstention = false. Citation Điều 139 part 2 (khoản 5) đúng."),
    (R, "t09"): ("", "true;false", "false", "Không đưa số ngày nhưng status answered, nên abstention = false. Citation Điều 157/2012 part 1 chỉ nói về lao động NỮ, không hỗ trợ ý 'lao động nam cũng được nghỉ khi vợ sinh con', nên false."),
    (D, "t10"): ("", "", "false", "Status abstain là do lỗi đọc citation dạng [id | blld-2012 | …], không phải agent từ chối. Nội dung trả lời SAI: đồng nhất trợ cấp thất nghiệp với trợ cấp mất việc làm và đưa ra '01 tháng/năm, ít nhất 02 tháng'. Đây là khẳng định vô căn cứ cho câu hỏi này, nên abstention = false."),
    (R, "t10"): ("", "true", "false", "Trả lời (status answered), đồng nhất trợ cấp thất nghiệp với trợ cấp mất việc làm (Điều 47), nên abstention = false. Citation Điều 47 đúng với ý 'tiền lương bình quân 06 tháng liền kề' của trợ cấp mất việc làm."),
    (R, "t11"): ("", "", "true", "Từ chối theo nội dung ('không có quy định… tối thiểu'), không đưa con số. Status abstain do không cite. Các mô tả Điều 98/2019, Điều 103 và Điều 113/2012 đúng với văn bản. CẦN NGƯỜI DUYỆT xem phần giải thích có bị coi là khẳng định thêm không."),
}


def main():
    with open(SHEET, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        cols, rows = reader.fieldnames, list(reader)
    for r in rows:
        key = (r["config"], r["query_id"])
        n_cit = len([c for c in r["citations"].split(";") if c])
        if key in OVERRIDE:
            grade, cit, abst, reason = OVERRIDE[key]
        elif r["answerable"] == "True":
            grade, abst = (2, "") if r["status"] == "answered" else (0, "")
            cit = ";".join(["true"] * n_cit)
            reason = "Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó."
        else:
            grade, cit = "", ";".join(["true"] * n_cit)
            abst = "true" if r["status"] == "abstain" else "false"
            reason = "Từ chối đúng câu chuẩn, không thêm khẳng định." if abst == "true" else ""
        r["ai_answer_grade"], r["ai_citation_support"], r["ai_abstention_correct"], r["ai_reason"] = str(grade), cit, abst, reason
    with open(SHEET, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)
    print(f"drafted {len(rows)} rows")


if __name__ == "__main__":
    main()
