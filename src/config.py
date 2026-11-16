"""Paths and settings read from .env (no secrets: local Postgres + local Ollama)."""
from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "day6"
CHUNKS_PATH = DATA_DIR / "chunks_B.jsonl"
PAGES_PATH = DATA_DIR / "pages.jsonl"
BENCHMARK_PATH = ROOT / "benchmark" / "questions.json"
RESULTS_DIR = ROOT / "results"
SELECTION_PATH = RESULTS_DIR / "selection.json"

try:
    from dotenv import load_dotenv
    load_dotenv(ROOT / ".env")
except ImportError:  # dotenv is optional for pure-stdlib scripts
    pass

DATABASE_URL = os.getenv("DATABASE_URL", "")
CHUNK_SET = os.getenv("CHUNK_SET", "B")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "intfloat/multilingual-e5-base")
EMBEDDING_DIMENSIONS = 768
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://127.0.0.1:11434")
LLM_MODEL = os.getenv("LLM_MODEL", "qwen3.5:9b")
RERANKER_MODEL = os.getenv("RERANKER_MODEL", "BAAI/bge-reranker-v2-m3")
