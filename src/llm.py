"""Local Ollama chat with tool calling (standard library HTTP, no SDK).

Settings chosen on 2026-11-16 (roadmap B1): qwen3.5:9b, think=false, temperature 0,
presence_penalty 0 and repeat_penalty 1.0. With the model's default presence_penalty 1.5 it
answered "35 giờ" while the context said "40 giờ": the penalty pushes away from copying numbers
that appear in the context. API cost is 0 USD (local); tokens and wall time are recorded.
"""
from __future__ import annotations

import json
import time
import urllib.error
import urllib.request
from typing import Any

from . import config

OPTIONS = {"temperature": 0, "presence_penalty": 0, "repeat_penalty": 1.0, "num_ctx": 8192, "seed": 7}


class LLMError(RuntimeError):
    pass


class OllamaChat:
    def __init__(self, model: str | None = None, base_url: str | None = None, options: dict[str, Any] | None = None,
                 timeout: float = 300, retries: int = 2):
        self.model = model or config.LLM_MODEL
        self.base_url = (base_url or config.OLLAMA_BASE_URL).rstrip("/")
        self.options = {**OPTIONS, **(options or {})}
        self.timeout, self.retries = timeout, retries

    def describe(self) -> dict[str, Any]:
        return {"provider": "ollama (local)", "model": self.model, "options": self.options, "think": False}

    def chat(self, messages: list[dict[str, Any]], tools: list[dict[str, Any]] | None = None) -> dict[str, Any]:
        body = {"model": self.model, "messages": messages, "stream": False, "think": False, "options": self.options}
        if tools:
            body["tools"] = tools
        data = json.dumps(body, ensure_ascii=False).encode("utf-8")
        last = None
        for attempt in range(self.retries + 1):
            req = urllib.request.Request(f"{self.base_url}/api/chat", data=data, headers={"Content-Type": "application/json"})
            t = time.perf_counter()
            try:
                with urllib.request.urlopen(req, timeout=self.timeout) as r:
                    out = json.loads(r.read())
                return {"message": out["message"], "prompt_tokens": out.get("prompt_eval_count", 0),
                        "output_tokens": out.get("eval_count", 0), "seconds": time.perf_counter() - t,
                        "attempts": attempt + 1}
            except urllib.error.HTTPError as exc:
                last = f"HTTP {exc.code}: {exc.read()[:300]!r}"
                if exc.code < 500:
                    break
            except (urllib.error.URLError, TimeoutError, ConnectionError) as exc:
                last = repr(exc)
            time.sleep(2 * (attempt + 1))
        raise LLMError(f"Ollama call failed after retries: {last}")
