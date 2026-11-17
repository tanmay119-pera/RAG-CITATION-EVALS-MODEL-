"""Unit tests for multi-query expansion, MMR diversity, and context compression."""

import unittest
from rag_evals.retrieval.multi_query import MultiQueryGenerator
from rag_evals.retrieval.mmr import MMRReranker
from rag_evals.retrieval.compressor import ContextCompressor
from rag_evals.retrieval.hybrid import RetrievedChunk

class TestRetrievalAdvanced(unittest.TestCase):
    def test_multi_query(self):
        exp = MultiQueryGenerator.expand("What is the penalty for plagiarism?")
        self.assertGreaterEqual(len(exp), 2)
        self.assertIn("penalty", exp[0].lower())

    def test_mmr_reranker(self):
        c1 = RetrievedChunk("1", "Plagiarism violations code of conduct", 0.9, 1)
        c2 = RetrievedChunk("2", "Plagiarism violations code of conduct duplicate", 0.88, 2)
        c3 = RetrievedChunk("3", "Tuition fees deadline schedule", 0.75, 3)
        mmr = MMRReranker()
        selected = mmr.rerank([c1, c2, c3], top_n=2)
        self.assertEqual(selected[0].chunk_id, "1")
        # Due to redundancy between c1 and c2, c3 should be preferred for diversity
        self.assertEqual(selected[1].chunk_id, "3")

    def test_context_compressor(self):
        chunk = RetrievedChunk("c1", "Sentence one about campus. Sentence two mentions plagiarism penalties.", 0.8, 1)
        comp = ContextCompressor.compress_chunk("plagiarism", chunk)
        self.assertIn("plagiarism", comp.text)

if __name__ == "__main__":
    unittest.main()
