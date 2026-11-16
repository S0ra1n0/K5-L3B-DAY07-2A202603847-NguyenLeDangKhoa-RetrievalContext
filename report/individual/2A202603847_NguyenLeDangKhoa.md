# Báo cáo Day 7: Agentic RAG

Học viên: Nguyễn Lê Đăng Khoa · MSSV 2A202603847 · Lớp L3B · Corpus: Bộ luật Lao động (BLLĐ) Việt Nam 2012 và 2019.

Các bảng số liệu sinh tự động bằng `scripts/build_report_tables.py` (bản đầy đủ ở [results/report_tables.md](../../results/report_tables.md)); không có số nào được điền tay.

## Dữ liệu và benchmark

- **Nguồn, quyền sử dụng, số trang và số chunk:**
  - Nguồn: Luật 10/2012/QH13 và Luật 45/2019/QH14. URL và sha256 của PDF ghi trong `data/day6/manifest.json`.
  - Quyền sử dụng: văn bản quy phạm pháp luật, không thuộc phạm vi bảo hộ quyền tác giả (khoản 2 Điều 15 Luật SHTT).
  - Quy mô: 151 trang OCR (68 + 83). Dùng chunk set B của Day 6: **552 chunk**, mỗi chunk là một Điều; Điều dài hơn 1.200 ký tự được tách theo khoản/điểm, mỗi part có `part/parts` và `pages`.
  - Dữ liệu copy từ repo Day 6 (commit `ac26168`) vào `data/day6/`, kèm SHA256SUMS.
- **Vector store, embedding model, phiên bản và số chiều:**
  - Store: PostgreSQL 16 + pgvector 0.8.7 (Docker, `127.0.0.1:55433`), exact cosine search, không dùng ANN.
  - Embedding: `intfloat/multilingual-e5-base` (revision `d1287505…`), 768 chiều, tiền tố `query:`/`passage:`, chạy local trên CPU.
  - `scripts/check_store.py` → `results/setup/store_check.json`: 552 dòng khớp ID local, self-retrieval 5/5, filter năm 2012/2019 đúng, latency trung vị 108 ms.
- **Agent model, cách chạy và phân chia dev/test:**
  - Model: Ollama local `qwen3.5:9b` (Q4_K_M) với `think=false`, `temperature=0`, `presence_penalty=0`, `repeat_penalty=1`.
  - Lý do đặt penalty = 0: với tham số mặc định (`presence_penalty 1.5`), model đọc context ghi "40 giờ" mà vẫn trả lời "35 giờ".
  - Chi phí API 0 USD. Lệnh chạy ở [README](../../README.md#bài-làm-agentic-rag-trên-bộ-luật-lao-động-2012-và-2019).
  - **Dev 23 câu** (20 có đáp án + 3 thiếu bằng chứng); **test 11 câu mới** (8 + 3). Benchmark đóng băng ở commit `bab4836` trước mọi lần chạy.
  - 5 câu test Day 6 (q16–q20) được **chuyển sang dev**, vì kết quả của chúng đã được xem ở Day 6 và một ý cải thiện đã lấy từ chúng.
- **Cách xác định câu có/thiếu evidence và tiêu chí chấm:**
  - Câu có đáp án: evidence copy nguyên văn từ text OCR. `scripts/verify_benchmark.py` xác nhận 53/53 quote nằm đúng trang gold và dev/test không chung Điều gold nào.
  - Chủ đề test do học viên chọn từ mục lục (Đ20, 37, 97, 99, 111, 115, 146, 199); câu hỏi do Claude soạn.
  - Câu thiếu bằng chứng (lương tối thiểu vùng I, tỷ lệ đóng BHXH, phụ cấp làm việc từ xa; nghỉ khi vợ sinh con, % trợ cấp thất nghiệp, thưởng Tết tối thiểu) được kiểm bằng grep **toàn bộ 151 trang** (`scripts/check_absence.py`), không dựa vào top-k.
  - Định nghĩa hit giống Day 6: chunk đúng nguồn, có trang gold trong `pages`, và chứa **đủ mọi** quote của một gold.
  - Tiêu chí chọn cấu hình được commit trước khi so sánh (`benchmark/selection_criteria.md`).

## Retrieval và thử nghiệm

| Cấu hình | Phương pháp, top-k, filter, rerank, context budget | Giả thuyết / thay đổi | Split | Hit@1 | Evidence Hit@3 | Context Evidence Rate | Thời gian / chi phí |
|---|---|---|---|---|---|---|---|
| Baseline (M1) `dense_k3` | Dense e5 + pgvector (Day 6 config C), top-3, filter năm của người dùng, 3000 ký tự | Baseline | dev | 16/20 (80%) | 20/20 (100%) | 20/20 (100%) | trung vị 63.0 ms/query · 0 USD |
| Phương pháp 2 (M2a) `bm25_syllable` | BM25 tách âm tiết, top-3, filter, 3000 ký tự | Từ khóa khớp tốt con số và thuật ngữ | dev | 17/20 (85%) | 20/20 (100%) | 20/20 (100%) | trung vị 2.6 ms/query · 0 USD |
| Phương pháp 2b (M2b) `bm25_pyvi` | BM25 tách từ pyvi, top-3, filter, 3000 ký tự | Tách từ ghép tiếng Việt giúp BM25 | dev | 18/20 (90%) | 20/20 (100%) | 20/20 (100%) | trung vị 2.3 ms/query · 0 USD |
| Phương pháp 3 (M3) `hybrid_rrf` | RRF(k=60) dense top-20 + BM25 top-20, top-3, filter, 3000 ký tự | Gộp hai tín hiệu bằng thứ hạng | dev | 19/20 (95%) | 20/20 (100%) | 20/20 (100%) | trung vị 66.6 ms/query · 0 USD |
| Cải thiện 1 (I1, M4) `rerank_hybrid` | Hybrid top-20 → bge-reranker-v2-m3 (CPU) → top-3, filter, 3000 ký tự | Cross-encoder phân biệt Điều kề nhau (lỗi q08) | dev | 20/20 (100%) | 20/20 (100%) | 20/20 (100%) | trung vị 10755.0 ms/query · 0 USD |
| Cải thiện 2 (I2) `rerank_hybrid_expand` | Như I1 + ghép các part cùng Điều, 4500 ký tự | Ghép part để đủ khoản/ngoại lệ | dev | 20/20 (100%) | 20/20 (100%) | 20/20 (100%) | trung vị 10954.0 ms/query · 0 USD |
| Chẩn đoán `dense_k3_nofilter` | Như baseline nhưng KHÔNG filter | Đo tác động của filter năm (lỗi q03, q16) | dev | 14/20 (70%) | 19/20 (95%) | 18/20 (90%) | trung vị 65.9 ms/query · 0 USD |
| Chẩn đoán `hybrid_rrf_nofilter` | Như M3, không filter |  | dev | 17/20 (85%) | 19/20 (95%) | 19/20 (95%) | trung vị 66.6 ms/query · 0 USD |
| Chẩn đoán `rerank_hybrid_nofilter` | Như I1, không filter |  | dev | 18/20 (90%) | 20/20 (100%) | 20/20 (100%) | trung vị 10623.5 ms/query · 0 USD |
| Cấu hình đã chọn `rerank_hybrid` | Như I1 | Chạy 1 lần sau khi chốt | test | 8/8 (100%) | 8/8 (100%) | 8/8 (100%) | trung vị 10673.3 ms/query · 0 USD |
| Baseline `dense_k3` | Như M1 | Chạy 1 lần sau khi chốt | test | 6/8 (75%) | 8/8 (100%) | 8/8 (100%) | trung vị 67.0 ms/query · 0 USD |

Bảng trên dùng query gốc, filter năm do người dùng cung cấp, và context là top-3 của một lượt tìm. Mọi dòng chạy trên cùng corpus, index, câu hỏi, nhãn và định nghĩa hit (`results/retrieval/comparison_dev.md`). Một cấu hình có thể vừa là phương pháp mới vừa là cải thiện: M4 rerank đồng thời là I1.

**Hai lỗi dev, nguyên nhân, cách thử** (chi tiết ở `results/retrieval/error_analysis_dev.md`):

1. **Nhầm phiên bản luật khi thiếu filter năm (q03, q16).**
   - Không có filter, dense xếp **Điều 106/2012 ("30 giờ")** trên gold Điều 107/2019 ("40 giờ") ở q03.
   - Ở q16, dense xếp **Điều 219/2019** (đoạn trích Luật BHXH) lên hạng 1, gold Điều 187/2012 chỉ ở hạng 3.
   - Nguyên nhân: hai bản luật gần như trùng chữ, chỉ khác con số; embedding và BM25 không phân biệt được năm.
   - Có filter thì cả hai câu lên hạng 1 (dense Hit@1: 14/20 → 16/20).
   - Thử **I3: agent tự suy năm** từ câu hỏi (`agent_dense_inferred`, bỏ qua filter benchmark). Model suy đúng năm ở **8/8** câu có năm; kết quả trùng baseline. Như vậy bỏ được filter nhập tay mà không mất chất lượng, nhưng không tăng điểm.
2. **Nhầm Điều kề nhau cùng từ vựng (q08, q07).**
   - Điều 36/2019 (quyền đơn phương chấm dứt của NSDLĐ, cũng có cụm "không cần báo trước") đứng trên gold Điều 35/2019 (quyền của NLĐ).
   - Nguyên nhân: bi-encoder và BM25 không phân biệt được chủ thể.
   - Thử **I1 rerank**: q08 lên hạng 1; Hit@1 dev 19/20 → 20/20. Đổi lại latency mỗi lượt tìm tăng từ 67 ms lên 10,8 s.
3. **I2 (ghép part cùng Điều): không cải thiện.** Context Evidence đã là 20/20 trước khi ghép; context tăng từ 2.362 lên 3.031 ký tự.

**Lý do chọn cấu hình** (`results/selection.json`, học viên xác nhận, commit `446525a` trước khi chạy test):
- Tiêu chí 1 là Context Evidence Rate của **context cuối gửi model** trong lượt chạy agent: rerank 20/20, dense 18/20, I3 18/20, hybrid 17/20. Chênh 2 câu, lớn hơn ngưỡng hòa 1 câu, nên chọn `agent_rerank_hybrid`. Tiêu chí này không phụ thuộc nhãn chấm tay.
- Nếu hiểu tiêu chí 1 là Context Evidence của retrieval với query gốc, cả 6 cấu hình đều 20/20; khi đó tiêu chí 2 (grounded 2,00 so với 1,80) cho cùng kết luận.

## Agent và đánh giá

- **Tool, số lượt gọi, điều kiện dừng, cách chọn context và xử lý lỗi:**
  - Tool duy nhất là `search_law(query, year?)` (`src/agent.py`).
  - Filter năm do người dùng cung cấp luôn được áp. Nếu không có, dùng `year` do model tự suy và ghi `filter_source: inferred`. Không bao giờ lấy từ gold: agent chỉ nhận `public_view()`, có unittest kiểm tra.
  - Mỗi lượt tìm lấy 3 chunk, tối đa 3 lượt. Context cộng dồn được dedup và giới hạn 3000 ký tự; chỉ context mới nhất được giữ trong hội thoại.
  - Dừng khi model trả lời. Hết lượt thì bỏ tool và bắt model trả lời hoặc từ chối.
  - Câu trả lời được tính là `answered` khi có ≥ 1 citation và mọi ID cite đều nằm trong context. Ngược lại là `abstain`, có ghi lý do.
  - Lỗi model hoặc store được ghi `status: error`, không thay bằng kết quả giả (0 lỗi trong mọi lượt chạy).
  - Prompt yêu cầu coi nội dung tài liệu là dữ liệu, không phải chỉ dẫn.

| Cấu hình / split | Tool use | Số lượt gọi | Grounded answer 0/1/2 và trung bình | Citation hợp lệ | Câu có citation | Abstention đúng | Từ chối nhầm | Context cuối đủ evidence | Thời gian trung vị · token vào/ra | Lỗi |
|---|---|---|---|---|---|---|---|---|---|---|
| agent_dense_k3 / dev | 23/23 (100%) | {'1': 23} | 2/0/18 · 1.80/2 | 27/32 (84%) | 21/21 (100%) | 2/3 (67%) | 0/20 (0%) | 18/20 (90%) | 4.12 s · 49988/3244 | 0 |
| agent_hybrid_rrf / dev | 23/23 (100%) | {'1': 23} | 3/0/17 · 1.70/2 | 27/32 (84%) | 20/20 (100%) | 3/3 (100%) | 0/20 (0%) | 17/20 (85%) | 5.76 s · 49904/3274 | 0 |
| agent_dense_inferred / dev | 23/23 (100%) | {'1': 23} | 2/0/18 · 1.80/2 | 27/32 (84%) | 21/21 (100%) | 2/3 (67%) | 0/20 (0%) | 18/20 (90%) | 7.21 s · 49988/3237 | 0 |
| agent_rerank_hybrid / dev | 23/23 (100%) | {'1': 23} | 0/0/20 · 2.00/2 | 31/31 (100%) | 21/21 (100%) | 2/3 (67%) | 0/20 (0%) | 20/20 (100%) | 15.26 s · 50610/3180 | 0 |
| agent_rerank_hybrid / test | 11/11 (100%) | {'1': 11} | 1/1/6 · 1.62/2 | 14/15 (93%) | 9/9 (100%) | 1/3 (33%) | 1/8 (12%) | 7/8 (88%) | 17.67 s · 25136/2178 | 0 |
| agent_dense_k3 / test | 11/11 (100%) | {'1': 11} | 1/1/6 · 1.62/2 | 11/11 (100%) | 8/8 (100%) | 1/3 (33%) | 1/8 (12%) | 8/8 (100%) | 4.17 s · 24502/1620 | 0 |

**Nguồn gốc nhãn (quan trọng):**
- Nhãn grounded, citation và abstention ở bảng trên do **AI chấm hai lượt bằng hai phương pháp**:
  - lượt 1: Claude đọc từng câu trả lời và nguyên văn mọi đoạn được cite;
  - lượt 2: `scripts/second_pass_check.py` kiểm tra bằng luật văn bản (con số bắt buộc, con số ngoài context, độ khớp của từng câu với đoạn được cite).
- Hai lượt khớp **89/92** dòng trên dev và **17/22** dòng trên test. Các dòng lệch được phân xử trong `results/review/conflict_resolution_{dev,test}.md`.
- **Học viên chưa duyệt từng dòng** (cột `human_*` để trống; cột "Human-reviewed rows" trong `results/agent/agent_table_*.md` là 0). Context 0/1/2 trên test (8 câu × 2 cấu hình) cũng do AI chấm: cả hai cấu hình đều 0/0/8 (`results/review/context_review_test.csv`).

| Query ID | Loại câu | Tool call và kết quả | Câu trả lời và citation | Nhãn, lý do |
|---|---|---|---|---|
| t01 (test, dense) | có đáp án, filter 2012 | `search_law(year=2012)`, top-1 Điều 22/2012 | "…từ đủ 12 tháng đến 36 tháng [a30b357d86050788]" | grade 2; citation đúng. Bản 2019 ghi "không quá 36 tháng", nên filter có tác dụng. |
| t11 (test, dense) | thiếu bằng chứng | 1 lượt tìm, không có Điều nào nêu mức thưởng | "Không đủ bằng chứng trong Bộ luật Lao động 2012/2019 để trả lời." | abstention đúng. |
| t05 (test, cả hai cấu hình) | có đáp án | top-2 là Điều 111/2019 và Điều 110/2012 (dense xếp 2019 lên đầu, rerank xếp 2012 lên đầu) | Nội dung đúng ("ít nhất 24 giờ liên tục") nhưng cite `[id \| id]`, bộ đọc citation không nhận, nên status = abstain | grade 0 (từ chối câu có đáp án). **Lỗi định dạng citation phát hiện trên test.** |
| q08 (dev, hybrid) | điều kiện/ngoại lệ, filter 2019 | context thiếu khoản 2 Điều 35 | Đầu nói "không phải báo trước", cuối nói "vẫn phải tuân thủ thời hạn báo trước" | grade 0; câu trả lời tự mâu thuẫn, do lượt 2 tìm ra. |
| q08 (dev, rerank) | như trên | top-1 Điều 35/2019 part 2 | "…không cần báo trước… trừ khoản 4 Điều 97 [ea3dc8618a0d48a9]" | grade 2; I1 sửa được lỗi 2. |

- **Đường dẫn trace, nhãn, lệnh chạy, thời gian và chi phí:**
  - Trace retrieval: `results/retrieval/<config>_<split>/traces.jsonl`.
  - Trace agent: `results/agent/<config>_<split>/traces.json` (gồm tool call, tham số, kết quả, context cuối, câu trả lời, citation, token, thời gian).
  - Nhãn: `results/review/`. Lệnh chạy: README.
  - Mọi cấu hình đều chi phí 0 USD (model local). Chạy agent trên dev mất khoảng 1,5–6 phút cho mỗi cấu hình.
- **Kết quả trước/sau, ví dụ lỗi, đánh đổi và giới hạn:**
  - **Lợi thế của rerank trên dev không lặp lại trên test.**
    - Trên test, rerank hơn ở Hit@1 retrieval (8/8 so với 6/8). Nhưng grounded bằng nhau (1,62), citation hợp lệ thấp hơn (14/15 so với 11/11), context cuối đủ evidence 7/8 (t02 thiếu Điều 37), và chậm hơn khoảng 4 lần (17,7 s so với 4,2 s mỗi câu).
    - Với 11 câu test, 1 câu tương đương 9–12,5 điểm %, nên không đủ để kết luận rerank tốt hơn ngoài corpus này.
    - Nếu triển khai thật, dense + filter năm là lựa chọn tốt hơn về chi phí và thời gian ở chất lượng tương đương. Rerank chỉ đáng dùng khi câu hỏi có Điều dễ nhầm như q08.
  - **Agent chỉ tìm 1 lượt** ở mọi câu (phân bố `{1: N}`), nên `max_searches = 3` không được dùng. Query do model tự viết làm mất evidence ở q05/q08 so với query gốc: Context Evidence của dense giảm từ 20/20 (retrieval) xuống 18/20 (agent).
  - **Lỗi đọc citation** gồm hai trường hợp:
    1. Trên dev, ngoặc gộp `[id1, id2]` bị bỏ qua. Đã sửa và đọc lại trace mà không gọi lại LLM; chỉ 1 dòng thay đổi.
    2. Trên test, dạng `[id | id]` hoặc header chép lại không được nhận: t05 đúng nhưng bị tính là từ chối nhầm ở cả hai cấu hình; t10 dense sai nhưng lại thành "từ chối".
    - Lỗi thứ hai lộ ra trên test nên **không sửa rồi chấm lại** (RULES). Ảnh hưởng ghi ở `results/review/posthoc_citation_parse_test.md`. Muốn có số liệu độc lập sau khi sửa thì cần một bộ test mới.
  - **Abstention yếu ở câu "gần chủ đề":**
    - u01, t09, t10 bị trả lời kèm citation thay vì từ chối theo quy ước. Nội dung u01/t09 thực chất là "luật không nêu con số", nhưng t10 đồng nhất trợ cấp thất nghiệp với trợ cấp mất việc làm.
    - Prompt "chỉ viết đúng một câu khi từ chối" không được model tuân thủ đầy đủ.
  - **Giới hạn khác:**
    - Nhãn do AI chấm, chưa có người duyệt.
    - Người soạn câu hỏi (Claude) cũng xây hệ thống; giảm thiên lệch bằng cách học viên chọn chủ đề test, đóng băng benchmark và khóa test bằng code.
    - Evidence giữ nguyên lỗi OCR. Bản 2019 là văn bản gốc, chưa gồm các lần sửa đổi về sau.
    - Thời gian đo trên một laptop (RTX 3070 cho LLM, CPU cho e5 và reranker).

## Thử thách nâng cao (nếu thực hiện)

Chưa thực hiện. Theo kế hoạch, phần này chỉ làm sau khi nộp phần cơ bản. Corpus luật hiện tại không có bảng, ảnh hay biểu đồ nên không đủ điều kiện.

## Công cụ AI đã dùng

Tôi dùng Claude Code (Claude Opus 5.5) để:
- lập roadmap;
- viết code (adapter Day 6, retrieval, context, agent, script đánh giá);
- soạn câu hỏi và evidence theo chủ đề tôi chọn;
- chạy thí nghiệm;
- chấm nháp nhãn hai lượt;
- soạn báo cáo này.

Cách kiểm tra:
- Evidence được script đối chiếu với trang nguồn (53/53).
- Câu thiếu bằng chứng được grep trên toàn corpus.
- 31 unittest offline.
- Rà soát sau khi nộp (2026-11-16):
  - Thêm giới hạn số lần gọi model cho vòng lặp agent, để chặn khả năng lặp vô hạn khi model cứ gửi tool call không hợp lệ. Mọi lượt chạy đã ghi đều dùng đúng 2 lần gọi, nên kết quả không đổi.
  - Thêm `scripts/load_vectors.py` để nạp lại pgvector mà không cần repo Day 6. Dry run: 552 vector khớp chunk, embed lại cho cosine bằng 1,0.
- Khóa quy trình chặn chạy khi benchmark chưa đóng băng và chặn chạy test trước khi chọn cấu hình.
- Mọi số trong báo cáo sinh từ file kết quả.
- Tôi duyệt câu t01 (và yêu cầu sửa `expected_answer`), chọn chủ đề test, xác nhận tiêu chí và cấu hình được chọn. Tôi **chưa** duyệt từng nhãn câu trả lời.
