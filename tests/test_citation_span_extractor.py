"""Tests for CitationSpanExtractor."""
import unittest
from rag_evals.generation.citation_highlighter import CitationSpanExtractor

class TestCitationSpanExtractor(unittest.TestCase):
    def test_extracts_sentence_spans(self):
        spans = CitationSpanExtractor.extract("Minimum attendance is 75% [c1]. Unsupported sentence.")
        self.assertEqual(spans[0]["citations"], ["c1"])
        self.assertTrue(spans[0]["grounded"])
        self.assertFalse(spans[1]["grounded"])
