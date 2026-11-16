# Dữ liệu từ Day 6

Các file được copy từ repo Day 6 (`K5-L3B-DAY06-NguyenLeDangKhoa-2A202603847-DataIngestion`, commit `ac26168`). Mục đích là để repo Day 7 chạy được mà không cần repo Day 6 và không phải OCR lại. Checksum nằm trong [SHA256SUMS](SHA256SUMS).

| File | Nguồn Day 6 | Nội dung |
|---|---|---|
| `chunks_B.jsonl` | `starter/data/chunks/B.jsonl` | 552 chunk, mỗi chunk là một Điều; Điều dài hơn 1.200 ký tự được tách theo khoản/điểm, có `part/parts`, `pages`, `year`, `article` |
| `vectors_B.npz` | `starter/data/vectors/B.npz` | Vector `intfloat/multilingual-e5-base` (768 chiều, chuẩn hóa, tiền tố `passage:`) của 552 chunk; dùng để nạp lại pgvector mà không phải embed lại |
| `pages.jsonl` | `starter/data/processed/pages.jsonl` | 151 trang text OCR đã làm sạch; dùng để kiểm evidence và kiểm câu thiếu bằng chứng |
| `manifest.json` | `starter/data/manifest.json` | Nguồn, URL, sha256 của 2 PDF, số hiệu và ngày hiệu lực |
| `day6_questions.json` | `benchmark/questions.json` | 20 câu benchmark gốc của Day 6 |

**Quyền sử dụng:** BLLĐ 10/2012/QH13 và 45/2019/QH14 là văn bản quy phạm pháp luật, không thuộc phạm vi bảo hộ quyền tác giả (khoản 2 Điều 15 Luật Sở hữu trí tuệ). Nguồn PDF ghi trong `manifest.json`.
