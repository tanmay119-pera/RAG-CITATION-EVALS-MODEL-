"""Tests for DiversityScorer."""
import unittest
from rag_evals.eval.diversity_metrics import DiversityScorer

class TestDiversity(unittest.TestCase):
    def test_diversity(self):
        ds = DiversityScorer()
        chunks = [{"text": "apple banana", "source": "s1"}, {"text": "cherry date", "source": "s2"}]
        r = ds.report(chunks)
        self.assertEqual(r["source_diversity"], 1.0)
        self.assertEqual(r["content_diversity"], 1.0)
