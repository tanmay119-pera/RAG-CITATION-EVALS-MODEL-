"""Unit tests for self-critique loop."""

import unittest
from rag_evals.generation.self_critique import SelfCritiqueAgent
from rag_evals.retrieval.hybrid import RetrievedChunk

class TestSelfCritique(unittest.TestCase):
    def test_repair_invalid_id(self):
        chunks = [RetrievedChunk("c1", "Evidence text", 0.9, 1)]
        bad_answer = "Policy requires approval [c1] but this is false [c_hallucinated]."
        repaired, was_clean = SelfCritiqueAgent.critique_and_repair(bad_answer, chunks)
        self.assertFalse(was_clean)
        self.assertNotIn("[c_hallucinated]", repaired)
        self.assertIn("[c1]", repaired)

if __name__ == "__main__":
    unittest.main()
