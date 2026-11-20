"""Tests for EmbeddingDriftMonitor."""
import unittest
from rag_evals.observability.drift_monitor import EmbeddingDriftMonitor

class TestDriftMonitor(unittest.TestCase):
    def test_no_drift(self):
        dm = EmbeddingDriftMonitor()
        b = [[1.0, 0.0], [0.0, 1.0]]
        c = [[0.95, 0.05], [0.05, 0.95]]
        res = dm.check(b, c)
        self.assertFalse(res.is_drifted)

    def test_drift_detected(self):
        dm = EmbeddingDriftMonitor(mean_threshold=0.01)
        res = dm.check([[0.1, 0.1]], [[10.0, 10.0]])
        self.assertTrue(res.is_drifted)
