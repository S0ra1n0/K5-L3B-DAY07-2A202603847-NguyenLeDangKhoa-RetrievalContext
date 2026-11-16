# Copied unchanged from Day 6 repo (commit ac26168), starter/src/embeddings.py.
"""Real embedding model: intfloat/multilingual-e5-base run locally with sentence-transformers.

E5 models expect a role prefix: "query: " for questions and "passage: " for chunks.
Vectors are L2-normalized, so cosine similarity = dot product. Any load or encode
failure raises; there is no fallback to mock or random vectors.
"""
from __future__ import annotations

import os
from typing import Any, Protocol

DEFAULT_MODEL = "intfloat/multilingual-e5-base"
QUERY_PREFIX = "query: "
PASSAGE_PREFIX = "passage: "


class Embedder(Protocol):
    model_name: str
    dimensions: int

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        """Return one vector per input text, in the same order."""
        ...

    def embed_query(self, question: str) -> list[float]:
        """Return a query vector compatible with the stored document vectors."""
        ...


class MyEmbedder:
    """multilingual-e5-base (768 dims, max 512 tokens) via sentence-transformers."""

    def __init__(self, model_name: str | None = None, device: str | None = None,
                 batch_size: int = 32) -> None:
        from sentence_transformers import SentenceTransformer

        self.model_name = model_name or os.getenv("EMBEDDING_MODEL") or DEFAULT_MODEL
        self.device = device or os.getenv("EMBEDDING_DEVICE", "cpu")
        self.batch_size = batch_size
        self.model = SentenceTransformer(self.model_name, device=self.device)
        self.dimensions = int(self.model.get_sentence_embedding_dimension())
        self.max_seq_length = int(self.model.max_seq_length)

    # -- encoding -------------------------------------------------------------------
    def _encode(self, texts: list[str]) -> list[list[float]]:
        vectors = self.model.encode(texts, batch_size=self.batch_size, normalize_embeddings=True,
                                    convert_to_numpy=True, show_progress_bar=False)
        if vectors.shape != (len(texts), self.dimensions):
            raise RuntimeError(f"unexpected embedding shape {vectors.shape}")
        return vectors.astype("float32").tolist()

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        return self._encode([PASSAGE_PREFIX + t for t in texts])

    def embed_query(self, question: str) -> list[float]:
        return self._encode([QUERY_PREFIX + question])[0]

    # -- reporting ------------------------------------------------------------------
    def token_lengths(self, texts: list[str], prefix: str = PASSAGE_PREFIX) -> list[int]:
        """Token count per text including prefix and special tokens (to detect truncation)."""
        tokenizer = self.model.tokenizer
        return [len(ids) for ids in tokenizer([prefix + t for t in texts], add_special_tokens=True)["input_ids"]]

    def describe(self) -> dict[str, Any]:
        import sentence_transformers
        import torch
        import transformers
        from huggingface_hub import try_to_load_from_cache

        config_path = try_to_load_from_cache(self.model_name, "config.json")
        revision = str(config_path).replace("\\", "/").split("/snapshots/")[1].split("/")[0] \
            if isinstance(config_path, str) and "/snapshots/" in config_path.replace("\\", "/") else None
        return {
            "provider": "local (sentence-transformers)",
            "model": self.model_name,
            "revision": revision,
            "dimensions": self.dimensions,
            "max_seq_length_tokens": self.max_seq_length,
            "query_prefix": QUERY_PREFIX,
            "passage_prefix": PASSAGE_PREFIX,
            "normalized": True,
            "similarity": "cosine",
            "device": self.device,
            "batch_size": self.batch_size,
            "versions": {"sentence_transformers": sentence_transformers.__version__,
                         "transformers": transformers.__version__, "torch": torch.__version__},
            "cost_usd": 0.0,
        }
