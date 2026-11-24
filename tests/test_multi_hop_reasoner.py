"""Tests for MultiHopReasoner."""
import unittest
from rag_evals.generation.multi_hop_reasoner import MultiHopReasoner

class TestMultiHopReasoner(unittest.TestCase):
    def test_multi_hop_flow(self):
        ret = lambda q: [{"chunk_id": f"c_{len(q)}", "text": "evidence"}]
        gen = lambda q, chunks: f"Answer to {q[:10]} with {len(chunks)} chunks"
        mhr = MultiHopReasoner(ret, gen)
        res = mhr.answer_multi_hop("Complex academic query?", hops=2)
        self.assertEqual(len(res["steps"]), 2)
        self.assertGreater(res["total_chunks_consulted"], 0)
