# Phạm vi index: những gì đã xử lý, chưa xử lý và ảnh hưởng

Tài liệu: World Bank, *International Debt Report 2026*, 280 trang PDF (`data/source.json`). Mọi con số dưới đây được sinh từ các file trong `data/processed/` và `data/index/`, chạy lại được bằng `extract.py report`.

## 1. Đã index (526 chunk, chung một index)

| Nội dung | Trang PDF | Cách xử lý | Chunk |
|---|---|---|---:|
| Text thân bài, Key Takeaways, Box, phụ lục, tài liệu tham khảo, mục lục | 3–135, 267–277 | Text layer (pdfplumber), đã cắt bỏ phần nằm trong vùng hình/bảng | 351 |
| 44 hình có số (Fig 1.1–3.4, 3B.1; Fig 2.14 và 2.15 mỗi hình tách 2 trang) + sơ đồ "How to read" (p136) | 30–136 | Crop theo bbox; chữ in trong hình + mô tả bằng `qwen3.5:9b` | 46 |
| Table 1.1, 1.2 | 28, 63 | Tách theo toạ độ dòng; ô giữ như in + giá trị số | 2 |
| 127 trang hồ sơ (6 khu vực/tổng hợp + 121 quốc gia) | 137–263 | Phân tích bố cục: hình chữ nhật đã vẽ + màu chú giải + text | 127 |

Mỗi chunk giữ `page`, `page_label`, `kind`, `region` và `bbox` (điểm PDF, gốc ở góc trên trái). Crop sinh lại được bằng `extract.py render`.

## 2. Không index hoặc index không đầy đủ

| # | Phần | Lý do | Ảnh hưởng | Cách xử lý / giảm thiểu |
|---|---|---|---|---|
| 1 | 14 trang không có chunk: p1 (bìa), p2, 12, 16, 18, 22, 26, 106, 264, 266, 278, 279 (trang trắng), p25 "PART 1 Overview", p265 "APPENDIX" | Trang trắng, bìa hoặc trang ngăn phần; đã kiểm bằng tỉ lệ điểm ảnh có mực và xem ảnh | Không mất thông tin | Không cần |
| 2 | **Hình dạng đường** trong trang hồ sơ: Figure 1 (nợ 2015–25, chỉ in số năm đầu và cuối), Figure 3 (đường tỷ lệ so với dải phân vị 25–75) | Vision trên 127 trang quá chậm vì GPU giảm tốc do nhiệt (50–85 giây/trang); khi thử, vision còn nhận định sai vị trí so với dải (Viet Nam) | Không trả lời được câu về năm đỉnh, xu hướng giữa kỳ, hay "nằm trong/ngoài dải" nếu chỉ dùng index | Cấu hình `a3_hybrid_view`: agent gọi `view_page` để đọc ảnh trang khi cần. 36 trang đã có mô tả vision nằm trong `figures.jsonl` nhưng không dùng làm nguồn chính |
| 3 | 7 trang hồ sơ có ô không in số: Afghanistan, Algeria, Brazil, China, Iran, Tunisia, Türkiye | Ô quá nhỏ: bản gốc không in số, hoặc chú giải không đủ để ghép | Tổng các ô con nhỏ hơn ô cha; một số chủ nợ nhỏ thiếu giá trị | Ghi `issues` trong `profiles.jsonl`; thẻ index ghi rõ "some blocks too small to show a value"; đưa vào phiếu P8.3 |
| 4 | Figure 3 thiếu tỷ lệ ở 3 trang hồ sơ: Eritrea, Syrian Arab Republic, Turkmenistan | Bản gốc không in đủ 4 tỷ lệ (ký hiệu "..") | Câu hỏi về các tỷ lệ này phải được trả lời là không đủ bằng chứng | Không cần |
| 5 | Số đọc từ trục ở biểu đồ không ghi số | Vision chỉ ước lượng (`~`), lệch khoảng 10% so với hình | Không dùng làm đáp án chính xác | Benchmark chỉ hỏi số in sẵn, so sánh hoặc xu hướng; câu đọc bằng mắt ghi "about" |
| 6 | Mô tả vision bị cắt ở 13 vùng (dài hơn 1.800 ký tự): bảng 1.1, 1.2; Fig 1.3, 1.7, 1.9, 1.10, 1.15, 1.18, 1.19, 2.2, 2.4, 2.5, 2.14 (p98) | Biểu đồ phân tán hoặc nhiều chuỗi: model liệt kê từng điểm, có lần dài tới 11.000 ký tự | Phần cuối danh sách điểm không vào chunk; tiêu đề, trục, chú giải và xu hướng (phần đầu) vẫn còn | Với bảng: chunk dùng bảng tách từ text (đầy đủ), không dùng mô tả |
| 7 | Embedding bị cắt ở 39/526 chunk (37 hình, 2 bảng) dài hơn 512 token | Giới hạn của `multilingual-e5-base` | Dense chỉ "thấy" phần đầu chunk | BM25 trong hybrid dùng toàn văn; danh sách lưu trong `index/vectors.json` |
| 8 | 12/1.540 số trong mô tả vision không có trong text layer | Model tự sửa ô in sai (Table 1.1) hoặc thêm vạch chia trục không có trên hình (Fig 1.22, 2.1); Fig 2.13 có một số "18" chưa rõ | Có thể gây trả lời sai nếu agent tin mô tả hơn text | Chunk hình luôn kèm "Words printed in the figure" (text gốc); prompt yêu cầu dùng giá trị in sẵn; vùng bị đánh dấu nằm trong phiếu P8.3 |
| 9 | 3 lỗi in trong bản gốc (Table 1.1: `8.182.1`, `2.009.7`, `2.041.7`) và "Granular **date** foundation" (Fig 3B.1) | Lỗi của tài liệu | Có thể đọc sai giá trị | Giữ nguyên như in kèm cách đọc trong `tables/tab_1_1.json` → `issues`; benchmark at05 kiểm tra đúng chỗ này |
| 10 | Text bị lỗi định dạng ở tiêu đề chạy ("ANALysIs Of ExTERNAL DEBT") | Font small-caps trong text layer | Chỉ ở dòng tiêu đề chạy đầu trang | Không ảnh hưởng nội dung |

## 3. Kiểm tra với bản gốc

- **Tự động (AI):**
  - Bảng: 13/13 dòng × 11 năm khớp ảnh crop.
  - Hồ sơ: 120/127 trang có tổng các ô con khớp ô cha ở mọi nhóm.
  - Mô tả vision: 1.528/1.540 số khớp text layer.
  - Claude đã so ảnh trang: Viet Nam, Ghana, Kenya, Sri Lanka, East Asia & Pacific, Fig 1.1, 1.5, 1.6, 1.15, 2.7, 2.10, 2.15, 3.1, 3.2, 3B.1, Table 1.1, 1.2.
- **Người (P8.3):** `results/extraction_check.csv`, 32 dòng gồm toàn bộ vùng bị đánh dấu + mẫu ngẫu nhiên (seed 7). **Chưa điền.**
