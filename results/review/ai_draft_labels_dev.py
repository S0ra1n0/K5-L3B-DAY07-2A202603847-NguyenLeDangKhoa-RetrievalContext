"""Claude's DRAFT labels for the dev agent runs (roadmap P5.5). Written after reading every answer and every
cited chunk on 2026-11-16. These fill the ai_* columns only; the student's human_* columns override them.

Default for answerable + answered: grade 2 and every citation supports its claim (checked by reading).
Default for unanswerable: abstention_correct = (status == abstain). Exceptions below carry their reason.
Run: .venv/Scripts/python -X utf8 results/review/ai_draft_labels_dev.py
"""
import csv
from pathlib import Path

SHEET = Path(__file__).with_name("agent_review_dev.csv")
D, H, I, R = "agent_dense_k3", "agent_hybrid_rrf", "agent_dense_inferred", "agent_rerank_hybrid"

OVERRIDE = {
    (D, "q05"): (0, "false", "", "Trả lời 'tối đa 18 tháng' là bịa: Điều 24/2019 không nêu thời gian thử việc; context không có Điều 25 (180 ngày). Citation [Đ24] chỉ hỗ trợ ý phụ 'HĐ dưới 01 tháng không thử việc', không hỗ trợ khẳng định chính."),
    (I, "q05"): (0, "false", "", "Giống agent_dense_k3: '18 tháng' không có căn cứ; Điều 25 không vào context."),
    (H, "q05"): (0, "false", "", "'12 tháng' và 'quản lý 18 tháng' đều bịa; Điều 24/2019 không chứa các con số này; thiếu Điều 25."),
    (D, "q07"): (2, "true;false", "", "Đáp án 45 ngày đúng và được Điều 35/2019 hỗ trợ. Citation thứ hai (Điều 40/2012 'Hủy bỏ việc đơn phương chấm dứt') KHÔNG chứa mức 45 ngày của bản 2012, nên sai."),
    (I, "q07"): (2, "true;false", "", "Giống agent_dense_k3: Điều 35/2019 đúng; Điều 40/2012 (hủy bỏ) không hỗ trợ ý '45 ngày theo 2012'."),
    (H, "q07"): (0, "false;false;false", "", "Trả lời '30 ngày' là sai (đúng là 45 ngày). Cả 3 citation (Điều 40/2012, Điều 38/2019 về hủy bỏ; Điều 43/2012 về nghĩa vụ khi chấm dứt trái luật) đều không chứa thời hạn báo trước."),
    (D, "q08"): (0, "false;false;false", "", "Kết luận ngược: nói trả lương không đúng hạn KHÔNG phải lý do chấm dứt không cần báo trước. Context thiếu khoản 2 Điều 35 (final_context_has_evidence=false). Câu 'chỉ được chấm dứt khi có lý do tại Điều 35, 36, 37' không có trong Điều 35 part 1; Điều 39, 40 không liên quan."),
    (I, "q08"): (0, "false;false;false", "", "Giống agent_dense_k3: kết luận sai, thiếu khoản 2 Điều 35 trong context."),
    (H, "q08"): (0, "false;true;true", "", "SỬA sau đối chiếu lượt 2: câu trả lời TỰ MÂU THUẪN. Câu đầu nói 'không phải báo trước', câu cuối nói 'vẫn phải tuân thủ thời hạn báo trước theo Điều 35'. Context thiếu khoản 2 Điều 35 (final_context_has_evidence=false). Citation Điều 35 part 1 bị gắn vào kết luận sai ở câu cuối nên false. Điều 39 và Điều 40 (ngoặc gộp, bị bỏ sót ở lần đọc citation đầu) đúng với mô tả 'đơn phương chấm dứt trái pháp luật / nghĩa vụ của NLĐ'."),
    (D, "u01"): ("", "true", "false", "Nội dung về bản chất là đúng (bộ luật không có con số), nhưng agent TRẢ LỜI có citation (status answered) thay vì từ chối theo quy ước, và thêm ý ngoài evidence ('Chính phủ ban hành trong các quyết định riêng'). Citation Điều 91 hỗ trợ ý 'xác lập theo vùng, ấn định theo tháng'."),
    (I, "u01"): ("", "true", "false", "Giống agent_dense_k3: không từ chối theo quy ước (status answered)."),
    (R, "u01"): ("", "true", "false", "Không từ chối theo quy ước (status answered); khuyên tra 'Quyết định của Thủ tướng' là ý ngoài corpus. Citation Điều 91 đúng với ý 'giao Chính phủ quy định chi tiết và công bố'."),
    (H, "u01"): ("", "", "true", "Từ chối đúng. Câu mở đầu nhắc Hội đồng tiền lương quốc gia/Chính phủ quy định, khớp Điều 91–92, không đưa con số. CẦN NGƯỜI DUYỆT xem phần giải thích có bị coi là khẳng định thêm không."),
}
UNANSWERABLE_NOTE = {
    "u02": "Từ chối đúng, không đưa tỷ lệ nào. Có thêm câu 'thường quy định trong Luật BHXH/văn bản hướng dẫn', ý này khớp với dẫn chiếu 'theo pháp luật về BHXH' trong bộ luật. CẦN NGƯỜI DUYỆT (quy tắc: không thêm khẳng định vô căn cứ).",
    "u03": "Từ chối đúng, không đưa con số phụ cấp. Câu giải thích (nếu có) chỉ nói bộ luật không quy định.",
}


def main():
    with open(SHEET, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        cols, rows = reader.fieldnames, list(reader)
    for r in rows:
        key = (r["config"], r["query_id"])
        n_cit = len([c for c in r["citations"].split(";") if c])
        answerable = r["answerable"] == "True"
        if key in OVERRIDE:
            grade, cit, abst, reason = OVERRIDE[key]
        elif answerable:
            grade, abst = (2, "") if r["status"] == "answered" else (0, "")
            cit = ";".join(["true"] * n_cit)
            reason = "Đúng và đủ ý được hỏi; đã đọc từng đoạn được cite, mỗi đoạn chứa khẳng định gắn với nó."
        else:
            grade, cit = "", ";".join(["true"] * n_cit)
            abst = "true" if r["status"] == "abstain" else "false"
            reason = UNANSWERABLE_NOTE.get(r["query_id"], "")
        r["ai_answer_grade"], r["ai_citation_support"], r["ai_abstention_correct"], r["ai_reason"] = str(grade), cit, abst, reason
    with open(SHEET, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)
    print(f"drafted {len(rows)} rows")


if __name__ == "__main__":
    main()
