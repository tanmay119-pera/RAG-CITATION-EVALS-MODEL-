"""Tests for CitationGraphView."""
import unittest
from rag_evals.ui.citation_graph_view import CitationGraphView

class TestCitationGraphView(unittest.TestCase):
    def test_ascii_view(self):
        cgv = CitationGraphView()
        out = cgv.render_ascii("What is attendance?", ["c1", "c2"], {"c1": "Attendance Policy"})
        self.assertIn("[c1] Attendance Policy", out)
        self.assertIn("[c2]", out)
