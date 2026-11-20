"""Tests for AnswerComparator."""
import unittest
from rag_evals.eval.answer_comparator import AnswerComparator

class TestAnswerComparator(unittest.TestCase):
    def setUp(self):
        self.cmp = AnswerComparator()

    def test_equivalent(self):
        res = self.cmp.compare("The sky is blue", ["c1"], "The sky is blue.", ["c1"])
        self.assertEqual(res.verdict, "equivalent")
        self.assertGreater(res.similarity, 0.8)

    def test_shared_citations(self):
        res = self.cmp.compare("A", ["c1", "c2"], "B", ["c2", "c3"])
        self.assertEqual(res.shared_citations, ["c2"])
        self.assertEqual(res.only_a, ["c1"])
        self.assertEqual(res.only_b, ["c3"])
