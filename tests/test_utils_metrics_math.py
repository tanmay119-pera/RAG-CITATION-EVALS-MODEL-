"""Tests for metrics_math."""
import unittest
from rag_evals.utils.metrics_math import cosine_similarity, reciprocal_rank

class TestMetricsMath(unittest.TestCase):
    def test_cosine_similarity(self):
        self.assertAlmostEqual(cosine_similarity([1.0, 0.0], [1.0, 0.0]), 1.0)
        self.assertAlmostEqual(cosine_similarity([1.0, 0.0], [0.0, 1.0]), 0.0)

    def test_reciprocal_rank(self):
        self.assertAlmostEqual(reciprocal_rank(["a", "b", "c"], {"b"}), 0.5)
        self.assertEqual(reciprocal_rank(["a", "b"], {"z"}), 0.0)
