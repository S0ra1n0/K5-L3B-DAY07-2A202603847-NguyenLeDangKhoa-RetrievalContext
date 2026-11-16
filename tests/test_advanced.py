"""Offline tests for the advanced pipeline (no model, no GPU, no network).

Covers the parts that are easy to get wrong: number parsing with source typos, table rows (wrapped labels,
en-dash minus), profile block-diagram pairing (rectangles + legend colours), hyphen joining in text chunks,
citation parsing / answer classification, context budget, the agent loop with a mock model, and the
run_bench guards (frozen benchmark, locked test). Regression checks read the committed extraction outputs.
"""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from advanced.rag import agent as A  # noqa: E402
from advanced.rag.chunks import _join, _split_paragraphs  # noqa: E402
from advanced.scripts import extract as X  # noqa: E402

PROC = ROOT / "advanced" / "data" / "processed"


class NumberAndTableTests(unittest.TestCase):
    def test_to_number_handles_source_typos_and_dashes(self):
        self.assertEqual(X.to_number("8.182.1"), 8182.1)   # printed with a separator typo in Table 1.1
        self.assertEqual(X.to_number("2,424.1"), 2424.1)
        self.assertEqual(X.to_number("–2.0"), -2.0)         # en dash minus as printed
        self.assertEqual(X.to_number("−0.4"), -0.4)         # unicode minus
        self.assertIsNone(X.to_number(".."))

    def test_table_1_1_rows(self):
        t = json.loads((PROC / "tables" / "tab_1_1.json").read_text(encoding="utf-8"))
        rows = {r["row"]: r for r in t["rows"]}
        self.assertEqual(len(t["rows"]), 13)
        self.assertIn("World Bank (IBRD and IDA)", rows)                  # label wrapped over two lines
        self.assertIn("IMF (Use of credit and SDR allocations)", rows)
        self.assertEqual(rows["World Bank (IBRD and IDA)"]["values"][-1], 498.7)
        self.assertEqual(rows["Debt stock"]["raw"][5], "8.182.1")          # kept as printed
        self.assertEqual(rows["Debt stock"]["values"][5], 8182.1)
        self.assertEqual(rows["Long-term PPG"]["section"], "Memorandum item")

    def test_table_1_2_negative_rows(self):
        t = json.loads((PROC / "tables" / "tab_1_2.json").read_text(encoding="utf-8"))
        rows = {r["row"]: r for r in t["rows"]}
        self.assertEqual(len(t["rows"]), 13)
        self.assertEqual(rows["Bonds"]["values"][7:9], [-2.0, -0.3])       # 2022, 2023
        self.assertEqual(rows["Short-term"]["values"][8], -11.0)


class FakePage:
    def __init__(self, words, rects):
        self._w, self.rects = words, rects

    def extract_words(self, **_):
        return self._w


def W(text, x0, top, size=7.4):
    return {"text": text, "x0": x0, "x1": x0 + 5 * len(text), "top": top, "bottom": top + size, "size": size}


def Rect(x0, top, w, h, col):
    return {"x0": x0, "x1": x0 + w, "top": top, "bottom": top + h, "width": w, "height": h, "non_stroking_color": col}


class ProfileBlockTests(unittest.TestCase):
    def test_pairs_labels_values_and_legend_by_colour(self):
        blue, light, tiny = (0.1, 0.6, 0.9), (0.6, 0.8, 0.9), (0.3, 0.7, 0.9)
        words = [W("BILATERAL", 300, 100), W("100", 550, 100, 8.5),
                 W("Japan", 306, 118), W("60", 306, 141, 8.0),              # labelled block
                 W("30", 520, 141, 7.6),                                     # narrow block: value only
                 W("Other", 495, 170, 7.2), W("bilateral", 520, 170, 7.2),   # legend label for the narrow block
                 W("Russia", 495, 185, 7.2), W("10", 540, 185, 7.2)]         # legend for a block too thin to draw
        rects = [Rect(300, 114, 200, 42, blue), Rect(510, 114, 40, 42, light),
                 Rect(485, 170, 6, 6, light), Rect(485, 185, 6, 6, tiny)]
        out, issues = X._parse_figure2(FakePage(words, rects), 90, 200)
        self.assertEqual(out["BILATERAL"]["items"], {"Japan": "60", "Other bilateral": "30", "Russia": "10"})
        self.assertEqual(issues, [])

    def test_sum_mismatch_is_reported(self):
        words = [W("BILATERAL", 300, 100), W("100", 550, 100, 8.5), W("Japan", 306, 118), W("60", 306, 141, 8.0)]
        out, issues = X._parse_figure2(FakePage(words, [Rect(300, 114, 200, 42, (0.1, 0.6, 0.9))]), 90, 200)
        self.assertTrue(any("items sum 60 != total 100" in i for i in issues))

    def test_viet_nam_profile_regression(self):
        prof = {json.loads(l)["entity"]: json.loads(l) for l in (PROC / "profiles.jsonl").read_text(encoding="utf-8").splitlines()}
        vn = prof["VIET NAM"]
        self.assertEqual(vn["total_external_debt_2025"], "131,777")
        self.assertEqual(vn["figure2"]["BILATERAL"]["items"],
                         {"Japan": "10,155", "Russian Federation": "1,392", "Other bilateral": "2,873"})
        self.assertEqual(prof["KENYA"]["figure2"]["MULTILATERAL"]["items"]["AfDB"], "4,413")
        self.assertEqual(sum(1 for p in prof.values() if not p["issues"]), 120)


class ChunkTextTests(unittest.TestCase):
    def test_join_keeps_suspended_hyphen(self):
        self.assertEqual(_join(["IDA-", "eligible countries"]), "IDA-eligible countries")
        self.assertEqual(_join(["of low-", "and middle-income countries"]), "of low- and middle-income countries")

    def test_split_respects_max_chars(self):
        text = "\n".join(["A sentence of moderate length that keeps going for a while."] * 60)
        parts = _split_paragraphs(text)
        self.assertTrue(all(len(p) <= 1200 for p in parts))
        self.assertGreater(len(parts), 1)


class CitationTests(unittest.TestCase):
    def test_parse_citations_single_grouped_and_piped(self):
        ans = "A [p028-table-1]. B [p030-figure-1, p260-profile]. C [p019-text-2 | p020-text-1] [p088-page]."
        self.assertEqual(A.parse_citations(ans), ["p028-table-1", "p030-figure-1", "p260-profile",
                                                  "p019-text-2", "p020-text-1", "p088-page"])

    def test_classify(self):
        ctx = ["p028-table-1", "p260-profile"]
        self.assertEqual(A.classify_answer("x [p028-table-1]", ctx)[0], "answered")
        self.assertEqual(A.classify_answer("x [p999-text-1]", ctx)[2], "invalid_citations")
        self.assertEqual(A.classify_answer("x without citation", ctx)[2], "no_citation")
        self.assertEqual(A.classify_answer("Not enough evidence in the International Debt Report 2026 to answer "
                                           "this question.", ctx)[2], "says_not_enough_evidence")

    def test_context_budget_and_dedup(self):
        c = lambda i, n: {"id": i, "kind": "text", "page": 1, "page_label": "1", "text": "x" * n, "metadata": {}}
        out = A.Context(budget=300).build([c("p001-text-1", 100), c("p001-text-1", 100), c("p001-text-2", 500),
                                           c("p001-text-3", 50)])
        self.assertEqual(out["context_ids"], ["p001-text-1", "p001-text-3"])
        self.assertEqual(out["skipped_for_budget"], ["p001-text-2"])


class MockLLM:
    def __init__(self, messages):
        self.script, self.seen = list(messages), []

    def chat(self, messages, tools):
        self.seen.append((list(messages), tools))
        return {"message": self.script.pop(0), "prompt_tokens": 1, "output_tokens": 1, "seconds": 0.0}


class MockRetriever:
    name = "mock"

    def search(self, query, *, filters=None, top_k=3):
        return [{"id": "p028-table-1", "kind": "table", "page": 28, "page_label": "4", "text": "Bonds 2,364.4",
                 "metadata": {"region": "tab_1_1", "bbox": [40, 106, 576, 458], "title": "Table 1.1"},
                 "score": 1.0, "rank": 1}]


def tool(name, **args):
    return {"role": "assistant", "content": "", "tool_calls": [{"function": {"name": name, "arguments": args}}]}


class AgentLoopTests(unittest.TestCase):
    def test_search_then_cited_answer(self):
        llm = MockLLM([tool("search_report", query="bonds 2025"), {"content": "US$2,364.4 billion [p028-table-1]."}])
        out = A.run_agent("q", llm, MockRetriever(), A.Context())
        self.assertEqual(out["status"], "answered")
        self.assertEqual(out["cited_regions"][0]["region"], "tab_1_1")
        self.assertEqual(out["cited_regions"][0]["pdf_page"], 28)
        self.assertNotIn("view_page", json.dumps(llm.seen[0][1]))   # tool only offered when enabled

    def test_view_page_refused_for_page_not_returned(self):
        llm = MockLLM([tool("search_report", query="bonds"), tool("view_page", pdf_page=99, question="value?"),
                       {"content": "Not enough evidence in the International Debt Report 2026 to answer this question."}])
        with mock.patch.object(X, "ollama_vision", side_effect=AssertionError("must not be called")):
            out = A.run_agent("q", llm, MockRetriever(), A.Context(), view_page=True)
        self.assertTrue(any(e["event"] == "invalid_view" for e in out["events"]))
        self.assertEqual(out["status"], "abstain")

    def test_citation_repair_turn(self):
        llm = MockLLM([tool("search_report", query="bonds"), {"content": "US$2,364.4 billion."},
                       {"content": "US$2,364.4 billion [p028-table-1-row07]."}])
        class RowRetriever(MockRetriever):
            def search(self, query, *, filters=None, top_k=3):
                r = super().search(query)[0]
                return [{**r, "id": "p028-table-1-row07", "kind": "table_row"}]
        out = A.run_agent("q", llm, RowRetriever(), A.Context(), citation_retry=True)
        self.assertEqual(out["status"], "answered")
        self.assertEqual(out["citations"], ["p028-table-1-row07"])
        self.assertTrue(any(e["event"] == "citation_retry" for e in out["events"]))
        # without the option the first uncited answer stands (abstain by rule)
        llm2 = MockLLM([tool("search_report", query="bonds"), {"content": "US$2,364.4 billion."}])
        self.assertEqual(A.run_agent("q", llm2, MockRetriever(), A.Context())["abstain_reason"], "no_citation")

    def test_model_error_is_recorded_not_hidden(self):
        class Boom:
            def chat(self, *_):
                raise RuntimeError("ollama down")
        out = A.run_agent("q", Boom(), MockRetriever(), A.Context())
        self.assertEqual(out["status"], "error")
        self.assertIn("ollama down", out["error"])


class RunBenchGuardTests(unittest.TestCase):
    def setUp(self):
        from advanced.scripts import run_bench
        self.rb = run_bench

    def test_refuses_uncommitted_benchmark(self):
        with mock.patch.object(self.rb, "git", side_effect=lambda *a: "" if a[0] == "ls-files" else ""):
            with self.assertRaises(SystemExit):
                self.rb.guard("dev", "x")

    def test_refuses_dirty_benchmark(self):
        fake = lambda *a: "advanced/benchmark/questions.json\n" if a[0] == "ls-files" else " M questions.json"
        with mock.patch.object(self.rb, "git", side_effect=fake):
            with self.assertRaises(SystemExit):
                self.rb.guard("dev", "x")

    def test_test_split_locked_and_run_once(self):
        clean = lambda *a: "advanced/benchmark/questions.json\n" if a[0] == "ls-files" else ""
        with tempfile.TemporaryDirectory() as d, mock.patch.object(self.rb, "git", side_effect=clean), \
                mock.patch.object(self.rb, "RESULTS", Path(d)), mock.patch.object(self.rb, "RUNS", Path(d) / "runs"):
            self.rb.guard("dev", "x")                       # dev allowed when frozen
            with self.assertRaises(SystemExit):
                self.rb.guard("test", "x")                  # no selection.json yet
            (Path(d) / "selection.json").write_text("{}")
            self.rb.guard("test", "x")                      # allowed once
            (Path(d) / "runs").mkdir()
            (Path(d) / "runs" / "x_test.jsonl").write_text("")
            with self.assertRaises(SystemExit):
                self.rb.guard("test", "x")                  # never twice


if __name__ == "__main__":
    unittest.main()
