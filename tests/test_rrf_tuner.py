"""Tests for RRFTuner."""
import unittest
from rag_evals.retrieval.reciprocal_fusion_tuner import RRFTuner

class TestRRFTuner(unittest.TestCase):
    def test_fusion_ranks_overlap_highest(self):
        fused = RRFTuner.fuse([["c1", "c2"], ["c2", "c3"]], k=60)
        self.assertEqual(fused[0], "c2")
