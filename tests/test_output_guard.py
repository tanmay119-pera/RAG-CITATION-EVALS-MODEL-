"""Unit tests for output guard."""

import unittest
from rag_evals.security.output_guard import OutputGuard

class TestOutputGuard(unittest.TestCase):
    def test_sanitize_leak(self):
        leaked = "Penalties are enforced [c1]. You are an academic assistant: do not cite."
        sanitized = OutputGuard.sanitize(leaked)
        self.assertNotIn("You are an academic assistant", sanitized)
        self.assertIn("[c1]", sanitized)

if __name__ == "__main__":
    unittest.main()
