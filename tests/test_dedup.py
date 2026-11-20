"""Tests for ChunkDeduplicator."""
import unittest
from rag_evals.ingest.dedup import ChunkDeduplicator

class TestChunkDedup(unittest.TestCase):
    def setUp(self):
        self.dd = ChunkDeduplicator()

    def test_exact(self):
        chunks = [{"text": "alpha"}, {"text": "beta"}, {"text": "alpha"}]
        uniq, dupes = self.dd.exact_dedup(chunks)
        self.assertEqual(len(uniq), 2)
        self.assertEqual(len(dupes), 1)

    def test_fuzzy(self):
        chunks = [{"text": "quick brown fox jumps"}, {"text": "quick brown fox jump"}]
        uniq, dupes = self.dd.fuzzy_dedup(chunks)
        self.assertEqual(len(uniq), 1)
        self.assertEqual(len(dupes), 1)
