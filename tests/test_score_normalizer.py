"""Tests for ScoreNormalizer."""
import unittest
from rag_evals.retrieval.score_normalizer import ScoreNormalizer

class TestScoreNormalizer(unittest.TestCase):
    def test_min_max(self):
        self.assertEqual(ScoreNormalizer.min_max([2.0, 6.0, 10.0]), [0.0, 0.5, 1.0])

    def test_z_score(self):
        zs = ScoreNormalizer.z_score([10.0, 10.0])
        self.assertEqual(zs, [0.0, 0.0])
