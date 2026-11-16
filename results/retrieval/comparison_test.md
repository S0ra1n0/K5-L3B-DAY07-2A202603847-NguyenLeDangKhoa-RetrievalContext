# Retrieval comparison · test

Benchmark commit `bab4836`. Same corpus (chunk set B, 552 chunks), index, questions, gold and hit definition for every row. Query = original question; filter = user-provided `filter`.

| Config | Hit@1 | Evidence Hit@3 | Context Evidence Rate | MRR@10 | Avg context (chars) | Median latency (ms) | Setup (s) | Cost |
|---|---|---|---|---|---|---|---|---|
| dense_k3 | 6/8 (75%) | 8/8 (100%) | 8/8 (100%) | 0.875 | 2290.9 | 67.0 | 16.07 | 0 USD |
| rerank_hybrid | 8/8 (100%) | 8/8 (100%) | 8/8 (100%) | 1.0 | 2518.5 | 10673.3 | 2.69 | 0 USD |

## First hit rank per question (only questions where some config is not rank 1)

| Query | dense_k3 | rerank_hybrid | dense top-1 (year/article) | question |
|---|---|---|---|---|
| t01 | 2 | 1 | 2012/Đ22 (2/2) | Theo Bộ luật Lao động 2012, hợp đồng lao động xác định thời hạn có thời hạn tron |
| t02 | 2 | 1 | 2012/Đ38 (1/2) | Người lao động đang điều trị tai nạn lao động theo chỉ định của cơ sở khám bệnh, |
