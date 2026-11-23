"""Tests for ContextualSentenceCompressor."""
import unittest
from rag_evals.retrieval.contextual_compression import ContextualSentenceCompressor

class TestContextualCompressor(unittest.TestCase):
    def test_compression(self):
        comp = ContextualSentenceCompressor()
        text = "Students must maintain 75% attendance. The weather in July is usually humid. Debarment applies otherwise."
        res = comp.compress_chunk("attendance rules", text)
        self.assertIn("attendance", res)
        self.assertNotIn("weather", res)
