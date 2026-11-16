# Bảng số liệu cho báo cáo (sinh tự động bằng scripts/build_report_tables.py)

## Retrieval và context

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

## Agent

| Cấu hình / split | Tool use | Số lượt gọi | Grounded answer 0/1/2 và trung bình | Citation hợp lệ | Câu có citation | Abstention đúng | Từ chối nhầm | Context cuối đủ evidence | Thời gian trung vị · token vào/ra | Lỗi |
|---|---|---|---|---|---|---|---|---|---|---|
| agent_dense_k3 / dev | 23/23 (100%) | {'1': 23} | 2/0/18 · 1.80/2 | 27/32 (84%) | 21/21 (100%) | 2/3 (67%) | 0/20 (0%) | 18/20 (90%) | 4.12 s · 49988/3244 | 0 |
| agent_hybrid_rrf / dev | 23/23 (100%) | {'1': 23} | 3/0/17 · 1.70/2 | 27/32 (84%) | 20/20 (100%) | 3/3 (100%) | 0/20 (0%) | 17/20 (85%) | 5.76 s · 49904/3274 | 0 |
| agent_dense_inferred / dev | 23/23 (100%) | {'1': 23} | 2/0/18 · 1.80/2 | 27/32 (84%) | 21/21 (100%) | 2/3 (67%) | 0/20 (0%) | 18/20 (90%) | 7.21 s · 49988/3237 | 0 |
| agent_rerank_hybrid / dev | 23/23 (100%) | {'1': 23} | 0/0/20 · 2.00/2 | 31/31 (100%) | 21/21 (100%) | 2/3 (67%) | 0/20 (0%) | 20/20 (100%) | 15.26 s · 50610/3180 | 0 |
| agent_rerank_hybrid / test | 11/11 (100%) | {'1': 11} | 1/1/6 · 1.62/2 | 14/15 (93%) | 9/9 (100%) | 1/3 (33%) | 1/8 (12%) | 7/8 (88%) | 17.67 s · 25136/2178 | 0 |
| agent_dense_k3 / test | 11/11 (100%) | {'1': 11} | 1/1/6 · 1.62/2 | 11/11 (100%) | 8/8 (100%) | 1/3 (33%) | 1/8 (12%) | 8/8 (100%) | 4.17 s · 24502/1620 | 0 |

Cấu hình chọn: `agent_rerank_hybrid`, baseline test `agent_dense_k3`, benchmark commit `bab4836`.
Tiêu chí quyết định: 1. Context Evidence Rate of the final context sent to the model: rerank 20/20 vs dense 18/20, inferred 18/20, hybrid 17/20 (difference 2 questions > tie threshold of 1). This criterion does not depend on manual labels.
