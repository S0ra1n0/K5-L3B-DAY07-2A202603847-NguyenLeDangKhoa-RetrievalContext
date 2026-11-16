"""Retrievers over the advanced chunk set (text, table, figure and profile chunks in one index).

dense  : intfloat/multilingual-e5-base (same model as the base lab), exact cosine in memory (526 chunks, no DB
         needed); passage vectors cached in advanced/data/index/vectors.npy, keyed by a hash of all chunk texts.
bm25   : base-lab BM25Retriever (Okapi, \\w+ tokens, casefold) on the same chunks.
hybrid : base-lab HybridRRF (k = 60) over dense + bm25.
rerank : base-lab CrossEncoderReranker (BAAI/bge-reranker-v2-m3, CPU) over any base.
Results have the base-lab shape: {id, text, kind, page, page_label, metadata, score, rank, strategy}.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from src.retrievers import BM25Retriever, CrossEncoderReranker, HybridRRF, _ranked  # noqa: E402

from .chunks import CHUNKS, INDEX  # noqa: E402

VECTORS = INDEX / "vectors.npy"
VECTORS_META = INDEX / "vectors.json"


def load_chunks() -> list[dict[str, Any]]:
    return [json.loads(l) for l in CHUNKS.read_text(encoding="utf-8").splitlines() if l.strip()]


def _fingerprint(chunks) -> str:
    h = hashlib.sha256()
    for c in chunks:
        h.update(c["id"].encode())
        h.update(c["text"].encode())
    return h.hexdigest()


class DenseMemory:
    def __init__(self, chunks, embedder=None):
        from src.day6.embeddings import MyEmbedder
        self.name = "dense"
        self.chunks = chunks
        self.embedder = embedder or MyEmbedder()
        fp = _fingerprint(chunks)
        meta = json.loads(VECTORS_META.read_text(encoding="utf-8")) if VECTORS_META.exists() else {}
        if VECTORS.exists() and meta.get("fingerprint") == fp:
            self.matrix = np.load(VECTORS)
        else:
            self.matrix = np.asarray(self.embedder.embed_documents([c["text"] for c in chunks]), dtype=np.float32)
            np.save(VECTORS, self.matrix)
            lengths = self.embedder.token_lengths([c["text"] for c in chunks])
            VECTORS_META.write_text(json.dumps({"fingerprint": fp, "model": self.embedder.describe(),
                                                "chunks": len(chunks), "truncated_over_512_tokens":
                                                    [c["id"] for c, n in zip(chunks, lengths) if n > 512]},
                                               ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    def search(self, query, *, filters=None, top_k=3):
        if filters:
            raise ValueError("filters are not used in the advanced index")
        q = np.asarray(self.embedder.embed_query(query), dtype=np.float32)
        scores = self.matrix @ q
        order = np.argsort(-scores, kind="stable")[:top_k]
        return _ranked([{**self.chunks[i], "score": float(scores[i])} for i in order], self.name)


def build_retriever(spec: dict[str, Any], *, cache: dict[str, Any] | None = None):
    cache = cache if cache is not None else {}
    if "chunks" not in cache:
        cache["chunks"] = load_chunks()
    m = spec["method"]
    if m == "dense":
        if "dense" not in cache:
            cache["dense"] = DenseMemory(cache["chunks"])
        return cache["dense"]
    if m == "bm25":
        if "bm25" not in cache:
            cache["bm25"] = BM25Retriever(cache["chunks"], tokenizer="syllable")
        return cache["bm25"]
    if m == "hybrid":
        return HybridRRF(build_retriever({"method": "dense"}, cache=cache), build_retriever({"method": "bm25"}, cache=cache),
                         candidates=spec.get("candidates", 20), k=spec.get("rrf_k", 60))
    if m == "rerank":
        base = build_retriever(spec["base"], cache=cache)
        if "reranker" not in cache:
            cache["reranker"] = CrossEncoderReranker(base, candidates=spec.get("candidates", 20))
        clone = object.__new__(CrossEncoderReranker)
        clone.__dict__.update(cache["reranker"].__dict__, base=base, candidates=spec.get("candidates", 20),
                              name=f"rerank({base.name})")
        return clone
    raise ValueError(f"unknown method {m!r}")
