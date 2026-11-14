"""Tests for AblationTableFormatter."""
import unittest
from rag_evals.eval.ablation_formatter import AblationTableFormatter

class TestAblationFormatter(unittest.TestCase):
    def test_markdown_rendering(self):
        md = AblationTableFormatter.to_markdown([{"mode": "hybrid", "recall@5": 0.91}])
        self.assertIn("| mode | recall@5 |", md)
        self.assertIn("| hybrid | 0.91 |", md)
