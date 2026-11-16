"""Smoke-test every retrieval config on ONE ad-hoc query that is not in the benchmark (load time, latency, top-3).

Run: .venv/Scripts/python -X utf8 scripts/smoke_retrievers.py "câu hỏi" [year]
"""
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.retrievers import build_retriever  # noqa: E402


def main():
    query = sys.argv[1]
    filters = {"year": int(sys.argv[2])} if len(sys.argv) > 2 else None
    cache = {}
    for path in sorted((ROOT / "configs").glob("*.json")):
        cfg = json.loads(path.read_text(encoding="utf-8"))
        if cfg["name"].startswith("agent_"):
            continue
        t = time.perf_counter()
        r = build_retriever(cfg["retriever"], cache=cache)
        load = time.perf_counter() - t
        t = time.perf_counter()
        top = r.search(query, filters=filters, top_k=3)
        ms = (time.perf_counter() - t) * 1000
        print(f"{cfg['name']:<22} load {load:6.1f}s  query {ms:7.0f} ms  top3 " +
              ", ".join(f"{x['metadata']['year']}/Đ{x['metadata'].get('article')}({x['score']:.3f})" for x in top))


if __name__ == "__main__":
    main()
