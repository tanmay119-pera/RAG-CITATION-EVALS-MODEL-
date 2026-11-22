"""Tests for ChunkQualityScorer."""
import unittest
from rag_evals.eval.chunk_quality import ChunkQualityScorer

class TestChunkQuality(unittest.TestCase):
    def test_scoring(self):
        cqs = ChunkQualityScorer()
        chunk = {"chunk_id": "c1", "text": "The quick brown fox jumps over the lazy dog.", "source": "s.txt"}
        res = cqs.score(chunk)
        self.assertGreater(res["overall"], 0.4)
