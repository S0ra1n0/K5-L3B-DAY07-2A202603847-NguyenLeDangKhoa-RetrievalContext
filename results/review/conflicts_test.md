# Mâu thuẫn giữa lượt 1 (AI đọc) và lượt 2 (kiểm tra tự động) · test

5/22 dòng khác nhau ở ít nhất một nhãn.

| Config | Query | Khác ở | Lượt 1 grade/cit/abst | Lượt 2 grade/cit/abst | Ghi chú lượt 2 |
|---|---|---|---|---|---|
| agent_dense_k3 | t02 | answer_grade | 1/true;true/ | 2/true;true/ |  |
| agent_dense_k3 | t08 | citation_support | 2/true/ | 2/false/ | [25405e] câu nhắc Điều ['188'] nhưng cite Điều 199 |
| agent_rerank_hybrid | t06 | citation_support | 2/true;true/ | 2/true;false/ | [f8e349] câu nhắc Điều ['116'] nhưng cite Điều 115 |
| agent_rerank_hybrid | t08 | citation_support | 2/true;true/ | 2/false;true/ | [25405e] câu nhắc Điều ['188'] nhưng cite Điều 199 |
| agent_rerank_hybrid | t09 | citation_support | /true;false/false | /true;true/false | không từ chối (status answered) |
