"""Tests for EvalSerializer."""
import unittest
from rag_evals.eval.serializer import EvalSerializer

class TestSerializer(unittest.TestCase):
    def test_serialization(self):
        ser = EvalSerializer()
        data = [{"config": "base", "score": 0.8}]
        self.assertIn("score", ser.to_json(data))
        self.assertIn("score", ser.to_csv(data))
        self.assertIn("| score |", ser.to_markdown(data))
