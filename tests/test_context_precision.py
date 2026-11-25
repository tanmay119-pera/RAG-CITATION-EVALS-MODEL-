"""Tests for ContextPrecisionEvaluator."""
import unittest
from rag_evals.eval.context_precision import ContextPrecisionEvaluator

class TestContextPrecision(unittest.TestCase):
    def test_average_precision(self):
        ap = ContextPrecisionEvaluator.average_precision(["c1", "c2", "c3"], {"c1", "c3"})
        # (1/1 + 2/3) / 2 = 0.8333
        self.assertAlmostEqual(ap, 0.8333, places=3)
