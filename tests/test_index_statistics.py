"""Tests for IndexStatistics."""
import unittest
from rag_evals.index.statistics import IndexStatistics

class TestIndexStatistics(unittest.TestCase):
    def test_stats(self):
        s = IndexStatistics()
        chunks = [
            {"text": "one two three", "source": "a.txt"},
            {"text": "four five six seven", "source": "b.txt"},
        ]
        rep = s.report(chunks)
        self.assertEqual(rep["chunk_statistics"]["count"], 2)
        self.assertEqual(rep["source_distribution"]["a.txt"], 1)
