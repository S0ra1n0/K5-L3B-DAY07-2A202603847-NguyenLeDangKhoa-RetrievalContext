# Mâu thuẫn giữa lượt 1 (AI đọc) và lượt 2 (kiểm tra tự động) · dev

3/92 dòng khác nhau ở ít nhất một nhãn.

| Config | Query | Khác ở | Lượt 1 grade/cit/abst | Lượt 2 grade/cit/abst | Ghi chú lượt 2 |
|---|---|---|---|---|---|
| agent_dense_k3 | q08 | citation_support | 0/false;false;false/ | 0/true;true;true/ | thiếu số bắt buộc ['4', '97'] |
| agent_hybrid_rrf | q08 | citation_support | 0/false;true;true/ | 0/true;true;true/ | thiếu số bắt buộc ['4', '97'] |
| agent_dense_inferred | q08 | citation_support | 0/false;false;false/ | 0/true;true;true/ | thiếu số bắt buộc ['4', '97'] |
