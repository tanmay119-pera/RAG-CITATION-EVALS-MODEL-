"""Unit tests for Citation Faithfulness Index."""

import unittest
from rag_evals.eval.cfi import CFIEvaluator

class TestCFI(unittest.TestCase):
    def test_cfi_perfect(self):
        score = CFIEvaluator.compute_cfi(1.0, 1.0)
        self.assertEqual(score, 1.0)

    def test_cfi_zero(self):
        score = CFIEvaluator.compute_cfi(0.0, 1.0)
        self.assertEqual(score, 0.0)

if __name__ == "__main__":
    unittest.main()
