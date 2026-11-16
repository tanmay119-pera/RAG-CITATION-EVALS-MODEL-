"""Unit tests for ablation modules."""

import unittest
from rag_evals.ablations.chunk_ablation import run_chunk_ablation
from rag_evals.ablations.retrieval_ablation import run_retrieval_ablation
from rag_evals.ablations.reranker_ablation import run_reranker_ablation

class TestAblations(unittest.TestCase):
    def test_chunk_ablation(self):
        res = run_chunk_ablation(chunk_sizes=[300, 450])
        self.assertEqual(len(res), 2)
        self.assertIn("hit_at_1", res[0])

    def test_retrieval_ablation(self):
        res = run_retrieval_ablation()
        self.assertEqual(len(res), 3)

    def test_reranker_ablation(self):
        res = run_reranker_ablation()
        self.assertEqual(len(res), 2)

if __name__ == "__main__":
    unittest.main()
