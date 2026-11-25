"""Tests for metric_thresholds."""
import unittest
from rag_evals.eval.metric_thresholds import passes_release_gates

class TestMetricThresholds(unittest.TestCase):
    def test_gate_pass_and_fail(self):
        self.assertTrue(passes_release_gates({"recall_at_5": 0.8, "mrr": 0.7, "faithfulness": 0.9, "citation_fidelity": 0.85}))
        self.assertFalse(passes_release_gates({"recall_at_5": 0.4, "mrr": 0.7, "faithfulness": 0.9, "citation_fidelity": 0.85}))
