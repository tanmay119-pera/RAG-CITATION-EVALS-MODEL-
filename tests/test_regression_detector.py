"""Tests for RegressionDetector."""
import unittest
from rag_evals.eval.regression_detector import RegressionDetector

class TestRegressionDetector(unittest.TestCase):
    def test_regression_detection(self):
        rd = RegressionDetector(tolerance_pct=0.10)
        baseline = {"recall": 0.80, "mrr": 0.75}
        current = {"recall": 0.65, "mrr": 0.74} # 18.75% drop in recall
        alerts = rd.evaluate(baseline, current)
        self.assertEqual(len(alerts), 1)
        self.assertEqual(alerts[0].metric, "recall")
