"""Tests for PageOffsetMapper."""
import unittest
from rag_evals.ingest.page_mapper import PageOffsetMapper

class TestPageMapper(unittest.TestCase):
    def test_offset_resolution(self):
        pm = PageOffsetMapper([100, 150, 200])
        self.assertEqual(pm.page_for_offset(50), 1)
        self.assertEqual(pm.page_for_offset(120), 2)
        self.assertEqual(pm.page_for_offset(300), 3)
