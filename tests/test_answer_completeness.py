"""Tests for CompletenessScorer."""
import unittest
from rag_evals.eval.answer_completeness import CompletenessScorer

class TestCompleteness(unittest.TestCase):
    def test_fact_coverage(self):
        s = CompletenessScorer.score("Minimum attendance is 75% per semester.", ["75%", "semester", "penalty"])
        self.assertAlmostEqual(s, 0.6667, places=3)
