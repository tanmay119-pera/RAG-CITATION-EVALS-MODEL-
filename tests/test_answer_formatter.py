"""Tests for format_with_references."""
import unittest
from rag_evals.generation.answer_formatter import format_with_references

class TestAnswerFormatter(unittest.TestCase):
    def test_appends_sources(self):
        out = format_with_references("Rule applies [c1].", [{"chunk_id": "c1", "source": "handbook.pdf"}])
        self.assertIn("[c1] handbook.pdf", out)
