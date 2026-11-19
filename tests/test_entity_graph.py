"""Unit tests for knowledge graph extraction and graph retrieval."""

import unittest
from rag_evals.index.entity_graph import EntityGraph
from rag_evals.retrieval.hybrid import HybridRetriever
from rag_evals.retrieval.graph_retriever import GraphEnhancedRetriever

class TestEntityGraph(unittest.TestCase):
    def test_entity_extraction(self):
        graph = EntityGraph()
        text = "Under Clause 1.2, evidence is submitted to the Departmental Ethics Board."
        graph.extract_and_add("chunk_1", text)
        chunks = graph.get_related_chunks("Clause 1.2")
        self.assertIn("chunk_1", chunks)
        board_chunks = graph.get_related_chunks("Departmental Ethics Board")
        self.assertIn("chunk_1", board_chunks)

if __name__ == "__main__":
    unittest.main()
