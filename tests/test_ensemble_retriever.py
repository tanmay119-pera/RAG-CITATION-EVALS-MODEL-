"""Tests for EnsembleRetriever."""
import unittest
from rag_evals.retrieval.ensemble_retriever import EnsembleRetriever

class TestEnsembleRetriever(unittest.TestCase):
    def test_fused_results(self):
        r1 = lambda q, k: [{"chunk_id": "c1", "score": 0.8}, {"chunk_id": "c2", "score": 0.4}]
        r2 = lambda q, k: [{"chunk_id": "c2", "score": 0.9}, {"chunk_id": "c1", "score": 0.3}]
        ens = EnsembleRetriever([(r1, 0.5), (r2, 0.5)])
        res = ens.retrieve("query", top_k=2)
        self.assertEqual(len(res), 2)
        self.assertEqual(res[0]["chunk_id"], "c2") # (0.4*0.5 + 0.9*0.5) = 0.65 vs (0.8*0.5 + 0.3*0.5) = 0.55
