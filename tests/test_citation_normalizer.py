"""Tests for CitationNormalizer."""
import unittest
from rag_evals.generation.citation_normalizer import CitationNormalizer

class TestCitationNormalizer(unittest.TestCase):
    def test_normalize_syntax(self):
        raw = "Attendance is 75% [chunk: rule_p1_c0] and strict [ rule_p1_c1 ]."
        norm = CitationNormalizer.normalize(raw)
        self.assertEqual(norm, "Attendance is 75% [rule_p1_c0] and strict [rule_p1_c1].")
