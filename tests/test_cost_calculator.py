"""Tests for CostCalculator."""
import unittest
from rag_evals.eval.cost_calculator import CostCalculator

class TestCostCalculator(unittest.TestCase):
    def test_cost_calculation(self):
        cc = CostCalculator()
        res = cc.calculate("gemini-1.5-flash", prompt_tokens=10_000, completion_tokens=2_000)
        self.assertGreater(res["estimated_cost_usd"], 0.0)
        self.assertEqual(res["total_tokens"], 12_000)
