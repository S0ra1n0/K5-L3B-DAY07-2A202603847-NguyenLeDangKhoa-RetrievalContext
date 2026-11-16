"""Offline checks for retrievers, context builder, agent loop and guards (fake LLM/store; no quality claims)."""
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src import config, guards  # noqa: E402
from src.agent import run_agent  # noqa: E402
from src.context import ContextBuilder  # noqa: E402
from src.retrievers import BM25Retriever, HybridRRF, tokenize_syllable  # noqa: E402


def ch(cid, text, year=2019, article=1, part=1, parts=1, doc=None):
    return {"id": cid, "text": text, "source_id": doc or f"blld-{year}", "source": "x.pdf", "page": 1, "pages": [1],
            "metadata": {"year": year, "article": article, "part": part, "parts": parts}}


CHUNKS = [ch("a" * 16, "làm thêm không quá 40 giờ trong 01 tháng", 2019, 107),
          ch("b" * 16, "làm thêm không quá 30 giờ trong 01 tháng", 2012, 106),
          ch("c" * 16, "nghỉ hằng tuần ít nhất 24 giờ liên tục", 2019, 111, 1, 2),
          ch("d" * 16, "nghỉ bù vào ngày làm việc kế tiếp", 2019, 111, 2, 2)]


class Fixed:
    def __init__(self, name, rows): self.name, self.rows = name, rows
    def search(self, query, *, filters=None, top_k=3):
        return [{**r, "rank": i, "score": 1.0 / i, "strategy": self.name} for i, r in enumerate(self.rows[:top_k], 1)]


class RetrieverTests(unittest.TestCase):
    def test_bm25_filter_and_tokens(self):
        self.assertEqual(tokenize_syllable("Giờ  làm THÊM"), ["giờ", "làm", "thêm"])
        bm25 = BM25Retriever(CHUNKS)
        top = bm25.search("làm thêm giờ trong tháng", filters={"year": 2012}, top_k=3)
        self.assertEqual([r["id"] for r in top], ["b" * 16])
        with self.assertRaises(ValueError):
            bm25.search("x", filters={"gold": 1})

    def test_rrf_uses_ranks_only(self):
        a, b, c = CHUNKS[0], CHUNKS[1], CHUNKS[2]
        fused = HybridRRF(Fixed("d", [a, b]), Fixed("l", [b, c]), candidates=5).search("q", top_k=3)
        self.assertEqual(fused[0]["id"], b["id"])          # 1/62 + 1/61 beats 1/61 and 1/62 alone
        self.assertEqual({r["id"] for r in fused}, {a["id"], b["id"], c["id"]})


class ContextTests(unittest.TestCase):
    def test_dedup_budget_and_part_expansion(self):
        plain = ContextBuilder(CHUNKS, budget=10_000).build([CHUNKS[2], CHUNKS[2], CHUNKS[0]])
        self.assertEqual(plain["context_ids"], ["c" * 16, "a" * 16])
        grown = ContextBuilder(CHUNKS, budget=10_000, expand_parts=True).build([CHUNKS[2]])
        self.assertEqual(grown["context_ids"], ["c" * 16, "d" * 16])
        self.assertEqual(grown["added_by_expansion"], ["d" * 16])
        tight = ContextBuilder(CHUNKS, budget=120).build(CHUNKS)
        self.assertLessEqual(len(tight["context"]), 120)
        self.assertTrue(tight["skipped_for_budget"])


class FakeLLM:
    def __init__(self, replies): self.replies, self.seen_tools = iter(replies), []
    def chat(self, messages, tools=None):
        self.seen_tools.append(bool(tools))
        return {"message": next(self.replies), "prompt_tokens": 10, "output_tokens": 5, "seconds": 0.01}


def search(q, year=None):
    args = {"query": q, **({"year": year} if year else {})}
    return {"role": "assistant", "content": "", "tool_calls": [{"function": {"name": "search_law", "arguments": args}}]}


class AgentTests(unittest.TestCase):
    def setUp(self):
        self.builder = ContextBuilder(CHUNKS, budget=5000)

    def test_answer_with_valid_citation_and_user_filter_wins(self):
        llm = FakeLLM([search("làm thêm", 2012), {"role": "assistant", "content": f"40 giờ [{'a' * 16}]"}])
        out = run_agent({"question": "q", "filter": {"year": 2019}}, llm, Fixed("r", CHUNKS), self.builder)
        self.assertEqual(out["status"], "answered")
        self.assertEqual(out["events"][0]["filter"], {"year": 2019})
        self.assertEqual(out["events"][0]["filter_source"], "user")

    def test_llm_call_limit_stops_endless_invalid_tool_calls(self):
        bad = {"role": "assistant", "content": "", "tool_calls": [{"function": {"name": "search_law", "arguments": {"query": ""}}}]}
        llm = FakeLLM([bad] * 50)
        out = run_agent({"question": "q"}, llm, Fixed("r", CHUNKS), self.builder, max_searches=2)
        self.assertEqual(out["status"], "abstain")
        self.assertEqual(out["usage"]["llm_calls"], 5)                     # max_searches + 3
        self.assertEqual(out["events"][-2]["event"], "llm_call_limit")

    def test_grouped_citations_are_parsed_and_checked(self):
        from src.agent import classify_answer, parse_citations
        a, b = "a" * 16, "b" * 16
        self.assertEqual(parse_citations(f"x [{a}, {b}] y [{a}]"), [a, b])
        self.assertEqual(classify_answer(f"x [{a}, {'f' * 16}]", [a])[0], "abstain")      # grouped invalid id caught
        self.assertEqual(classify_answer(f"x [{a}, {b}]", [a, b])[:2], ("answered", [a, b]))

    def test_inferred_only_ignores_user_filter(self):
        llm = FakeLLM([search("x", 2012), {"role": "assistant", "content": f"ok [{'b' * 16}]"}])
        out = run_agent({"question": "q", "filter": {"year": 2019}}, llm, Fixed("r", CHUNKS), self.builder,
                        filter_policy="inferred_only")
        self.assertEqual((out["events"][0]["filter"], out["events"][0]["filter_source"]), ({"year": 2012}, "inferred"))

    def test_inferred_filter_and_invalid_citation_abstains(self):
        llm = FakeLLM([search("x", 2012), {"role": "assistant", "content": "30 giờ [ffffffffffffffff]"}])
        out = run_agent({"question": "q"}, llm, Fixed("r", CHUNKS[:1]), self.builder)
        self.assertEqual(out["events"][0]["filter_source"], "inferred")
        self.assertEqual((out["status"], out["abstain_reason"]), ("abstain", "invalid_citations"))

    def test_search_limit_removes_tools_and_abstain_text(self):
        llm = FakeLLM([search("1"), search("2"),
                       {"role": "assistant", "content": "Không đủ bằng chứng trong Bộ luật Lao động 2012/2019 để trả lời."}])
        out = run_agent({"question": "q"}, llm, Fixed("r", CHUNKS), self.builder, max_searches=2)
        self.assertEqual(out["searches"], 2)
        self.assertEqual(llm.seen_tools, [True, True, False])
        self.assertEqual(out["status"], "abstain")

    def test_nudge_when_model_skips_search_and_errors_are_reported(self):
        llm = FakeLLM([{"role": "assistant", "content": "đoán"}, search("x"), {"role": "assistant", "content": f"ok [{'a' * 16}]"}])
        out = run_agent({"question": "q"}, llm, Fixed("r", CHUNKS), self.builder)
        self.assertEqual(out["events"][0]["event"], "nudge_search_first")
        class Broken:
            def search(self, *a, **k): raise ConnectionError("db down")
        err = run_agent({"question": "q"}, FakeLLM([search("x")]), Broken(), self.builder)
        self.assertEqual(err["status"], "error")
        self.assertIn("db down", err["error"])


class GuardTests(unittest.TestCase):
    def test_test_split_locked_without_selection(self):
        with tempfile.TemporaryDirectory() as d, mock.patch.object(config, "SELECTION_PATH", Path(d) / "selection.json"):
            with self.assertRaises(RuntimeError):
                guards.check_split_allowed("test", Path(d) / "out")
            guards.check_split_allowed("dev", Path(d) / "out")


if __name__ == "__main__":
    unittest.main()
