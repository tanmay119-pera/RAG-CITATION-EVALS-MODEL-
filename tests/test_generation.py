"""Unit tests for generation, prompt formatting, and citation verification."""

import unittest
from rag_evals.generation.generator import GroundedGenerator, REFUSAL_STRING
from rag_evals.generation.verifier import CitationVerifier
from rag_evals.retrieval.hybrid import RetrievedChunk
from scripts.ask import ask

class TestGeneration(unittest.TestCase):
    def test_citation_verifier(self):
        text = "Students may withdraw within 12 days [chunk_1]. Failure penalty is F [chunk_bad]."
        res = CitationVerifier.verify(text, valid_chunk_ids={"chunk_1"})
        self.assertFalse(res.is_valid)
        self.assertEqual(res.valid_ids, ["chunk_1"])
        self.assertEqual(res.invalid_ids, ["chunk_bad"])

    def test_refusal_on_empty_chunks(self):
        gen = GroundedGenerator()
        ans, is_refused = gen.generate("What is quantum computing?", [])
        self.assertTrue(is_refused)
        self.assertEqual(ans, REFUSAL_STRING)

    def test_ask_pipeline(self):
        res = ask("What are the penalties for plagiarism?")
        self.assertIn("answer", res)
        self.assertIn("verification", res)

if __name__ == "__main__":
    unittest.main()
