"""Tests for BatchComparator."""
import unittest
from rag_evals.eval.batch_comparator import BatchComparator, EvalSummary

class TestBatchComparator(unittest.TestCase):
    def test_rank(self):
        bc = BatchComparator()
        bc.add_run(EvalSummary("baseline", 0.6, 0.5, 0.7, 0.65))
        bc.add_run(EvalSummary("hybrid", 0.85, 0.8, 0.9, 0.88))
        ranked = bc.rank_by("cfi")
        self.assertEqual(ranked[0].config_name, "hybrid")
