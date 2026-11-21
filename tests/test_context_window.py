"""Tests for ContextWindowManager."""
import unittest
from rag_evals.generation.context_window import ContextWindowManager

class TestContextWindow(unittest.TestCase):
    def test_pack(self):
        cwm = ContextWindowManager(max_tokens=100, reserved_tokens=20)
        chunks = [{"chunk_id": "c1", "text": "short"}, {"chunk_id": "c2", "text": "also short"}]
        inc, exc = cwm.pack(chunks)
        self.assertEqual(len(inc), 2)
        self.assertEqual(len(exc), 0)
        ctx = cwm.format_context(inc)
        self.assertIn("[c1]", ctx)
