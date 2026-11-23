"""Tests for HyDERetriever."""
import unittest
from rag_evals.retrieval.hypothetical_document import HyDERetriever

class TestHyDE(unittest.TestCase):
    def test_default_generation(self):
        hyde = HyDERetriever()
        doc = hyde.generate_hypothetical_doc("attendance rules")
        self.assertIn("attendance rules", doc)
        exp = hyde.expand_query("attendance rules")
        self.assertTrue(exp.startswith("attendance rules"))

    def test_custom_generator(self):
        hyde = HyDERetriever(generator_fn=lambda q: "Custom expansion text.")
        self.assertEqual(hyde.generate_hypothetical_doc("test"), "Custom expansion text.")
