"""Integration test for citation verification over retrieved candidate chunks."""
import unittest
from rag_evals.generation.verifier import CitationVerifier

class TestRetrievalGenerationIntegration(unittest.TestCase):
    def test_citation_verification_flow(self):
        valid_chunk_ids = {"rule_c0", "rule_c1"}
        generated_answer = "Students must attend 75% of classes [rule_c0]. Debarment applies otherwise [rule_c1]."
        res = CitationVerifier.verify(generated_answer, valid_chunk_ids)
        self.assertTrue(res.is_valid)
        self.assertEqual(len(res.invalid_ids), 0)
        self.assertEqual(set(res.cited_ids), valid_chunk_ids)
