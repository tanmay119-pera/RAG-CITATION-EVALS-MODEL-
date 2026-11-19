"""Unit tests for confidence scorer and feedback collector."""

import unittest
import tempfile
from pathlib import Path
from rag_evals.generation.confidence import ConfidenceScorer
from rag_evals.generation.verifier import VerificationResult
from rag_evals.retrieval.hybrid import RetrievedChunk
from rag_evals.observability.feedback import FeedbackCollector

class TestConfidence(unittest.TestCase):
    def test_confidence_valid(self):
        chunks = [RetrievedChunk("c1", "text", 0.9, 1)]
        v_res = VerificationResult(is_valid=True, cited_ids=["c1"], valid_ids=["c1"], invalid_ids=[])
        score = ConfidenceScorer.calculate(chunks, v_res, is_refusal=False)
        self.assertGreaterEqual(score, 0.7)

    def test_feedback_collector(self):
        with tempfile.TemporaryDirectory() as tmp:
            fp = Path(tmp) / "feedback.jsonl"
            collector = FeedbackCollector(log_path=fp)
            collector.log_feedback("query", "answer", True, "Great citation!")
            self.assertTrue(fp.exists())

if __name__ == "__main__":
    unittest.main()
