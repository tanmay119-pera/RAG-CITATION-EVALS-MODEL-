"""Unit tests for hybrid retrieval, RRF, and reranking."""

import unittest
from rag_evals.retrieval.hybrid import HybridRetriever, RetrievedChunk
from rag_evals.retrieval.reranker import CrossEncoderReranker

class TestRetrieval(unittest.TestCase):
    def test_hybrid_retrieval(self):
        retriever = HybridRetriever()
        results = retriever.retrieve("academic integrity plagiarism penalties", top_k=3, mode="hybrid")
        self.assertGreaterEqual(len(results), 1)
        self.assertIn("chunk_id", results[0].__dict__)

    def test_reranker(self):
        chunks = [
            RetrievedChunk("c1", "Tuition fees and refund policy.", score=0.5, rank=1),
            RetrievedChunk("c2", "Academic integrity code: penalties for plagiarism violations.", score=0.4, rank=2)
        ]
        reranker = CrossEncoderReranker(top_n=2)
        reranked = reranker.rerank("What are penalties for plagiarism?", chunks)
        self.assertEqual(reranked[0].chunk_id, "c2")

if __name__ == "__main__":
    unittest.main()
