"""Tests for RelevanceFeedback."""
import unittest
from rag_evals.retrieval.relevance_feedback import RelevanceFeedback

class TestRelevanceFeedback(unittest.TestCase):
    def test_feedback_boost(self):
        rf = RelevanceFeedback()
        rf.record("q", "c1", True)
        rf.record("q", "c2", False)
        res = [{"chunk_id": "c2", "score": 0.5}, {"chunk_id": "c1", "score": 0.4}]
        boosted = rf.apply_boosts(res)
        self.assertEqual(boosted[0]["chunk_id"], "c1")
