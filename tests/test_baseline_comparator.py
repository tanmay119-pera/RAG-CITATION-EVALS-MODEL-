"""Tests for BaselineDeltaTracker."""
import unittest
from rag_evals.eval.baseline_comparator import BaselineDeltaTracker

class TestBaselineDelta(unittest.TestCase):
    def test_delta_calculation(self):
        d = BaselineDeltaTracker.compute_deltas({"mrr": 0.70, "recall": 0.80}, {"mrr": 0.78, "recall": 0.79})
        self.assertEqual(d["mrr"], 0.08)
        self.assertEqual(d["recall"], -0.01)
