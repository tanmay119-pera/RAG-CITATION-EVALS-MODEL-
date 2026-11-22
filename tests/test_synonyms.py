"""Tests for SynonymExpander."""
import unittest
from rag_evals.retrieval.synonyms import SynonymExpander

class TestSynonyms(unittest.TestCase):
    def test_expand(self):
        se = SynonymExpander()
        res = se.expand("final exam dates")
        self.assertTrue(any("examination" in r for r in res))
