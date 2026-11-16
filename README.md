# Day 7 — Agentic RAG

**Bài cá nhân · Python 3.11+ · tiếp nối Day 6**

## Bài làm: Agentic RAG trên Bộ luật Lao động 2012 và 2019

Học viên Nguyễn Lê Đăng Khoa · MSSV 2A202603847 · Lớp L3B. Báo cáo: [report/individual/2A202603847_NguyenLeDangKhoa.md](report/individual/2A202603847_NguyenLeDangKhoa.md).

### Thành phần

| Phần | Nội dung | File |
|---|---|---|
| Dữ liệu Day 6 | 552 chunk theo Điều (chunk set B), vector e5-base 768 chiều, 151 trang OCR, manifest | `data/day6/` (README + SHA256SUMS) |
| Vector store | PostgreSQL 16 + pgvector 0.8.7 (Docker), exact cosine; code copy từ Day 6 | `docker-compose.yml`, `src/day6/` |
| Retrieval | M1 dense, M2 BM25 (tách âm tiết / pyvi), M3 hybrid RRF, M4 rerank (bge-reranker-v2-m3) | `src/retrievers.py`, `configs/*.json` |
| Context | dedup, ghép part cùng Điều, đóng gói theo budget ký tự, header id/năm/trang/Điều | `src/context.py` |
| Agent | Ollama local `qwen3.5:9b`, tool `search_law(query, year?)`, citation `[chunk-id]`, từ chối khi thiếu bằng chứng | `src/llm.py`, `src/agent.py` |
| Benchmark | 34 câu: dev 20 + 3, test 8 + 3 (mới), đóng băng ở commit `bab4836` | `benchmark/` |
| Kết quả | trace, summary, nhãn, bảng so sánh, lựa chọn cấu hình | `results/` |

### Cách chạy lại (Windows, Python 3.12, từ thư mục gốc repo)

Cần có Docker Desktop và Ollama với model `qwen3.5:9b` (`ollama pull qwen3.5:9b`). Không cần API key; chi phí API 0 USD.

```bash
python -m venv .venv
.venv/Scripts/python -m pip install torch==2.7.1 --index-url https://download.pytorch.org/whl/cpu
.venv/Scripts/python -m pip install -r requirements.txt
copy .env.example .env
docker compose -p day6_student_starter up -d --wait
```

- Volume pgvector của Day 6 được dùng lại. Nếu tạo DB mới, nạp 552 vector từ `data/day6/vectors_B.npz` bằng `scripts/ingest_store.py` của repo Day 6. Không cần embed lại.
- Lần chạy đầu, `intfloat/multilingual-e5-base` và `BAAI/bge-reranker-v2-m3` được tải tự động từ HuggingFace.

```bash
.venv/Scripts/python -X utf8 -m unittest discover -s tests -v          # 30 test offline (mock)
.venv/Scripts/python -X utf8 scripts/check_store.py                    # kiểm tra store: 552 dòng, self-retrieval, filter
.venv/Scripts/python -X utf8 scripts/build_benchmark.py                # sinh benchmark/questions.json
.venv/Scripts/python -X utf8 scripts/verify_benchmark.py               # 53/53 quote đúng trang, dev/test không trùng Điều
.venv/Scripts/python -X utf8 scripts/check_absence.py                  # grep toàn corpus cho 6 câu thiếu bằng chứng
.venv/Scripts/python -X utf8 scripts/eval_retrieval.py --split dev configs/dense_k3.json configs/bm25_syllable.json configs/bm25_pyvi.json configs/hybrid_rrf.json configs/rerank_hybrid.json configs/rerank_hybrid_expand.json
.venv/Scripts/python -X utf8 scripts/run_agent_bench.py --split dev configs/agent_dense_k3.json configs/agent_hybrid_rrf.json configs/agent_dense_inferred.json configs/agent_rerank_hybrid.json
.venv/Scripts/python -X utf8 scripts/make_review_sheet.py dev agent_dense_k3 agent_hybrid_rrf agent_dense_inferred agent_rerank_hybrid
.venv/Scripts/python -X utf8 scripts/aggregate_agent.py dev agent_dense_k3 agent_hybrid_rrf agent_dense_inferred agent_rerank_hybrid
# test: chỉ chạy được khi có results/selection.json, và chỉ chạy một lần
.venv/Scripts/python -X utf8 scripts/eval_retrieval.py --split test configs/dense_k3.json configs/rerank_hybrid.json
.venv/Scripts/python -X utf8 scripts/run_agent_bench.py --split test configs/agent_dense_k3.json configs/agent_rerank_hybrid.json
.venv/Scripts/python -X utf8 scripts/build_report_tables.py            # bảng số liệu của báo cáo
```

Khóa quy trình (`src/guards.py`): các script chạy benchmark sẽ từ chối chạy nếu `benchmark/questions.json` chưa commit hoặc đang bị sửa. Split test bị khóa cho tới khi có `results/selection.json` và không cho chạy lại.

---

Dùng embedding và vector store từ Day 6 để xây một agent biết tìm bằng chứng, trả lời có nguồn và nhận biết khi không đủ thông tin. Bạn tự chọn kiến trúc, số tool và cách tổ chức retrieval.

> **Tùy chọn:** [Gợi ý dùng AI để lập trình](AGENT_SETUP.md) giúp bạn làm lab; phần này không bắt buộc và không tính điểm.

## Bài cần làm

![Agent tìm tài liệu trong kho Day 6 và trả lời có nguồn](assets/retrieval-pipeline.svg)

1. Kết nối dữ liệu, embedding và vector store Day 6.
2. Xây agent dùng model thật và ít nhất một khả năng truy xuất dữ liệu. Agent có thể dùng nhiều tool và nhiều lượt gọi.
3. Thử **ít nhất 3 phương pháp retrieval khác nhau**, trong đó có dense retrieval dùng vector store Day 6. Tự chọn các phương pháp còn lại; xem [gợi ý](GUIDE.md#2-thử-các-phương-pháp-retrieval).
4. Thử nhiều cấu hình, benchmark, phân tích lỗi và chọn cấu hình tốt trên **dev**; sau đó đánh giá trên **test**.

Benchmark tối thiểu có **24 câu**: dev gồm 15 câu có đáp án và 2 câu thiếu bằng chứng; test gồm 5 câu có đáp án và 2 câu thiếu bằng chứng. Xem [benchmark](BENCHMARK.md) và [rubric](RUBRIC.md).

## Thử thách nâng cao · +15 điểm

Index một tài liệu thực tế từ **100 trang** có bảng, ảnh và biểu đồ; xây agent truy xuất và trả lời các câu hỏi về nội dung đó. Hoàn thành [thử thách nâng cao](ADVANCED.md) và đạt **ít nhất 90% benchmark test** để nhận 15 điểm bonus. Phần cơ bản tối đa 85 điểm; toàn bài tối đa 100 điểm.

## Bắt đầu

1. Đọc [hướng dẫn](GUIDE.md), [rubric](RUBRIC.md) và [quy tắc](RULES.md).
2. Tạo repo cá nhân theo [cách nộp bài](SUBMISSION.md), chuẩn bị đầu ra Day 6 và model hỗ trợ tool calling.
3. Dùng hoặc thay thế [starter](starter/README.md); bạn cần kết nối model và vector store thật.
4. Chạy `python -m unittest discover -s tests -v`. Test mock chỉ kiểm tra code, không phải benchmark agent thật.

![Các bước thử nghiệm trên dev và đánh giá trên test](assets/experiment-loop.svg)

Nộp code, cách chạy, cấu hình, benchmark, trace và [báo cáo](report/individual/MSSV_HoTen.md). Thời gian ở [checkpoints](CHECKPOINTS.md) là gợi ý, có thể điều chỉnh theo lớp và phạm vi thử nghiệm.
