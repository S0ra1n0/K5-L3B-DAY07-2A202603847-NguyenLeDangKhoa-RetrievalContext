"""Load the Day 6 chunk set B (552 chunks + stored e5 vectors) into pgvector, without the Day 6 repo.

Default is a DRY RUN: it only checks that data/day6/vectors_B.npz matches data/day6/chunks_B.jsonl (same IDs,
same order, 768 dims, unit norm) and that the stored vectors are reproducible with the current embedder
(re-embeds 3 chunks, cosine must be > 0.999). Nothing is written.
With --write it upserts the rows into table `chunks`, chunk_set "B" (idempotent: same IDs are updated, stale
rows of the same documents are deleted), then runs scripts/check_store.py logic yourself to verify.
Run: .venv/Scripts/python -X utf8 scripts/load_vectors.py [--write]
"""
import argparse
import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src import config  # noqa: E402
from src.day6.models import Chunk  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true", help="upsert into pgvector (default: dry run, no write)")
    args = ap.parse_args()
    rows = [json.loads(l) for l in config.CHUNKS_PATH.read_text(encoding="utf-8").splitlines() if l.strip()]
    chunks = [Chunk(**r) for r in rows]
    data = np.load(config.DATA_DIR / "vectors_B.npz", allow_pickle=False)
    ids, vectors = [str(i) for i in data["chunk_ids"]], data["vectors"]
    if ids != [c.chunk_id for c in chunks]:
        raise SystemExit("vectors_B.npz does not match chunks_B.jsonl (IDs or order differ)")
    if vectors.shape != (len(chunks), config.EMBEDDING_DIMENSIONS):
        raise SystemExit(f"unexpected vector shape {vectors.shape}")
    norms = np.linalg.norm(vectors, axis=1)
    if not np.allclose(norms, 1.0, atol=1e-3):
        raise SystemExit("stored vectors are not unit-normalized")
    from src.day6.embeddings import MyEmbedder
    embedder = MyEmbedder()
    probe = [0, len(chunks) // 2, len(chunks) - 1]
    fresh = np.array(embedder.embed_documents([chunks[i].text for i in probe]))
    cos = [float(fresh[k] @ vectors[i]) for k, i in enumerate(probe)]
    print(json.dumps({"chunks": len(chunks), "dims": vectors.shape[1], "fingerprint": str(data["fingerprint"]),
                      "model": embedder.model_name, "re_embed_cosine": [round(c, 5) for c in cos]}, ensure_ascii=False))
    if min(cos) < 0.999:
        raise SystemExit("stored vectors are not reproducible with the current embedder; re-embed instead")
    if not args.write:
        print("dry run OK: nothing written (use --write to upsert into pgvector)")
        return
    from src.day6.store import PgVectorStore
    store = PgVectorStore(config.DATABASE_URL, config.EMBEDDING_DIMENSIONS)
    store.create_schema()
    print(json.dumps(store.upsert(config.CHUNK_SET, chunks, vectors.tolist(), embedder.model_name)))
    print("written; now run scripts/check_store.py")


if __name__ == "__main__":
    main()
