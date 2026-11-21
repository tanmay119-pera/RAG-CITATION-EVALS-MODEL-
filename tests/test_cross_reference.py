"""Tests for CrossReferenceLinker."""
import unittest
from rag_evals.ingest.cross_reference import CrossReferenceLinker

class TestCrossReference(unittest.TestCase):
    def test_links(self):
        linker = CrossReferenceLinker(min_shared=1)
        chunks = [
            {"chunk_id": "c1", "text": "Academic Council approved the calendar."},
            {"chunk_id": "c2", "text": "The Academic Council meets every month."},
        ]
        links = linker.link(chunks)
        self.assertIn("c1", links)
        self.assertIn("c2", links["c1"])
