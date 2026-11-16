# Đối chiếu hai lượt gán nhãn trên test (2026-11-16)

**Nguồn gốc nhãn:** lượt 1 là Claude đọc 22 câu trả lời (2 config × 11 câu) cùng mọi đoạn được cite; lượt 2 là `scripts/second_pass_check.py` (luật văn bản). Cả hai đều là AI. Các cột `human_*` để trống.

Hai lượt khác nhau ở **5/22** dòng:

| Config | Query | Khác ở | Phân xử | Lý do |
|---|---|---|---|---|
| dense | t02 | grade (1 so với 2) | **giữ 1, CẦN NGƯỜI DUYỆT** | Lượt 2 chỉ kiểm con số. Câu trả lời bỏ ngoại lệ "trừ điểm b khoản 1 Điều 36/38" có ngay trong đoạn được cite. Bỏ ngoại lệ là "đúng một phần" hay vẫn "đúng và đủ" là việc người chấm quyết định. |
| dense, rerank | t08 | citation Điều 199 | giữ `true` | Báo động giả: "khoản 2 Điều 188" là câu trích nằm trong chính Điều 199. |
| rerank | t06 | citation Điều 115 | giữ `true` | Báo động giả: model đặt `[id]` trước dòng mô tả, nên bộ kiểm tra ghép mã với dòng của bản 2012. |
| rerank | t09 | citation Điều 157/2012 | giữ `false` | Trùng từ cao, nhưng Điều 157/2012 part 1 chỉ nói về lao động **nữ**, không hỗ trợ ý "lao động nam được nghỉ khi vợ sinh con". |

## Lỗi phát hiện khi đọc test (không sửa vào kết quả chính thức)

Model đôi khi cite dạng `[id | id]` hoặc chép nguyên header của context. Bộ đọc citation không nhận các dạng này, nên câu trả lời bị gán `no_citation`, tức là từ chối.
- **t05:** câu trả lời **đúng** ("24 giờ liên tục") ở cả hai config nhưng bị tính là **từ chối nhầm**.
- **t10 (dense):** câu trả lời **sai** (đồng nhất trợ cấp thất nghiệp với trợ cấp mất việc làm) nhưng lại thành "từ chối" do lỗi định dạng.

Lỗi lộ ra trên test, nên theo RULES **không chỉnh hệ thống rồi chấm lại test**. Ảnh hưởng được ghi riêng ở `posthoc_citation_parse_test.md`. Muốn có con số độc lập sau khi sửa thì cần một bộ test mới.
