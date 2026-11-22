"""Tests for LanguageDetector."""
import unittest
from rag_evals.ingest.language_detector import LanguageDetector

class TestLanguageDetector(unittest.TestCase):
    def test_detect(self):
        ld = LanguageDetector()
        res = ld.detect("This is an English test sentence.")
        self.assertEqual(res["script"], "latin")
        self.assertEqual(res["language"], "en")
