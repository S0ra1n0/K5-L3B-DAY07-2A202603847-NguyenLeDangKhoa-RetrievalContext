"""Check the Day 6 pgvector store before Day 7 uses it (roadmap P1.3).

Checks: row count of chunk set B equals the 552 local chunks and their IDs match; stored model and
vector dims; query embedding compatibility (5 chunks used as queries must retrieve themselves at
rank 1); year filter returns only that year. No mock fallback: any failure raises.
Run: .venv/Scripts/python -X utf8 scripts/check_store.py
"""
import json
import platform
import statistics
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src import config  # noqa: E402
from src.data_io import load_chunks  # noqa: E402
from src.day6.embeddings import MyEmbedder  # noqa: E402
from src.day6.store import PgVectorStore  # noqa: E402


def main():
    chunks = load_chunks()
    store = PgVectorStore(config.DATABASE_URL, config.EMBEDDING_DIMENSIONS)
    with store.connect() as conn, conn.cursor() as cur:
        cur.execute("SELECT version(), (SELECT extversion FROM pg_extension WHERE extname = 'vector')")
        pg_version, pgvector_version = cur.fetchone()
        cur.execute("SELECT chunk_id, model, vector_dims(embedding) FROM chunks WHERE chunk_set = %s", (config.CHUNK_SET,))
        rows = cur.fetchall()
    db_ids = {r[0] for r in rows}
    local_ids = {c["id"] for c in chunks}
    report = {"postgres": pg_version.split(",")[0], "pgvector": pgvector_version, "chunk_set": config.CHUNK_SET,
              "rows": len(rows), "local_chunks": len(chunks), "ids_match": db_ids == local_ids,
              "models": sorted({r[1] for r in rows}), "dims": sorted({r[2] for r in rows})}
    embedder = MyEmbedder()
    report["embedder"] = embedder.describe()
    probes = [chunks[i] for i in (10, 120, 260, 400, 540)]
    self_hits, latencies = [], []
    for c in probes:
        t = time.perf_counter()
        hits = store.search(config.CHUNK_SET, embedder.embed_query(c["text"]), top_k=3)
        latencies.append((time.perf_counter() - t) * 1000)
        self_hits.append({"chunk_id": c["id"], "top1": hits[0]["chunk_id"], "self_at_1": hits[0]["chunk_id"] == c["id"]})
    report["self_retrieval"] = {"n": sum(h["self_at_1"] for h in self_hits), "N": len(self_hits), "probes": self_hits}
    report["query_latency_ms_median"] = round(statistics.median(latencies), 1)
    vec = embedder.embed_query("số giờ làm thêm tối đa trong một tháng")
    report["year_filter"] = {str(y): sorted({h["year"] for h in store.search(config.CHUNK_SET, vec, top_k=10, filters={"year": y})})
                             for y in (2012, 2019)}
    report["machine"] = {"python": platform.python_version(), "platform": platform.platform()}
    report["ok"] = (report["rows"] == 552 and report["ids_match"] and report["dims"] == [768]
                    and report["models"] == [config.EMBEDDING_MODEL]
                    and report["self_retrieval"]["n"] == len(probes)
                    and report["year_filter"] == {"2012": [2012], "2019": [2019]})
    out = ROOT / "results" / "setup" / "store_check.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2, default=str) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2, default=str))
    sys.exit(0 if report["ok"] else 1)


if __name__ == "__main__":
    main()
