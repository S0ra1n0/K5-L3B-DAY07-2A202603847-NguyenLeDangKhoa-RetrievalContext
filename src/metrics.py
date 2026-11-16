"""Retrieval and context metrics with one hit definition (same as Day 6).

A chunk HITS a question when, for at least one gold alternative, the chunk has the gold
source_id, covers the gold page (page in chunk.pages) and contains EVERY evidence quote
(whitespace collapsed). Context Evidence Rate uses the final context sent to the model:
for one gold alternative, every quote must appear in some context chunk of that source
covering that page; quotes may come from different chunks (e.g. two parts of one article).
Unanswerable questions are excluded from every denominator here.
"""
from __future__ import annotations

from typing import Any, Iterable


def squash(text: str) -> str:
    return " ".join(text.split())


def _covers(chunk: dict[str, Any], gold: dict[str, Any]) -> bool:
    pages = chunk.get("pages") or [chunk.get("page")]
    return chunk["source_id"] == gold["source_id"] and gold["page"] in pages


def chunk_hit(chunk: dict[str, Any], golds: Iterable[dict[str, Any]]) -> bool:
    text = squash(chunk["text"])
    return any(_covers(chunk, g) and all(squash(q) in text for q in g["evidence"]) for g in golds)


def context_has_evidence(context_chunks: list[dict[str, Any]], golds: Iterable[dict[str, Any]]) -> bool:
    for g in golds:
        texts = [squash(c["text"]) for c in context_chunks if _covers(c, g)]
        if texts and all(any(squash(q) in t for t in texts) for q in g["evidence"]):
            return True
    return False


def first_hit_rank(results: list[dict[str, Any]], golds: list[dict[str, Any]]) -> int | None:
    return next((i for i, c in enumerate(results, start=1) if chunk_hit(c, golds)), None)


def ratio(n: int, total: int) -> dict[str, Any]:
    return {"n": n, "N": total, "rate": round(n / total, 4) if total else None}


def summarize_retrieval(rows: list[dict[str, Any]]) -> dict[str, Any]:
    """rows: per answerable question {hit1, hit3, context_hit, rr}; returns n/N and rates."""
    total = len(rows)
    return {"hit@1": ratio(sum(r["hit1"] for r in rows), total),
            "evidence_hit@3": ratio(sum(r["hit3"] for r in rows), total),
            "context_evidence_rate": ratio(sum(r["context_hit"] for r in rows), total),
            "mrr@10": round(sum(r["rr"] for r in rows) / total, 4) if total else None}
