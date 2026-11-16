"""Retrieval methods over the Day 6 chunk set B. Every method returns the same result shape:

{id, text, source_id, source, page, pages, metadata, score, rank, strategy}

M1 dense   : multilingual-e5-base query embedding + exact cosine search in pgvector (Day 6 store).
M2 bm25    : BM25 (Okapi) in memory; tokenizer "syllable" (NFC + casefold + \\w+) or "pyvi" (word segmentation).
M3 hybrid  : Reciprocal Rank Fusion of dense and BM25 candidate lists, score = sum 1/(k + rank), k = 60.
M4 rerank  : any candidate retriever, re-scored by a cross-encoder (BAAI/bge-reranker-v2-m3, CPU).

Filters are equality on metadata (year, article, document_id). They come from the user (benchmark
`filter`) or from the agent's tool arguments; never from gold. Errors propagate, no mock fallback.
"""
from __future__ import annotations

import re
import unicodedata
from typing import Any, Protocol

from . import config
from .data_io import load_chunks

FILTER_KEYS = {"year", "article", "document_id", "law_number", "chapter"}


class Retriever(Protocol):
    name: str

    def search(self, query: str, *, filters: dict[str, Any] | None = None, top_k: int = 3) -> list[dict[str, Any]]:
        ...


def _check_filters(filters: dict[str, Any] | None) -> dict[str, Any]:
    filters = dict(filters or {})
    bad = set(filters) - FILTER_KEYS
    if bad:
        raise ValueError(f"unsupported filter fields {sorted(bad)}")
    return filters


def _matches(chunk: dict[str, Any], filters: dict[str, Any]) -> bool:
    meta = chunk["metadata"]
    for key, value in filters.items():
        actual = chunk["source_id"] if key == "document_id" else meta.get(key)
        if actual != value:
            return False
    return True


def _ranked(rows: list[dict[str, Any]], strategy: str) -> list[dict[str, Any]]:
    return [{**r, "rank": i, "strategy": strategy} for i, r in enumerate(rows, start=1)]


class DenseRetriever:
    """M1: query embedding compatible with the Day 6 index (same model, `query:` prefix)."""

    def __init__(self, embedder=None, store=None, chunks: list[dict[str, Any]] | None = None):
        from .day6.embeddings import MyEmbedder
        from .day6.store import PgVectorStore
        self.name = "dense"
        self.embedder = embedder or MyEmbedder()
        self.store = store or PgVectorStore(config.DATABASE_URL, config.EMBEDDING_DIMENSIONS)
        self.by_id = {c["id"]: c for c in (chunks or load_chunks())}

    def search(self, query, *, filters=None, top_k=3):
        filters = _check_filters(filters)
        if not query.strip():
            raise ValueError("empty query")
        rows = self.store.search(config.CHUNK_SET, self.embedder.embed_query(query), top_k=top_k, filters=filters)
        out = []
        for r in rows:
            c = self.by_id.get(r["chunk_id"])
            if c is None:
                raise RuntimeError(f"store returned unknown chunk {r['chunk_id']} (index and local chunks differ)")
            out.append({**c, "score": float(r["score"])})
        return _ranked(out, self.name)


def tokenize_syllable(text: str) -> list[str]:
    return re.findall(r"\w+", unicodedata.normalize("NFC", text).casefold())


def tokenize_pyvi(text: str) -> list[str]:
    from pyvi import ViTokenizer
    segmented = ViTokenizer.tokenize(unicodedata.normalize("NFC", text))
    return [t.casefold() for t in segmented.split() if re.search(r"\w", t)]


class BM25Retriever:
    """M2: Okapi BM25 over all chunks; filters applied before ranking (exact, no candidate loss)."""

    def __init__(self, chunks: list[dict[str, Any]] | None = None, tokenizer: str = "syllable",
                 k1: float = 1.5, b: float = 0.75):
        from rank_bm25 import BM25Okapi
        self.name = f"bm25_{tokenizer}"
        self.tokenize = {"syllable": tokenize_syllable, "pyvi": tokenize_pyvi}[tokenizer]
        self.chunks = chunks or load_chunks()
        self.bm25 = BM25Okapi([self.tokenize(c["text"]) for c in self.chunks], k1=k1, b=b)

    def search(self, query, *, filters=None, top_k=3):
        filters = _check_filters(filters)
        terms = self.tokenize(query)
        if not terms:
            raise ValueError("empty query")
        scores = self.bm25.get_scores(terms)
        rows = [(float(s), c) for s, c in zip(scores, self.chunks) if s > 0 and _matches(c, filters)]
        rows.sort(key=lambda x: (-x[0], x[1]["id"]))
        return _ranked([{**c, "score": s} for s, c in rows[:top_k]], self.name)


class HybridRRF:
    """M3: RRF over dense and BM25 lists of `candidates` each; ranks only, raw scores are not added."""

    def __init__(self, dense: Retriever, lexical: Retriever, candidates: int = 20, k: int = 60):
        self.name = f"hybrid_rrf({dense.name}+{lexical.name})"
        self.dense, self.lexical, self.candidates, self.k = dense, lexical, candidates, k

    def search(self, query, *, filters=None, top_k=3):
        fused: dict[str, dict[str, Any]] = {}
        for source in (self.dense, self.lexical):
            for r in source.search(query, filters=filters, top_k=self.candidates):
                entry = fused.setdefault(r["id"], {**{k: v for k, v in r.items() if k not in ("score", "rank", "strategy")},
                                                   "score": 0.0, "components": {}})
                entry["score"] += 1.0 / (self.k + r["rank"])
                entry["components"][source.name] = {"rank": r["rank"], "score": r["score"]}
        rows = sorted(fused.values(), key=lambda r: (-r["score"], r["id"]))[:top_k]
        return _ranked(rows, self.name)


class CrossEncoderReranker:
    """M4: take `candidates` from a base retriever, re-score (query, chunk) pairs with a cross-encoder."""

    def __init__(self, base: Retriever, candidates: int = 20, model_name: str | None = None, device: str = "cpu"):
        from sentence_transformers import CrossEncoder
        self.name = f"rerank({base.name})"
        self.base, self.candidates = base, candidates
        self.model_name = model_name or config.RERANKER_MODEL
        self.model = CrossEncoder(self.model_name, device=device, max_length=512)

    def search(self, query, *, filters=None, top_k=3):
        pool = self.base.search(query, filters=filters, top_k=self.candidates)
        if not pool:
            return []
        scores = self.model.predict([(query, c["text"]) for c in pool], batch_size=8, show_progress_bar=False)
        rows = [{**{k: v for k, v in c.items() if k not in ("score", "rank", "strategy")}, "score": float(s),
                 "before_rerank": {"rank": c["rank"], "score": c["score"]}} for c, s in zip(pool, scores)]
        rows.sort(key=lambda r: (-r["score"], r["id"]))
        return _ranked(rows[:top_k], self.name)


def build_retriever(spec: dict[str, Any], *, cache: dict[str, Any] | None = None) -> Retriever:
    """Build from a config dict, e.g. {"method": "rerank", "base": {"method": "hybrid", ...}, "candidates": 20}.
    `cache` shares heavy objects (embedder, chunks, BM25 index, cross-encoder) across configs."""
    cache = cache if cache is not None else {}
    method = spec["method"]
    if "chunks" not in cache:
        cache["chunks"] = load_chunks()
    if method == "dense":
        if "dense" not in cache:
            cache["dense"] = DenseRetriever(chunks=cache["chunks"])
        return cache["dense"]
    if method == "bm25":
        key = f"bm25_{spec.get('tokenizer', 'syllable')}"
        if key not in cache:
            cache[key] = BM25Retriever(cache["chunks"], tokenizer=spec.get("tokenizer", "syllable"))
        return cache[key]
    if method == "hybrid":
        return HybridRRF(build_retriever({"method": "dense"}, cache=cache),
                         build_retriever({"method": "bm25", "tokenizer": spec.get("tokenizer", "syllable")}, cache=cache),
                         candidates=spec.get("candidates", 20), k=spec.get("rrf_k", 60))
    if method == "rerank":
        base = build_retriever(spec["base"], cache=cache)
        key = "reranker_model"
        if key not in cache:
            cache[key] = CrossEncoderReranker(base, candidates=spec.get("candidates", 20))
        rr = cache[key]
        if rr.base is not base or rr.candidates != spec.get("candidates", 20):
            clone = object.__new__(CrossEncoderReranker)
            clone.__dict__.update(rr.__dict__, base=base, candidates=spec.get("candidates", 20),
                                  name=f"rerank({base.name})")
            return clone
        return rr
    raise ValueError(f"unknown method {method!r}")
