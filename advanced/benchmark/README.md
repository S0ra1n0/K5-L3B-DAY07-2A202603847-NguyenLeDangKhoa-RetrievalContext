# Benchmark nâng cao: *International Debt Report 2026*

**Trạng thái: BẢN NHÁP do AI soạn, chưa có người duyệt, chưa đóng băng.** Chưa chạy pipeline nào trên bộ câu hỏi này.

- `questions.json`: 48 câu.
  - **dev:** 15 câu có đáp án (mỗi nhóm 3) + 3 câu thiếu bằng chứng.
  - **test:** 24 câu có đáp án (bảng 6, ảnh/sơ đồ 5, biểu đồ 5, multi-hop 4, text 4) + 6 câu thiếu bằng chứng.
- `review_sheet.csv`: phiếu duyệt từng câu, mở bằng Excel. Cột `human_*` để trống cho bạn điền.
- Kiểm tra tự động: `.venv/Scripts/python -X utf8 advanced/scripts/check_benchmark.py`.

## Quy ước

- **Câu hỏi:** viết bằng tiếng Anh (ngôn ngữ của tài liệu), kèm bản dịch `question_vi`.
- **Trang:** `pdf_page` là số thứ tự trang trong file PDF; `printed_page` là số in trên trang. Ví dụ Table 1.1 nằm ở pdf 28, trang in 4.
- **Evidence:** mỗi evidence có `region` (id trong `data/processed/regions.json`), `bbox` (điểm PDF, gốc ở góc trên trái), `locator` (hàng/cột/ô hoặc vùng hình) và `quote_or_value`.
  - Giá trị có `~` hoặc `(visual` là số **đọc bằng mắt** từ biểu đồ không ghi số. Đáp án các câu này ghi "about" và chấm theo sai số hợp lý.
- **Câu thiếu bằng chứng:** có `absence_check`, gồm các mẫu regex đã chạy trên toàn bộ 280 trang và kết quả đọc từng chỗ khớp.
- **Không đưa đáp án hay evidence vào pipeline khi chạy.** Pipeline chỉ được đọc trường `question`.

## Kết quả kiểm tra tự động (lần chạy cuối: 0 lỗi)

- Đủ quota cho cả dev và test; mỗi câu chỉ thuộc một nhóm.
- **Evidence:** mọi trích dẫn text và ô bảng đều tìm thấy trong text layer đúng trang/vùng.
- **Cặp nhãn–số đọc từ hình:** 9 evidence có nhãn và số in tách rời trên sơ đồ khối của trang hồ sơ, nên cần đối chiếu cặp nhãn–số trên ảnh.
  - Claude đã đối chiếu trên ảnh trang: Ghana, Viet Nam, Sri Lanka, East Asia & Pacific, Fig 3B.1.
  - **Còn at10 (Kenya)** chưa đối chiếu ảnh. Cặp nhãn–số được suy từ thứ tự text layer, và tổng các ô khớp với tổng in trên trang.
- Không có evidence trùng giữa dev và test. Đã đổi ad14 vì từng trùng con số 8,2% với at19.

## Ghi chú về tài liệu gốc (đáp án đã tính đến)

- **Table 1.1** in sai dấu phân cách: `8.182.1` (năm 2020), `2.009.7`, `2.041.7`. Câu at05 kiểm tra đúng chỗ này; đáp án đúng là 8,182.1 tỷ USD.
- **Fig 3B.1** in "Granular **date** foundation" (lỗi in của bản gốc).
- **Đơn vị:** trang hồ sơ quốc gia tính bằng triệu USD, trang khu vực tính bằng tỷ USD. Câu ad06 và at11 kiểm tra điều kiện này.

## Cách duyệt (P8.4, 👤)

Mở `review_sheet.csv` và mở PDF (`data/raw/9781464823558.pdf`, nhảy đến trang theo số **pdf**). Với từng dòng:

1. **Câu có đáp án:** tìm evidence theo `evidence_locator` rồi kiểm tra ba điều.
   - Số và nhãn đúng như in.
   - Đáp án đủ ý, đúng đơn vị và điều kiện; phép tính đúng nếu có.
   - Câu hỏi chỉ có **một** cách hiểu.
   - Câu dựa trên biểu đồ (giá trị `~`): xem có đọc ra cùng kết luận không.
2. **Câu thiếu bằng chứng:** đọc phần `absence` và tự tìm thêm 1–2 từ khoá trong PDF (Ctrl+F). Nếu tìm thấy đáp án thì câu đó phải bỏ hoặc sửa.
3. Điền `human_ok` = y/n. Nếu n, ghi đề xuất sửa vào `human_fix_or_note`; Claude sẽ sửa `questions.json` và chạy lại kiểm tra.
4. Cần xem kỹ: **at10** (Kenya, chưa đối chiếu ảnh) và các câu biểu đồ đọc bằng mắt (ad08, ad09, ad12, at13, at15, at16).

Duyệt xong thì **đóng băng**: commit `questions.json` trước lần chạy pipeline đầu tiên. Sau mốc này không sửa test.
