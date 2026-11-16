"""Offline checks for the Day 6 adapter, gold hiding and the hit/context definitions."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.data_io import convert_chunk, convert_day6_question, load_benchmark, public_view  # noqa: E402
from src.metrics import chunk_hit, context_has_evidence, first_hit_rank  # noqa: E402

GOLD = [{"source_id": "blld-2019", "page": 14, "article": 35, "evidence": ["không cần báo trước", "trả lương không đúng thời hạn"]},
        {"source_id": "blld-2012", "page": 12, "article": 37, "evidence": ["báo trước ít nhất 45 ngày"]}]


def chunk(cid, doc, pages, text):
    return {"id": cid, "source_id": doc, "page": pages[0], "pages": pages, "text": text, "metadata": {}}


class MetricTests(unittest.TestCase):
    def test_hit_needs_every_quote_right_source_and_page(self):
        full = chunk("a", "blld-2019", [13, 14], "... không cần  báo trước ... trả lương không đúng thời hạn")
        self.assertTrue(chunk_hit(full, GOLD))                      # page 14 in pages, whitespace collapsed
        self.assertFalse(chunk_hit(chunk("b", "blld-2019", [14], "không cần báo trước"), GOLD))
        self.assertFalse(chunk_hit(chunk("c", "blld-2019", [15], full["text"]), GOLD))
        self.assertFalse(chunk_hit(chunk("d", "blld-2012", [14], full["text"]), GOLD))
        self.assertTrue(chunk_hit(chunk("e", "blld-2012", [12], "phải báo trước ít nhất 45 ngày"), GOLD))  # alternative gold

    def test_context_allows_quotes_from_two_parts(self):
        p1 = chunk("p1", "blld-2019", [14], "không cần báo trước")
        p2 = chunk("p2", "blld-2019", [14], "trả lương không đúng thời hạn")
        self.assertTrue(context_has_evidence([p1, p2], GOLD))
        self.assertFalse(context_has_evidence([p1], GOLD))
        self.assertEqual(first_hit_rank([p1, p2], GOLD), None)


class DataTests(unittest.TestCase):
    def test_convert_day6_question_keeps_all_golds(self):
        q = {"id": "q08", "split": "test", "type": "x", "question": "Theo 2019?", "filter": {"year": 2019},
             "expected_answer": "A", "gold_source_id": "blld-2019", "gold_page": 14, "gold_article": 35,
             "evidence_quote": ["a", "b"], "alternative_gold": [{"source_id": "blld-2012", "page": 12, "article": 37, "evidence_quote": ["c"]}]}
        out = convert_day6_question(q, split="dev")
        self.assertEqual((out["split"], out["origin"]), ("dev", "day6-test"))
        self.assertEqual([g["evidence"] for g in out["gold"]], [["a", "b"], ["c"]])

    def test_convert_chunk(self):
        raw = {"chunk_id": "x", "document_id": "blld-2019", "source": "s.pdf", "page": 8, "text": "t",
               "metadata": {"pages": [8, 9], "year": 2019, "article": 20}}
        self.assertEqual(convert_chunk(raw)["pages"], [8, 9])

    def test_public_view_hides_gold_for_every_benchmark_question(self):
        secret = ("gold", "expected_answer", "absence_reason", "absence_check", "answerable", "split", "type", "origin")
        for q in load_benchmark():
            view = public_view(q)
            self.assertFalse(set(secret) & set(view), q["id"])
            self.assertEqual(view["question"], q["question"])


if __name__ == "__main__":
    unittest.main()
