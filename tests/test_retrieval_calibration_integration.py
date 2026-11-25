"""Integration test linking QueryRewriter, RRFTuner, and ContextPrecisionEvaluator."""
import unittest
from rag_evals.retrieval import QueryRewriter, RRFTuner
from rag_evals.eval.context_precision import ContextPrecisionEvaluator

class TestRetrievalCalibrationIntegration(unittest.TestCase):
    def test_rewrite_fuse_eval(self):
        q = QueryRewriter.rewrite("Check SGPA calculation")
        self.assertIn("semester grade point average", q)
        fused = RRFTuner.fuse([["c2", "c1"], ["c1", "c3"]], k=60)
        ap = ContextPrecisionEvaluator.average_precision(fused, {"c1"})
        self.assertEqual(ap, 1.0)
