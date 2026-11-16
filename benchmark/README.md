# Benchmark Day 7: Bộ luật Lao động 2012 và 2019

File chính: [questions.json](questions.json), sinh bằng `python -X utf8 scripts/build_benchmark.py` từ:
- [data/day6/day6_questions.json](../data/day6/day6_questions.json): 20 câu của Day 6, giữ nguyên nội dung;
- [day7_new_questions.json](day7_new_questions.json): 14 câu mới của Day 7.

Kiểm chứng bằng `python -X utf8 scripts/verify_benchmark.py`. Kết quả ghi vào `results/setup/benchmark_verification.json`.

## Thành phần

| Split | Có đáp án | Thiếu bằng chứng | ID |
|---|---:|---:|---|
| dev | 20 | 3 | q01–q20 (Day 6), u01–u03 (mới) |
| test | 8 | 3 | t01–t08 (có đáp án), t09–t11 (thiếu bằng chứng), đều mới |
| **Tổng** | **28** | **6** | 34 câu, vượt mức tối thiểu 24 câu (dev 15+2, test 5+2) |

Câu có filter `year`:
- dev 8 câu: q01–q04, q08, q16–q18;
- test 3 câu: t01 (2012), t04 (2019), t08 (2019).

Loại câu ở test: `metadata_filter` 3, `dieu_kien_ngoai_le` 1, `truc_tiep` 2, `dien_dat_lai` 2, `thieu_bang_chung` 3.

## Vì sao chia lại split so với Day 6

Test Day 6 (q16–q20) đã được chạy và xem kết quả. Ý tưởng cải thiện "loại phần trích Luật BHXH ở Điều 219" bắt nguồn từ lỗi của q16/q17. Vì vậy 5 câu này không còn là đánh giá độc lập (RUBRIC, RULES) và được **chuyển sang dev** (trường `origin: "day6-test"`).

**Test Day 7 là bộ mới.**
- Chủ đề do học viên chọn từ mục lục BLLĐ 2019 (Đ20, Đ37, Đ97, Đ99, Đ111, Đ115, Đ146, Đ199).
- Câu hỏi và evidence do Claude soạn từ `pages.jsonl`; học viên duyệt.
- Dev và test **không có chung Điều gold nào**; `verify_benchmark.py` kiểm tra điều này.
- Bộ câu hỏi được commit **trước** mọi lần chạy retrieval của Day 7.

## Schema

- **Câu có đáp án:** `id`, `split`, `type`, `origin`, `question`, `filter` (nếu có), `answerable: true`, `expected_answer`, `gold`.
  - `gold` là danh sách các **gold thay thế**; truy xuất đúng bất kỳ gold nào cũng tính là trúng.
  - Mỗi gold gồm `{source_id, page, article, evidence: [quote, …]}`. Trong một gold, **mọi** quote đều bắt buộc.
- **Câu thiếu bằng chứng:** `answerable: false`, `expected_behavior: "search_and_abstain"`, `absence_reason`, `absence_check.keywords`.
  - Sự vắng mặt được kiểm trên **toàn bộ 151 trang** bằng `scripts/check_absence.py` (kết quả ở `results/setup/absence_check.json`), rồi người duyệt đọc từng đoạn khớp.
  - Không kết luận thiếu bằng chứng chỉ vì top-k không tìm thấy.
- Evidence được copy **nguyên văn** từ text OCR đã làm sạch, kể cả lỗi OCR ("quyên", "tôi thiêu"), để so khớp tự động. `expected_answer` viết bằng tiếng Việt chuẩn.
- `filter.year` là input giả định do người dùng cung cấp: năm luôn được viết trong câu hỏi, không lấy từ gold.

## Định nghĩa dùng cho metric (`src/metrics.py`)

- **Hit:** một chunk trúng khi có đúng `source_id` của một gold, có trang gold nằm trong `pages` của chunk, và chứa **đủ mọi quote** của gold đó (so sánh sau khi gộp khoảng trắng). Định nghĩa này giống Day 6.
  - Hit@1 = số câu có chunk hạng 1 trúng / số câu có đáp án.
  - Evidence Hit@3 = số câu có ít nhất một chunk trúng trong top-3 / số câu có đáp án.
- **Context Evidence Rate:** với một gold, mọi quote phải xuất hiện trong context cuối gửi cho model, ở chunk cùng nguồn có chứa trang gold. Các quote được phép nằm ở các chunk khác nhau, ví dụ hai part của cùng một Điều.
- Câu thiếu bằng chứng **không** nằm trong mẫu số của các metric retrieval/context. Chúng được đánh giá bằng abstention.

## Tiêu chí chọn cấu hình

Xem [selection_criteria.md](selection_criteria.md). Tiêu chí được chốt trước khi chạy bất kỳ so sánh nào.

## Rủi ro và giới hạn

1. Người soạn câu (Claude) cũng là người xây hệ thống. Để giảm thiên lệch: học viên chọn chủ đề test, test được đóng băng trước khi chạy, và script test bị khóa cho đến khi có `results/selection.json`.
2. t02 và t03 cùng chủ đề hợp đồng/tiền lương với một số câu dev (q07–q08 về đơn phương chấm dứt; q08 dẫn chiếu Điều 97) nhưng khác Điều gold.
3. t04 nhắc "mức lương tối thiểu" (Đ99) và u01 (dev) hỏi số tiền lương tối thiểu vùng. Hai câu khác split và u01 không có đáp án, nên không lộ đáp án.
4. Bản 2019 là văn bản gốc, chưa gồm các lần sửa đổi về sau. Evidence giữ nguyên lỗi OCR.
5. Test chỉ có 11 câu: một câu chênh 9–12,5 điểm phần trăm. Không nên khái quát ra ngoài corpus này.
