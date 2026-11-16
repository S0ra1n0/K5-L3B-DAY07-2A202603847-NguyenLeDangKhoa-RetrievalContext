"""Load Day 6 chunks and the Day 7 benchmark; convert Day 6 questions; hide gold from the agent.

Chunk contract (data/README.md, extended): id, text, source_id, source, page, pages, metadata.
Answerable question: id, split, type, origin, question, [filter], answerable=True,
expected_answer, gold=[{source_id, page, article, evidence: [quote, ...]}, ...]. Gold entries
are ALTERNATIVES; within one gold, EVERY quote is required.
Unanswerable question: answerable=False, expected_behavior="search_and_abstain",
absence_reason, absence_check={keywords: [...]}.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from . import config

# The only question fields the agent and the retrievers may see.
PUBLIC_FIELDS = ("id", "question", "filter")


def load_chunks(path: Path = config.CHUNKS_PATH) -> list[dict[str, Any]]:
    chunks = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                chunks.append(convert_chunk(json.loads(line)))
    ids = [c["id"] for c in chunks]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate chunk id")
    return chunks


def convert_chunk(raw: dict[str, Any]) -> dict[str, Any]:
    """Day 6 JSONL row -> Day 7 chunk; keeps pages/year/article/part for filters and context."""
    meta = dict(raw.get("metadata") or {})
    return {"id": raw["chunk_id"], "text": raw["text"], "source_id": raw["document_id"],
            "source": raw["source"], "page": raw["page"], "pages": list(meta.get("pages") or [raw["page"]]),
            "metadata": meta}


def load_pages(path: Path = config.PAGES_PATH) -> list[dict[str, Any]]:
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def convert_day6_question(q: dict[str, Any], *, split: str | None = None, origin: str | None = None) -> dict[str, Any]:
    gold = [{"source_id": q["gold_source_id"], "page": q["gold_page"], "article": q.get("gold_article"),
             "evidence": list(q["evidence_quote"])}]
    for alt in q.get("alternative_gold") or []:
        gold.append({"source_id": alt["source_id"], "page": alt["page"], "article": alt.get("article"),
                     "evidence": list(alt["evidence_quote"])})
    out = {"id": q["id"], "split": split or q["split"], "type": q["type"],
           "origin": origin or f"day6-{q['split']}", "question": q["question"], "answerable": True,
           "expected_answer": q["expected_answer"], "gold": gold}
    if q.get("filter"):
        out["filter"] = dict(q["filter"])
    return out


def load_benchmark(path: Path = config.BENCHMARK_PATH, split: str | None = None) -> list[dict[str, Any]]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    questions = data["questions"] if isinstance(data, dict) else data
    if split is not None:
        if split not in ("dev", "test"):
            raise ValueError("split must be dev or test")
        questions = [q for q in questions if q["split"] == split]
    return questions


def public_view(question: dict[str, Any]) -> dict[str, Any]:
    """What the agent/retriever receives: no gold, expected answer or absence notes."""
    view = {k: question[k] for k in PUBLIC_FIELDS if k in question}
    if "filter" in view:
        view["filter"] = dict(view["filter"])
    return view
