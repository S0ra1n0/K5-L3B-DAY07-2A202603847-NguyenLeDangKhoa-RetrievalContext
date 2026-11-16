# Retrieval comparison · dev

Benchmark commit `bab4836`. Same corpus (chunk set B, 552 chunks), index, questions, gold and hit definition for every row. Query = original question; filter = user-provided `filter`.

| Config | Hit@1 | Evidence Hit@3 | Context Evidence Rate | MRR@10 | Avg context (chars) | Median latency (ms) | Setup (s) | Cost |
|---|---|---|---|---|---|---|---|---|
| dense_k3 | 16/20 (80%) | 20/20 (100%) | 20/20 (100%) | 0.8917 | 2267.9 | 63.0 | 25.84 | 0 USD |
| bm25_syllable | 17/20 (85%) | 20/20 (100%) | 20/20 (100%) | 0.925 | 2346.7 | 2.6 | 0.06 | 0 USD |
| bm25_pyvi | 18/20 (90%) | 20/20 (100%) | 20/20 (100%) | 0.95 | 2363.2 | 2.3 | 0.95 | 0 USD |
| hybrid_rrf | 19/20 (95%) | 20/20 (100%) | 20/20 (100%) | 0.975 | 2315 | 66.6 | 0.0 | 0 USD |
| rerank_hybrid | 20/20 (100%) | 20/20 (100%) | 20/20 (100%) | 1.0 | 2361.7 | 10755.0 | 2.49 | 0 USD |
| rerank_hybrid_expand | 20/20 (100%) | 20/20 (100%) | 20/20 (100%) | 1.0 | 3031.3 | 10954.0 | 0.0 | 0 USD |

## First hit rank per question (only questions where some config is not rank 1)

| Query | dense_k3 | bm25_syllable | bm25_pyvi | hybrid_rrf | rerank_hybrid | rerank_hybrid_expand | dense top-1 (year/article) | question |
|---|---|---|---|---|---|---|---|---|
| q02 | 2 | 1 | 1 | 1 | 1 | 1 | 2012/Đ22 (2/2) | Theo Bộ luật Lao động 2012, công việc tạm thời có thời hạn bao lâu thì các bên đ |
| q05 | 1 | 2 | 2 | 1 | 1 | 1 | 2019/Đ25 (1/1) | Người được tuyển vào vị trí quản lý doanh nghiệp có thể phải thử việc tối đa bao |
| q07 | 2 | 1 | 1 | 1 | 1 | 1 | 2019/Đ36 (3/3) | Nhân viên ký hợp đồng không thời hạn muốn tự nghỉ việc thì phải báo trước cho cô |
| q08 | 2 | 2 | 2 | 2 | 1 | 1 | 2019/Đ36 (3/3) | Theo Bộ luật Lao động 2019, nếu người lao động bị trả lương không đúng thời hạn  |
| q13 | 3 | 1 | 1 | 1 | 1 | 1 | 2019/Đ110 (1/1) | Người làm ca đêm được nghỉ giữa ca ít nhất bao nhiêu phút? |
| q16 | 1 | 2 | 1 | 1 | 1 | 1 | 2012/Đ187 (1/1) | Theo Bộ luật Lao động 2012, người lao động được hưởng lương hưu khi đủ bao nhiêu |
