"""Context selection: dedup, optional expansion to the other parts of the same article, char budget.

Each block starts with a header that keeps source and conditions checkable:
[chunk-id | blld-2019 | năm 2019 | trang 40 | Điều 107 | phần 1/2]
Blocks are added in rank order; a block that does not fit the remaining budget is skipped
(later, shorter blocks may still fit). Budget counts characters of the whole context, headers included.
"""
from __future__ import annotations

from typing import Any


def header(c: dict[str, Any]) -> str:
    m = c["metadata"]
    pages = c.get("pages") or [c["page"]]
    page = f"trang {pages[0]}" if len(pages) == 1 else f"trang {pages[0]}-{pages[-1]}"
    parts = f" | phần {m.get('part')}/{m.get('parts')}" if (m.get("parts") or 1) > 1 else ""
    article = f" | Điều {m['article']}" if m.get("article") is not None else ""
    return f"[{c['id']} | {c['source_id']} | năm {m.get('year')} | {page}{article}{parts}]"


def block(c: dict[str, Any]) -> str:
    return f"{header(c)}\n{c['text']}"


class ContextBuilder:
    def __init__(self, chunks: list[dict[str, Any]], *, budget: int = 2400, expand_parts: bool = False):
        if budget < 1:
            raise ValueError("budget must be positive")
        self.budget, self.expand_parts = budget, expand_parts
        self.siblings: dict[tuple, list[dict[str, Any]]] = {}
        for c in chunks:
            art = c["metadata"].get("article")
            if art is not None:
                self.siblings.setdefault((c["source_id"], art), []).append(c)
        for rows in self.siblings.values():
            rows.sort(key=lambda c: c["metadata"].get("part") or 1)

    def _expand(self, c: dict[str, Any]) -> list[dict[str, Any]]:
        art = c["metadata"].get("article")
        if not self.expand_parts or art is None or (c["metadata"].get("parts") or 1) <= 1:
            return [c]
        return self.siblings.get((c["source_id"], art), [c])

    def build(self, ranked: list[dict[str, Any]]) -> dict[str, Any]:
        """ranked: retrieval results in priority order (may contain duplicates across searches)."""
        blocks, chosen, seen, skipped, used = [], [], set(), [], 0
        for c in ranked:
            for item in self._expand(c):
                if item["id"] in seen:
                    continue
                seen.add(item["id"])
                text = block(item)
                cost = len(text) + (2 if blocks else 0)
                if used + cost > self.budget:
                    skipped.append(item["id"])
                    continue
                blocks.append(text)
                chosen.append(item)
                used += cost
        return {"context": "\n\n".join(blocks), "context_ids": [c["id"] for c in chosen], "chunks": chosen,
                "chars": used, "skipped_for_budget": skipped,
                "added_by_expansion": [c["id"] for c in chosen if c["id"] not in {r["id"] for r in ranked}]}
