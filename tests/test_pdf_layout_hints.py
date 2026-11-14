"""Tests for LayoutHintExtractor."""
import unittest
from rag_evals.ingest.pdf_layout_hints import LayoutHintExtractor

class TestLayoutHints(unittest.TestCase):
    def test_headings_and_bullets(self):
        self.assertTrue(LayoutHintExtractor.is_heading("Section 4.1 Attendance"))
        self.assertTrue(LayoutHintExtractor.is_heading("EXAMINATION RULES"))
        self.assertTrue(LayoutHintExtractor.is_bullet("- Minimum 75% attendance"))
