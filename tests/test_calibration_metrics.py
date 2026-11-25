"""Tests for CalibrationEvaluator."""
import unittest
from rag_evals.eval.calibration_metrics import CalibrationEvaluator

class TestCalibration(unittest.TestCase):
    def test_perfect_calibration(self):
        self.assertEqual(CalibrationEvaluator.brier_score([1.0, 0.0], [1, 0]), 0.0)
        self.assertEqual(CalibrationEvaluator.expected_calibration_error([1.0, 0.0], [1, 0]), 0.0)
