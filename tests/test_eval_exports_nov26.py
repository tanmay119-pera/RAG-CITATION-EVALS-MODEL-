"""Verify updated rag_evals.eval package exports."""
import unittest
from rag_evals.eval import CalibrationEvaluator, ContextPrecisionEvaluator, GoldenSetAuditor

class TestEvalExports(unittest.TestCase):
    def test_exports_callable(self):
        self.assertIsNotNone(CalibrationEvaluator)
        self.assertIsNotNone(ContextPrecisionEvaluator)
        self.assertIsNotNone(GoldenSetAuditor)
