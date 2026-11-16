# Đối chiếu hai lượt gán nhãn trên dev (2026-11-16)

**Nguồn gốc nhãn, cần ghi trung thực trong báo cáo:** cả hai lượt đều do AI thực hiện. Đây **không phải** nhãn của người chấm; các cột `human_*` trong `agent_review_dev.csv` để trống vì học viên chưa duyệt.

- **Lượt 1 (AI đọc):** Claude đọc 92 câu trả lời (4 config × 23 câu) và nguyên văn mọi đoạn được cite, chấm theo thang của BENCHMARK. Nhãn và lý do ở `ai_draft_labels_dev.py`.
- **Lượt 2 (kiểm tra tự động, phương pháp khác):** `scripts/second_pass_check.py` kiểm tra bằng luật văn bản:
  - câu trả lời có đủ con số của mệnh đề chính trong đáp án không;
  - có con số nào không nằm trong context không;
  - mỗi đoạn câu gắn `[id]` có trùng số Điều, đủ con số và trùng ≥ 50% từ với chunk được cite không;
  - câu thiếu bằng chứng có được từ chối và không đưa con số không.

## Diễn biến

| Bước | Số dòng mâu thuẫn | Nguyên nhân |
|---|---|---|
| Lượt 2, lần chạy đầu | 76/92 | Lỗi của bộ kiểm tra: mã chunk hex bị đọc thành con số; "số bắt buộc" lấy cả ý phụ ("60 tuổi năm 2035", "01 tháng"); câu nối ngắn bị tách khỏi ý chính. Đã sửa script. |
| Lượt 2 sau khi sửa | 5/92 | q08 × 3 config (citation), q09 × 2 config (số trông như con số, thực ra là mã chunk trong ngoặc gộp) |
| Đọc lại nguyên văn 5 dòng | phát hiện 2 lỗi thật | (1) **hybrid q08 tự mâu thuẫn**: đầu nói "không phải báo trước", cuối nói "vẫn phải tuân thủ thời hạn báo trước". Lượt 1 bỏ sót vì chỉ đọc 420 ký tự đầu. (2) **Lỗi đọc citation trong agent**: ngoặc gộp `[id1, id2]` không được nhận, nên citation trong đó không được đếm và không được kiểm tra có nằm trong context không. |
| Sửa lỗi đọc citation | — | `src/agent.py::parse_citations` nhận ngoặc gộp (có unittest). `scripts/reparse_citations.py` đọc lại trace đã lưu **mà không gọi lại LLM**; chỉ 1 dòng thay đổi: hybrid q08 từ 1 thành 3 citation, giá trị cũ giữ ở `citation_parse_v1`. |
| Sửa nhãn lượt 1 | 1 dòng | hybrid q08: citation thành `false;true;true` (Điều 35 part 1 gắn với kết luận sai ở câu cuối; Điều 39 và 40 đúng với mô tả); grade giữ 0. |
| Lượt 2, lần chạy cuối | **3/92** | Chỉ còn citation của q08 ở dense, I3, hybrid. |

## Phân xử 3 dòng còn lại: giữ nhãn lượt 1

Cả 3 dòng là phủ định hoặc lập luận sai, thứ mà bộ kiểm tra theo con số và mức trùng từ không phát hiện được:
- **dense / I3 q08** (câu trả lời giống hệt nhau):
  - "*Theo Điều 35 [Đ35 part 1], NLĐ chỉ được đơn phương chấm dứt HĐ khi có lý do tại Điều 35, 36, 37*": part 1 chỉ quy định thời hạn báo trước, không có câu này, nên **false**.
  - "*…coi là trái pháp luật theo Điều 39 […] và chịu nghĩa vụ theo Điều 40 […]*": khoản 2 Điều 35 lại cho phép nghỉ không cần báo trước khi bị trả lương không đúng hạn, nên áp Điều 39 và 40 vào trường hợp này là sai, **false; false**.
- **hybrid q08**: như đã phân tích ở bảng trên.

## Kết luận đối chiếu

- Sau khi sửa bộ kiểm tra và đọc lại, hai lượt **khớp nhau ở 89/92 dòng** về grade, citation và abstention. **Không có mâu thuẫn nào về grade.**
- 3 dòng còn lệch đều là citation của q08, đã phân xử như trên.
- Lượt 2 giúp tìm ra một câu trả lời tự mâu thuẫn mà lượt 1 bỏ sót, và một lỗi trong agent.
- **Giới hạn:** cả hai lượt đều là AI. Bộ kiểm tra tự động không hiểu phủ định, lập luận, hay ý không chứa con số. BENCHMARK yêu cầu người đọc citation để xác nhận; việc đó vẫn chưa được thực hiện.
