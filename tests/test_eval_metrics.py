"""Unit tests for faithfulness judge and citation metrics."""

import unittest
from rag_evals.eval.faithfulness import FaithfulnessJudge
from rag_evals.eval.citation_metrics import CitationMetrics

class TestEvalMetrics(unittest.TestCase):
    def test_faithfulness_supported(self):
        ctx = ["A course repetition is allowed at most twice for grades of C- or lower."]
        ans = "Students may repeat a course at most twice [chunk_1]."
        score = FaithfulnessJudge.evaluate_faithfulness(ans, ctx)
        self.assertGreaterEqual(score, 0.8)

    def test_citation_metrics(self):
        meta = {"c1": {"text": "Clause 1.2 penalties for minor violations.", "section_title": "Integrity"}}
        res = CitationMetrics.compute("Some answer [c1]", ["c1"], "Clause 1.2", meta)
        self.assertEqual(res["citation_precision"], 1.0)

if __name__ == "__main__":
    unittest.main()
