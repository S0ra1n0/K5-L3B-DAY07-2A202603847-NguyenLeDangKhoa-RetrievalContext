# Thử thách nâng cao (+15đ): tài liệu ≥ 100 trang có bảng, ảnh, biểu đồ

Tách riêng khỏi phần cơ bản: phần này không sửa `benchmark/`, `results/` hay `data/day6/` của bài 85 điểm. Yêu cầu chi tiết ở [ADVANCED.md](../ADVANCED.md).

## Cấu trúc

```
advanced/
  data/
    raw/                 PDF gốc (bị Git bỏ qua; chỉ commit khi giấy phép cho phép chia sẻ)
    source.json          nguồn, phiên bản, giấy phép, sha256, số trang (sinh bởi scripts/intake.py)
    processed/
      pages/             text từng trang (text layer hoặc OCR), có số trang gốc
      tables/            bảng trích xuất (CSV/Markdown) + trang, vùng (bbox)
      figures/           ảnh crop của hình/biểu đồ + mô tả + trang, vùng (bbox)
  benchmark/             câu hỏi dev/test, đáp án, evidence theo trang/vùng
  configs/               cấu hình pipeline đã thử
  results/               trace, nhãn, metric theo nhóm
  scripts/               intake.py, rồi extract/index/eval
```

## Bước 1: đưa tài liệu vào

Chọn **một** tài liệu thực tế **≥ 100 trang**, có text, **bảng**, **ảnh/sơ đồ** và **biểu đồ** chứa thông tin hữu ích, ví dụ báo cáo thường niên, báo cáo nghiên cứu, niên giám thống kê. Người chấm phải truy cập được bản gốc.

Gửi cho Claude **link PDF** hoặc **đường dẫn file PDF** trên máy, kèm (nếu biết): tên tài liệu, đơn vị phát hành, năm/phiên bản, điều kiện sử dụng. Claude chạy:

```bash
.venv/Scripts/python -X utf8 advanced/scripts/intake.py --file "C:/duong/dan/bao-cao.pdf" --title "..." --publisher "..." --license "..." --version "..."
```

Hoặc với link (Claude hỏi xác nhận trước khi tải, nêu rõ tên file, nguồn và dung lượng):

```bash
.venv/Scripts/python -X utf8 advanced/scripts/intake.py --url "https://.../bao-cao.pdf" --title "..." --publisher "..." --license "..."
```

Kết quả là `advanced/data/source.json`, gồm:
- sha256, số trang, kiểm tra điều kiện ≥ 100 trang;
- số trang có text layer (trang scan sẽ cần OCR);
- số trang có ảnh nhúng.

Có bảng và biểu đồ thật hay không thì vẫn phải xác nhận bằng cách đọc tài liệu.

## Tài liệu đã chọn

World Bank, *International Debt Report 2026*: 280 trang, giấy phép CC BY 3.0 IGO, https://hdl.handle.net/10986/45762 (DOI 10.1596/978-1-4648-2355-8). sha256 ghi trong `data/source.json`. Người chấm tải bản gốc từ link này rồi đặt vào `data/raw/9781464823558.pdf`.

## Bước 2 (P8.2): trích xuất, đã chạy

Cài: `pdfplumber==0.11.10`, `pypdfium2==5.15.2` (có trong `requirements.txt`). Vision model chạy local: Ollama `qwen3.5:9b` (có vision), `think=false`, temperature 0, seed 7.

```bash
.venv/Scripts/python -X utf8 advanced/scripts/extract.py text      # pages.jsonl: text từng trang + số trang in
.venv/Scripts/python -X utf8 advanced/scripts/extract.py regions   # regions.json: vùng Figure/Table (caption..Source) + trang hồ sơ quốc gia, bbox
.venv/Scripts/python -X utf8 advanced/scripts/extract.py render    # ảnh trang + ảnh crop từng vùng (bị Git bỏ qua, sinh lại được)
.venv/Scripts/python -X utf8 advanced/scripts/extract.py tables    # tables/tab_1_1|tab_1_2 .csv/.md/.json
.venv/Scripts/python -X utf8 advanced/scripts/extract.py describe --kinds figure,table  # figures.jsonl: mô tả hình/bảng bằng vision model (khoảng 30 phút)
.venv/Scripts/python -X utf8 advanced/scripts/extract.py profiles  # profiles.jsonl: 127 trang hồ sơ, phân tích bố cục, không dùng model
.venv/Scripts/python -X utf8 advanced/scripts/extract.py report    # extraction_stats.json: thống kê + số model nêu mà không có trong text layer
.venv/Scripts/python -X utf8 advanced/scripts/check_sheet.py       # results/extraction_check.csv: phiếu đối chiếu cho người (P8.3)
```

**Cách xử lý từng loại nội dung:**
- **Text:** PDF có text layer (không cần OCR). 13 trang gần như không có chữ đều là trang trắng, bìa hoặc trang ngăn phần; đã kiểm tra bằng tỉ lệ điểm ảnh có mực và xem ảnh.
- **Bảng:** tách từ text layer theo toạ độ dòng. Giữ ô đúng như in (dấu trừ in là "–") kèm giá trị số; nhãn xuống hàng được ghép lại; cấp thụt lề cho biết thứ bậc dòng.
  - Bản gốc có 3 lỗi in dấu phân cách ở Table 1.1: `8.182.1`, `2.009.7`, `2.041.7`. Giữ nguyên như in, đọc là 8,182.1 / 2,009.7 / 2,041.7, và ghi vào `issues`.
- **Hình/biểu đồ:** biểu đồ là hình vector, nên render trang rồi crop theo bbox (từ caption đến hết khối Source/Note). Hình trải qua 2 trang được tách thành 2 vùng (`fig_2_14_p098`, `fig_2_14_p099`).
  - Vision model mô tả theo khung cố định: TITLE / TYPE / AXES / LEGEND / PRINTED_VALUES / READ_VALUES (~) / TRENDS.
  - Số ước lượng từ trục được đánh dấu `~`, sai số khoảng 10%, nên **không dùng làm đáp án chính xác**.
- **Hồ sơ quốc gia** (127 trang, mỗi trang 4 hình): **không** mô tả trước bằng vision model mà phân tích bố cục bằng `extract.py profiles`, ra `profiles.jsonl`.
  - **Lý do:** GPU laptop bị giảm tốc vì nhiệt (89–90°C, 210–405 MHz), mỗi trang mất 50–85 giây. Trong khi đó mọi con số đã in sẵn trong text layer; chỉ cặp nhãn–số của sơ đồ khối (Figure 2) là bị text layer xếp lẫn.
  - **Cách ghép cặp:** mỗi ô là một hình chữ nhật tô màu; chữ và số nằm trong ô nào thì thuộc ô đó. Ô hẹp không có nhãn thì ghép với ô vuông chú giải cùng màu.
  - **Kiểm tra tự động:** tổng các ô con phải bằng ô cha. **120/127 trang khớp ở mọi nhóm.** 7 trang lệch vì có ô quá nhỏ mà bản gốc không in số; các trang này được ghi `issues` và đưa vào phiếu P8.3.
  - Đã đối chiếu với ảnh trang cho Viet Nam, Ghana, Sri Lanka, East Asia & Pacific và Kenya.
  - Figure 3 (tỷ lệ năm 2025 và mức thay đổi) và Figure 4 (điều khoản vay) lấy từ text.
  - **Hình dạng đường** (xu hướng, vị trí so với dải phân vị) không có trong index. Khi cần, agent đọc ảnh trang lúc trả lời. Lần thử cho thấy vision model nhận định vị trí so với dải không đáng tin (trang Viet Nam bị nói sai).
  - 36 trang hồ sơ đã được mô tả bằng vision trước khi đổi cách; các mô tả này vẫn nằm trong `figures.jsonl` nhưng không dùng làm nguồn chính.

**Kiểm tra tự động mô tả vision** (`report`, 84 vùng): 1.528/1.540 số model nêu là "in trên hình" có trong text layer (99,2%). 12 số không khớp nằm ở 4 vùng:
- **Bảng 1.1:** model tự sửa các ô in sai, ví dụ ghi 8182.1.
- **Fig 1.22 và 2.1:** model thêm vạch chia trục không có trên hình.
- **Fig 2.13:** một số "18" cần người kiểm.

## Các bước tiếp theo (theo roadmap P8)

1. **P8.2: trích xuất.** Đã làm, xem mục trên.
2. **P8.3:** đối chiếu mẫu nội dung trích xuất với bản gốc.
3. **P8.4: benchmark.**
   - Dev ≥ 15 câu có đáp án + 3 câu thiếu bằng chứng.
   - Test ≥ 24 câu có đáp án + 6 câu thiếu bằng chứng, với tối thiểu: bảng 6, ảnh/sơ đồ 5, biểu đồ 5, multi-hop 4, text 4.
   - Chia split và **đóng băng trước khi thử nghiệm**.
4. **P8.5:** index đa phương thức, agent dùng lại khung của phần cơ bản; chọn cấu hình trên dev.
5. **P8.6:** chạy test một lần. Chấm **từng câu** đạt/không đạt, đối chiếu bản gốc. Cần **≥ 27/30 (90%)**, không làm tròn; lỗi hệ thống và timeout tính là không đạt.
6. **P8.7:** báo cáo theo nhóm, chi phí, giới hạn, cách tái lập.

## Lưu ý quyền sử dụng

Ghi rõ nguồn và điều kiện sử dụng trong `source.json`. Nếu giấy phép không cho phép chia sẻ lại, **không commit PDF**. Khi đó chỉ commit link gốc và sha256 để người chấm tự tải và đối chiếu.

## Bước 5 (P8.5): index đa phương thức và agent (code xong, chưa chạy benchmark)

**Index** (`advanced/rag/chunks.py` → `data/index/chunks.jsonl`): **526 chunk** trong một index chung. Mỗi chunk giữ `page`, `page_label`, `kind`, `region` và `bbox`.

| Loại | Số chunk | Nội dung |
|---|---:|---|
| text | 351 | Chữ của trang đã cắt bỏ mọi vùng hình/bảng; gộp theo đoạn, tối đa 1.200 ký tự |
| figure | 46 | Tiêu đề + chữ in trong hình (nhãn, số, vạch trục) + mô tả của vision model (ghi rõ là model sinh ra) |
| table | 2 | Bảng Markdown, ô giữ đúng như in, kèm ghi chú lỗi in |
| profile | 127 | Thẻ dữ liệu từ `profiles.jsonl` (Figure 2–4) |

**Retrieval** (`advanced/rag/retrieval.py`):
- **dense:** e5 chạy trong bộ nhớ, vector lưu cache.
- **BM25, hybrid RRF và rerank** (bge-reranker-v2-m3): dùng lại lớp của phần cơ bản.

**Agent** (`advanced/rag/agent.py`):
- Công cụ `search_report`; tuỳ chọn thêm `view_page`, cho vision model đọc ảnh một trang **mà search đã trả về** rồi đưa kết quả vào context dưới dạng block `pNNN-page` có thể trích dẫn.
- Trích dẫn ghi theo id chunk. Trace lưu `cited_regions` (trang PDF, trang in, region, bbox) để người chấm tìm lại đúng vùng.
- Quy tắc trả lời và từ chối giống phần cơ bản: trích dẫn id nằm ngoài context thì tính là từ chối.

**Cấu hình** (`advanced/configs/`): `a0_dense`, `a1_hybrid`, `a2_rerank`, `a3_hybrid_view`.

```bash
.venv/Scripts/python -X utf8 advanced/scripts/run_bench.py --config advanced/configs/a1_hybrid.json --split dev
```

**Chốt chặn:**
- `questions.json` phải đã commit và không có thay đổi chưa commit.
- Test bị khoá cho tới khi có `results/selection.json`.
- Mỗi cấu hình chỉ chạy test một lần.

**Đã chạy thử** (chỉ với câu hỏi **ngoài** benchmark): Ukraine (+29,2%, 250,3 tỷ USD) đúng; Bangladesh 113.438 triệu USD đúng; câu về dự báo GDP Brazil 2027 thì từ chối đúng.

**Vấn đề đã thấy:** với câu khó (so sánh hai số âm), model "nghĩ thành tiếng" dài, và câu đầu mâu thuẫn với kết luận. Cần xem lỗi này phổ biến đến đâu trên dev.

## Phạm vi index và kiểm thử

- **Những gì đã và chưa index**, lý do và ảnh hưởng tới câu hỏi: [results/index_coverage.md](results/index_coverage.md).
- **Unit test offline** (`tests/test_advanced.py`, 17 test, không cần model): tách số (lỗi in, dấu trừ "–"), dòng bảng, ghép ô sơ đồ hồ sơ theo hình chữ nhật và màu chú giải, nối gạch nối, đọc trích dẫn, ngân sách context, vòng agent với model giả, và các chốt chặn của `run_bench`.
  - Chạy: `.venv/Scripts/python -X utf8 -m unittest discover -s tests -v`.
