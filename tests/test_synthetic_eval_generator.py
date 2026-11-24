"""Tests for SyntheticEvalGenerator."""
import unittest
from rag_evals.eval.synthetic_eval_generator import SyntheticEvalGenerator

class TestSyntheticGenerator(unittest.TestCase):
    def test_generation(self):
        gen = SyntheticEvalGenerator()
        chunk = {"chunk_id": "c10", "text": "Students must achieve 75 percent attendance to sit for final semester examinations."}
        cases = gen.generate_from_chunk(chunk)
        self.assertGreater(len(cases), 0)
        self.assertIn("c10", cases[0]["source_chunk_ids"])
