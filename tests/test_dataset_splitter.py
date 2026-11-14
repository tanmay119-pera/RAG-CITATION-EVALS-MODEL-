"""Tests for StratifiedSplitter."""
import unittest
from rag_evals.eval.dataset_splitter import StratifiedSplitter

class TestStratifiedSplitter(unittest.TestCase):
    def test_preserves_unanswerable_balance(self):
        cases = [{"id": i, "is_unanswerable": i >= 8} for i in range(10)]
        dev, test = StratifiedSplitter.split(cases, holdout_ratio=0.25)
        self.assertTrue(any(c["is_unanswerable"] for c in test))
        self.assertEqual(len(dev) + len(test), 10)
