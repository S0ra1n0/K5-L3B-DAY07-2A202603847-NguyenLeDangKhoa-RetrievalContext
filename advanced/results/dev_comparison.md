# Dev comparison (18 questions: 15 answerable + 3 unanswerable)

Labels: AI reading against the gold evidence and the PDF (`review/dev_labels_v1.json`, `v2.json`, `v3.json`); human check pending.
v1 = first index/agent; v2 = after dev v1 error analysis (table_row chunks, creditor rule, citation repair); v3 = v2 + profile cards mark segments named in the legend, guide page read by columns (after dev v2).

| config | index/agent | pass | table | figure | chart | multihop | text | unanswerable | evidence in context | errors | avg s/question | avg LLM calls | avg prompt tok | avg output tok |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| a0_dense | v1 | **12/18** | 0/3 | 2/3 | 2/3 | 2/3 | 3/3 | 3/3 | 9/15 | 0 | 9.1 | 2.00 | 3244 | 121 |
| a1_hybrid | v1 | **12/18** | 1/3 | 2/3 | 2/3 | 2/3 | 3/3 | 2/3 | 11/15 | 0 | 6.5 | 2.06 | 3470 | 149 |
| a2_rerank | v1 | **13/18** | 1/3 | 3/3 | 2/3 | 2/3 | 3/3 | 2/3 | 11/15 | 0 | 24.1 | 2.00 | 3284 | 123 |
| a3_hybrid_view | v1 | **12/18** | 1/3 | 1/3 | 3/3 | 2/3 | 3/3 | 2/3 | 11/15 | 0 | 22.7 | 2.39 | 5060 | 227 |
| b0_dense | v2 | **17/18** | 3/3 | 2/3 | 3/3 | 3/3 | 3/3 | 3/3 | 13/15 | 0 | 10.0 | 2.17 | 3780 | 123 |
| b1_hybrid | v2 | **15/18** | 3/3 | 1/3 | 3/3 | 2/3 | 3/3 | 3/3 | 13/15 | 0 | 7.6 | 2.11 | 3520 | 137 |
| b2_rerank | v2 | **16/18** | 3/3 | 2/3 | 3/3 | 2/3 | 3/3 | 3/3 | 13/15 | 0 | 24.7 | 2.17 | 3791 | 135 |
| c0_dense | v3 | **18/18** | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 14/15 | 0 | 8.1 | 2.22 | 3969 | 124 |
| c2_rerank | v3 | **16/18** | 3/3 | 2/3 | 3/3 | 2/3 | 3/3 | 3/3 | 13/15 | 0 | 24.5 | 2.11 | 3672 | 127 |

Cost: all models run locally (Ollama `qwen3.5:9b`, e5-base, bge-reranker-v2-m3 on CPU): US$0 API cost; time measured on an RTX 3070 Laptop GPU that was thermally throttled during the runs.
