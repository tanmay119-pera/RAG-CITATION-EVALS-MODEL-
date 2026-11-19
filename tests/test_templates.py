"""Unit tests for prompt template registry."""

import unittest
from rag_evals.generation.templates import PromptRegistry

class TestTemplates(unittest.TestCase):
    def test_get_templates(self):
        t1 = PromptRegistry.get_template("academic")
        self.assertIn("academic regulations", t1)
        t2 = PromptRegistry.get_template("legal")
        self.assertIn("compliance officer", t2)

if __name__ == "__main__":
    unittest.main()
