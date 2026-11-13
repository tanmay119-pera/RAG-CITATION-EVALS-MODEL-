"""Tests for retry_call."""
import unittest
from rag_evals.utils.retry import retry_call

class TestRetryCall(unittest.TestCase):
    def test_recovers_after_failures(self):
        state = {"tries": 0}
        def flaky():
            state["tries"] += 1
            if state["tries"] < 3:
                raise ConnectionError("transient")
            return "ok"
        self.assertEqual(retry_call(flaky, max_attempts=3, base_delay=0), "ok")
        self.assertEqual(state["tries"], 3)
