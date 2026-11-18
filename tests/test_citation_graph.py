"""Unit tests for citation graph visualizer."""

import unittest
from rag_evals.observability.citation_graph import CitationGraphVisualizer

class TestCitationGraph(unittest.TestCase):
    def test_generate_mermaid(self):
        chunks = [{"chunk_id": "c1", "section_title": "Integrity"}]
        graph = CitationGraphVisualizer.generate_mermaid_graph("What is plagiarism?", chunks)
        self.assertIn("flowchart LR", graph)
        self.assertIn("[c1]", graph)

if __name__ == "__main__":
    unittest.main()
