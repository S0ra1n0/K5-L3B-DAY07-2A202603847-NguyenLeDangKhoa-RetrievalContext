# Copied unchanged from Day 6 repo (commit ac26168), starter/src/store.py.
"""Store and search chunk vectors in PostgreSQL + pgvector.

One table `chunks` holds every chunk set, keyed by (chunk_set, chunk_id). Strategy C
has no rows of its own: it searches the B chunk set with a metadata filter.

Search is EXACT: there is no ANN index (HNSW/IVFFlat), so every row of the chunk set
is scored with cosine distance (`<=>`) and filters never cut the candidate list short.
"""
from __future__ import annotations

import json
from typing import Any

import psycopg

from .models import Chunk

FILTER_COLUMNS = {"year", "document_id", "law_number", "chapter", "article"}


def _vec(values: list[float]) -> str:
    return "[" + ",".join(f"{v:.7g}" for v in values) + "]"


class PgVectorStore:
    def __init__(self, database_url: str, dimensions: int) -> None:
        if not database_url:
            raise ValueError("DATABASE_URL is empty (copy starter/.env.example to starter/.env)")
        if dimensions <= 0:
            raise ValueError("dimensions must be positive")
        self.database_url = database_url
        self.dimensions = dimensions

    def connect(self) -> psycopg.Connection:
        return psycopg.connect(self.database_url, connect_timeout=5)

    def create_schema(self) -> None:
        """Create the table if missing; refuse to reuse a table built for other dimensions."""
        with self.connect() as conn, conn.cursor() as cur:
            cur.execute("CREATE EXTENSION IF NOT EXISTS vector")
            cur.execute(f"""
                CREATE TABLE IF NOT EXISTS chunks (
                    chunk_set   text    NOT NULL,
                    chunk_id    text    NOT NULL,
                    document_id text    NOT NULL,
                    source      text    NOT NULL,
                    page        integer NOT NULL,
                    pages       integer[] NOT NULL,
                    year        integer NOT NULL,
                    law_number  text    NOT NULL,
                    chapter     text,
                    article     integer,
                    text        text    NOT NULL,
                    metadata    jsonb   NOT NULL,
                    model       text    NOT NULL,
                    embedding   vector({self.dimensions}) NOT NULL,
                    ingested_at timestamptz NOT NULL DEFAULT now(),
                    PRIMARY KEY (chunk_set, chunk_id)
                )""")
            cur.execute("CREATE INDEX IF NOT EXISTS chunks_set_year ON chunks (chunk_set, year)")
            cur.execute("""
                SELECT atttypmod FROM pg_attribute
                WHERE attrelid = 'chunks'::regclass AND attname = 'embedding'""")
            stored = cur.fetchone()[0]
            if stored != self.dimensions:
                raise RuntimeError(f"table chunks has vector({stored}), model has {self.dimensions} dims")

    def upsert(self, strategy: str, chunks: list[Chunk], vectors: list[list[float]], model: str) -> dict[str, int]:
        """Insert or update chunks of one chunk set; delete its rows no longer produced.

        Stale rows are removed per document present in `chunks`, so re-ingesting a
        changed document drops its old chunks while other documents stay untouched.
        Runs in one transaction.
        """
        if len(chunks) != len(vectors):
            raise ValueError(f"{len(chunks)} chunks but {len(vectors)} vectors")
        for vector in vectors:
            if len(vector) != self.dimensions:
                raise ValueError(f"vector has {len(vector)} dims, expected {self.dimensions}")
        ids = [c.chunk_id for c in chunks]
        if len(ids) != len(set(ids)):
            raise ValueError("duplicate chunk_id in input")
        documents = sorted({c.document_id for c in chunks})
        rows = [(
            strategy, c.chunk_id, c.document_id, c.source, c.page, c.metadata["pages"],
            c.metadata["year"], c.metadata["law_number"], c.metadata.get("chapter"),
            c.metadata.get("article"), c.text, json.dumps(c.metadata, ensure_ascii=False),
            model, _vec(v),
        ) for c, v in zip(chunks, vectors)]
        with self.connect() as conn, conn.cursor() as cur:
            cur.execute("SELECT count(*) FROM chunks WHERE chunk_set = %s", (strategy,))
            before = cur.fetchone()[0]
            cur.executemany("""
                INSERT INTO chunks (chunk_set, chunk_id, document_id, source, page, pages, year,
                                    law_number, chapter, article, text, metadata, model, embedding)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s::jsonb, %s, %s::vector)
                ON CONFLICT (chunk_set, chunk_id) DO UPDATE SET
                    document_id = EXCLUDED.document_id, source = EXCLUDED.source,
                    page = EXCLUDED.page, pages = EXCLUDED.pages, year = EXCLUDED.year,
                    law_number = EXCLUDED.law_number, chapter = EXCLUDED.chapter,
                    article = EXCLUDED.article, text = EXCLUDED.text, metadata = EXCLUDED.metadata,
                    model = EXCLUDED.model, embedding = EXCLUDED.embedding, ingested_at = now()
                """, rows)
            cur.execute("""
                DELETE FROM chunks
                WHERE chunk_set = %s AND document_id = ANY(%s) AND NOT (chunk_id = ANY(%s))""",
                        (strategy, documents, ids))
            deleted = cur.rowcount
            cur.execute("SELECT count(*) FROM chunks WHERE chunk_set = %s", (strategy,))
            after = cur.fetchone()[0]
        return {"before": before, "upserted": len(rows), "deleted_stale": deleted, "after": after}

    def search(self, strategy: str, query_vector: list[float], top_k: int = 3,
               filters: dict[str, Any] | None = None) -> list[dict[str, Any]]:
        """Exact cosine search in one chunk set; filters are equality on known columns."""
        if len(query_vector) != self.dimensions:
            raise ValueError(f"query has {len(query_vector)} dims, expected {self.dimensions}")
        where, params = ["chunk_set = %s"], [strategy]
        for column, value in (filters or {}).items():
            if column not in FILTER_COLUMNS:                      # column names are never user text
                raise ValueError(f"filter on unsupported field {column!r}")
            where.append(f"{column} = %s")
            params.append(value)
        q = _vec(query_vector)
        sql = f"""
            SELECT chunk_id, document_id, source, page, pages, year, law_number, chapter, article,
                   text, metadata, 1 - (embedding <=> %s::vector) AS score
            FROM chunks WHERE {' AND '.join(where)}
            ORDER BY embedding <=> %s::vector, chunk_id
            LIMIT %s"""
        with self.connect() as conn, conn.cursor() as cur:
            cur.execute(sql, [q, *params, q, top_k])
            names = [d.name for d in cur.description]
            return [dict(zip(names, row)) for row in cur.fetchall()]

    def count(self, strategy: str) -> int:
        with self.connect() as conn, conn.cursor() as cur:
            cur.execute("SELECT count(*) FROM chunks WHERE chunk_set = %s", (strategy,))
            return cur.fetchone()[0]

    def delete_set(self, strategy: str) -> int:
        with self.connect() as conn, conn.cursor() as cur:
            cur.execute("DELETE FROM chunks WHERE chunk_set = %s", (strategy,))
            return cur.rowcount
