"""Generate the report's tables from result files, so no number in the report is typed by hand.

Run: .venv/Scripts/python -X utf8 scripts/build_report_tables.py  ->  results/report_tables.md
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
R = ROOT / "results"

RETRIEVAL_ROWS = [
    ("Baseline (M1)", "dense_k3", "dev", "Dense e5 + pgvector (Day 6 config C), top-3, filter năm của người dùng, 3000 ký tự", "Baseline"),
    ("Phương pháp 2 (M2a)", "bm25_syllable", "dev", "BM25 tách âm tiết, top-3, filter, 3000 ký tự", "Từ khóa khớp tốt con số và thuật ngữ"),
    ("Phương pháp 2b (M2b)", "bm25_pyvi", "dev", "BM25 tách từ pyvi, top-3, filter, 3000 ký tự", "Tách từ ghép tiếng Việt giúp BM25"),
    ("Phương pháp 3 (M3)", "hybrid_rrf", "dev", "RRF(k=60) dense top-20 + BM25 top-20, top-3, filter, 3000 ký tự", "Gộp hai tín hiệu bằng thứ hạng"),
    ("Cải thiện 1 (I1, M4)", "rerank_hybrid", "dev", "Hybrid top-20 → bge-reranker-v2-m3 (CPU) → top-3, filter, 3000 ký tự", "Cross-encoder phân biệt Điều kề nhau (lỗi q08)"),
    ("Cải thiện 2 (I2)", "rerank_hybrid_expand", "dev", "Như I1 + ghép các part cùng Điều, 4500 ký tự", "Ghép part để đủ khoản/ngoại lệ"),
    ("Chẩn đoán", "dense_k3_nofilter", "dev", "Như baseline nhưng KHÔNG filter", "Đo tác động của filter năm (lỗi q03, q16)"),
    ("Chẩn đoán", "hybrid_rrf_nofilter", "dev", "Như M3, không filter", ""),
    ("Chẩn đoán", "rerank_hybrid_nofilter", "dev", "Như I1, không filter", ""),
    ("Cấu hình đã chọn", "rerank_hybrid", "test", "Như I1", "Chạy 1 lần sau khi chốt"),
    ("Baseline", "dense_k3", "test", "Như M1", "Chạy 1 lần sau khi chốt"),
]
AGENT_ROWS = [("agent_dense_k3", "dev"), ("agent_hybrid_rrf", "dev"), ("agent_dense_inferred", "dev"),
              ("agent_rerank_hybrid", "dev"), ("agent_rerank_hybrid", "test"), ("agent_dense_k3", "test")]


def nf(m):
    return f"{m['n']}/{m['N']} ({m['n'] / m['N']:.0%})" if m["N"] else "0/0 (không áp dụng)"


def main():
    out = ["# Bảng số liệu cho báo cáo (sinh tự động bằng scripts/build_report_tables.py)", "",
           "## Retrieval và context", "",
           "| Cấu hình | Phương pháp, top-k, filter, rerank, context budget | Giả thuyết / thay đổi | Split | Hit@1 | Evidence Hit@3 | Context Evidence Rate | Thời gian / chi phí |",
           "|---|---|---|---|---|---|---|---|"]
    for label, cfg, split, desc, hyp in RETRIEVAL_ROWS:
        s = json.loads((R / "retrieval" / f"{cfg}_{split}" / "summary.json").read_text(encoding="utf-8"))
        out.append(f"| {label} `{cfg}` | {desc} | {hyp} | {split} | {nf(s['hit@1'])} | {nf(s['evidence_hit@3'])} | "
                   f"{nf(s['context_evidence_rate'])} | trung vị {s['median_latency_ms']} ms/query · 0 USD |")
    out += ["", "## Agent", "",
            "| Cấu hình / split | Tool use | Số lượt gọi | Grounded answer 0/1/2 và trung bình | Citation hợp lệ | Câu có citation | Abstention đúng | Từ chối nhầm | Context cuối đủ evidence | Thời gian trung vị · token vào/ra | Lỗi |",
            "|---|---|---|---|---|---|---|---|---|---|---|"]
    for cfg, split in AGENT_ROWS:
        d = R / "agent" / f"{cfg}_{split}"
        m = json.loads((d / "agent_metrics.json").read_text(encoding="utf-8"))
        s = json.loads((d / "summary.json").read_text(encoding="utf-8"))
        g = m["grounded_answer"]
        out.append(f"| {cfg} / {split} | {nf(m['tool_use'])} | {s['searches_distribution']} | {g['0']}/{g['1']}/{g['2']} · {g['mean']:.2f}/2 | "
                   f"{nf(m['citation_validity'])} | {nf(m['answer_citation_coverage'])} | {nf(m['abstention'])} | "
                   f"{nf(m['false_abstention'])} | {nf(s['context_evidence_rate_final'])} | {s['median_seconds']} s · "
                   f"{s['tokens']['prompt']}/{s['tokens']['output']} | {m['provider_errors']} |")
    sel = json.loads((R / "selection.json").read_text(encoding="utf-8"))
    out += ["", f"Cấu hình chọn: `{sel['selected']}`, baseline test `{sel['baseline_for_test']}`, benchmark commit `{sel['benchmark_commit']}`.",
            f"Tiêu chí quyết định: {sel['decisive_criterion']}"]
    (R / "report_tables.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print("\n".join(out))


if __name__ == "__main__":
    main()
