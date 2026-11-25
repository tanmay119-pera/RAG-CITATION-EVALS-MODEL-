"""Tests for QueryRewriter."""
import unittest
from rag_evals.retrieval.query_rewriter import QueryRewriter

class TestQueryRewriter(unittest.TestCase):
    def test_acronym_expansion(self):
        rw = QueryRewriter.rewrite("Minimum CGPA for honors?")
        self.assertIn("cumulative grade point average", rw)
