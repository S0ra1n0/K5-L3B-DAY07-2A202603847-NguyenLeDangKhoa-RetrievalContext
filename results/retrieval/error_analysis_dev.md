# Phân tích lỗi retrieval trên dev (nháp của Claude, chờ học viên xác nhận theo roadmap H5)

Nguồn số liệu: `comparison_dev.md` (có filter `year` do người dùng cung cấp) và `comparison_dev_nofilter.md` (chẩn đoán: bỏ filter, tương ứng người dùng không nêu năm hoặc hệ thống bỏ qua năm). Benchmark commit `bab4836`. Trace của từng câu nằm ở `results/retrieval/<config>_dev/traces.jsonl`.

## Quan sát chung

- **Khi có filter, dev chạm trần ở top-3.** Cả 6 cấu hình đều đạt Evidence Hit@3 = Context Evidence Rate = 20/20. Khác biệt chỉ còn ở Hit@1: dense 16, BM25 âm tiết 17, BM25 pyvi 18, hybrid 19, rerank 20.
  - Ý nghĩa: với context top-3, cả 6 cấu hình đều đưa đủ evidence cho model. Chất lượng câu trả lời sẽ do agent quyết định (P5.4).
  - Tiêu chí 1 (Context Evidence Rate) và 5 (Hit@3) đã đăng ký trước sẽ hòa nhau; việc chọn chuyển sang các tiêu chí 2–4 (nhãn câu trả lời) và 6 (latency).
- **Bỏ filter thì lỗi xuất hiện.**
  - dense: Hit@1 14/20, Hit@3 19/20, Context Evidence 18/20.
  - hybrid: 17/20, 19/20, 19/20.
  - rerank: 18/20, 20/20, 20/20.
- **Latency:** BM25 khoảng 2–3 ms, dense và hybrid khoảng 65 ms, rerank khoảng 10,7 giây (CPU, 20 candidate), tức chậm hơn khoảng 160 lần.

## Lỗi 1: nhầm phiên bản luật khi không có filter năm (q03, q16)

| | |
|---|---|
| Triệu chứng | **q03** ("Theo BLLĐ **2019**… giờ làm thêm tối đa/tháng"): không có filter, dense và hybrid đều xếp **Điều 106 bản 2012** ("30 giờ") lên hạng 1, gold Điều 107/2019 ("40 giờ") đứng hạng 2. **q16** ("Theo BLLĐ **2012**… tuổi hưởng lương hưu"): dense xếp **Điều 219 bản 2019** (part 6/10, trích nguyên văn Luật BHXH) lên hạng 1, gold Điều 187/2012 ở hạng 3; hybrid đẩy gold xuống hạng 6. |
| Tầng lỗi | Retrieval. Hai bản luật có nội dung gần như trùng chữ, chỉ khác con số; embedding và BM25 không phân biệt được năm. |
| Hậu quả | Model nhận chunk sai năm ở hạng 1 và dễ trả lời sai con số (30 thay vì 40 giờ). Đây là lỗi nguy hiểm nhất của corpus này. |
| Giả thuyết | Áp filter `year` lấy từ chính câu hỏi (người dùng đã ghi năm) sẽ loại chunk sai năm. Có filter thì q03 và q16 đều lên hạng 1 ở mọi cấu hình (bảng có filter). |
| Thay đổi thử | **I3: agent tự suy năm** từ câu hỏi qua tham số `year` của tool `search_law`, ghi `filter_source: inferred`. Đo trên dev bằng cấu hình agent **bỏ qua filter của benchmark**, để xem model tự suy năm có tốt bằng filter người dùng đưa vào không. |
| Trước → sau | Retrieval: không filter 14/20 → có filter 16/20 (Hit@1, dense). Agent (`agent_dense_inferred`): model tự suy **đúng năm ở 8/8** câu có năm, kết quả giống hệt baseline (Context Evidence 18/20, grounded 1,80). Như vậy bỏ được filter nhập tay mà không mất chất lượng, nhưng không tăng điểm. Model cũng tự gán `year=2019` cho u01 (câu không nêu năm). |

## Lỗi 2: nhầm Điều kề nhau có cùng chủ đề (q08, q07; câu cần nhiều đoạn evidence)

| | |
|---|---|
| Triệu chứng | **q08** (NLĐ đơn phương chấm dứt HĐ **không cần báo trước** khi bị trả lương không đúng hạn; gold Điều 35/2019 cần **2 quote**). Có filter: dense, BM25 và hybrid đều xếp **Điều 36/2019 part 3/3** (quyền đơn phương chấm dứt của **NSDLĐ**, cũng có cụm "không cần báo trước") lên hạng 1; gold ở hạng 2. Không filter: dense đẩy gold xuống hạng 4, ra khỏi context top-3. **q07** cũng có top-1 là Điều 36 khi dùng dense. |
| Tầng lỗi | Retrieval/xếp hạng. Hai Điều kề nhau dùng gần như cùng từ vựng ("đơn phương chấm dứt", "báo trước"); chỉ khác chủ thể (người lao động hay người sử dụng lao động). Bi-encoder và BM25 không bắt được khác biệt này. |
| Giả thuyết | Cross-encoder đọc cùng lúc cặp (câu hỏi, đoạn) nên phân biệt được chủ thể, và sẽ đưa đúng Điều lên hạng 1. |
| Thay đổi thử | **I1: rerank** top-20 của hybrid bằng bge-reranker-v2-m3. |
| Trước → sau | q08 có filter: hạng 2 → **1**; không filter: dense 4, hybrid 2 → rerank **1**. Hit@1 dev có filter: hybrid 19/20 → rerank 20/20. **Đánh đổi:** latency 67 ms → 10,8 s mỗi lần tìm. |

## Cải thiện I2 (ghép các part cùng Điều): không đo được khác biệt ở retrieval

`rerank_hybrid_expand` thêm các part còn lại của cùng Điều vào context (budget 4.500 ký tự). Context trung bình tăng từ 2.362 lên 3.031 ký tự, nhưng Context Evidence Rate đã là 20/20 trước khi ghép, nên **không cải thiện được trên dev**. Ghi nhận đây là kết quả không cải thiện. Giá trị của I2, nếu có, chỉ thấy được ở câu trả lời của agent: có thêm khoản/ngoại lệ ở part khác.

## Rủi ro rút ra

- q04 không filter: rerank đẩy gold (2012) xuống hạng 2, dưới Điều 107/2019. Rerank cũng không phân biệt được năm, nên **filter năm vẫn cần thiết** ngay cả khi có rerank.
- Dev có 20 câu; một câu tương đương 5 điểm %. Các khác biệt Hit@1 1–2 câu nằm trong vùng nhiễu.
