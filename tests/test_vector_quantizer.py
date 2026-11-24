"""Tests for ScalarQuantizer."""
import unittest
from rag_evals.index.vector_quantizer import ScalarQuantizer

class TestScalarQuantizer(unittest.TestCase):
    def test_quantize_dequantize(self):
        sq = ScalarQuantizer()
        vec = [0.1, 0.5, 0.9, -0.2]
        q, v_min, v_max = sq.quantize(vec)
        self.assertEqual(len(q), len(vec))
        rec = sq.dequantize(q, v_min, v_max)
        for original, reconstructed in zip(vec, rec):
            self.assertAlmostEqual(original, reconstructed, delta=0.02)
