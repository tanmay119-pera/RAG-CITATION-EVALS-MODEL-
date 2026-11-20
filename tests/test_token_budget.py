"""Tests for TokenBudget."""
import unittest
from rag_evals.generation.token_budget import TokenBudget

class TestTokenBudget(unittest.TestCase):
    def test_consume_within_limit(self):
        tb = TokenBudget(max_prompt_tokens=100, max_completion_tokens=50)
        self.assertTrue(tb.consume_prompt(50))
        self.assertEqual(tb.prompt_remaining, 50)

    def test_reject_over_limit(self):
        tb = TokenBudget(max_prompt_tokens=10)
        self.assertTrue(tb.consume_prompt(10))
        self.assertFalse(tb.consume_prompt(1))

    def test_reset(self):
        tb = TokenBudget(max_prompt_tokens=10)
        tb.consume_prompt(10)
        tb.reset()
        self.assertEqual(tb.prompt_remaining, 10)
