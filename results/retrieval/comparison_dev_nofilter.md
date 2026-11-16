# Retrieval comparison · dev

Benchmark commit `bab4836`. Same corpus (chunk set B, 552 chunks), index, questions, gold and hit definition for every row. Query = original question; filter = user-provided `filter`.

| Config | Hit@1 | Evidence Hit@3 | Context Evidence Rate | MRR@10 | Avg context (chars) | Median latency (ms) | Setup (s) | Cost |
|---|---|---|---|---|---|---|---|---|
| dense_k3_nofilter | 14/20 (70%) | 19/20 (95%) | 18/20 (90%) | 0.8208 | 2187.1 | 65.9 | 12.93 | 0 USD |
| hybrid_rrf_nofilter | 17/20 (85%) | 19/20 (95%) | 19/20 (95%) | 0.9083 | 2272.9 | 66.6 | 0.05 | 0 USD |
| rerank_hybrid_nofilter | 18/20 (90%) | 20/20 (100%) | 20/20 (100%) | 0.95 | 2263.9 | 10623.5 | 2.6 | 0 USD |

## First hit rank per question (only questions where some config is not rank 1)

| Query | dense_k3_nofilter | hybrid_rrf_nofilter | rerank_hybrid_nofilter | dense top-1 (year/article) | question |
|---|---|---|---|---|---|
| q02 | 2 | 1 | 1 | 2012/Đ22 (2/2) | Theo Bộ luật Lao động 2012, công việc tạm thời có thời hạn bao lâu thì các bên đ |
| q03 | 2 | 2 | 1 | 2012/Đ106 (1/1) | Theo Bộ luật Lao động 2019, số giờ làm thêm của người lao động tối đa trong một  |
| q04 | 1 | 1 | 2 | 2012/Đ106 (1/1) | Bộ luật Lao động 2012 giới hạn số giờ làm thêm trong một tháng là bao nhiêu? |
| q07 | 2 | 1 | 1 | 2019/Đ36 (3/3) | Nhân viên ký hợp đồng không thời hạn muốn tự nghỉ việc thì phải báo trước cho cô |
| q08 | 4 | 2 | 1 | 2012/Đ43 (1/1) | Theo Bộ luật Lao động 2019, nếu người lao động bị trả lương không đúng thời hạn  |
| q13 | 3 | 1 | 1 | 2019/Đ110 (1/1) | Người làm ca đêm được nghỉ giữa ca ít nhất bao nhiêu phút? |
| q16 | 3 | 6 | 2 | 2019/Đ219 (6/10) | Theo Bộ luật Lao động 2012, người lao động được hưởng lương hưu khi đủ bao nhiêu |
