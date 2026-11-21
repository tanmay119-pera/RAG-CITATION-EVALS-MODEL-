"""Tests for QueryComplexityEstimator."""
import unittest
from rag_evals.retrieval.complexity import QueryComplexityEstimator

class TestComplexity(unittest.TestCase):
    def test_complexity(self):
        qce = QueryComplexityEstimator()
        s1 = qce.estimate("What is CGPA?")
        self.assertEqual(s1["score"], 1)
        s2 = qce.estimate("Compare the difference between grading and pass rules in semester 1")
        self.assertGreater(s2["score"], 1)
