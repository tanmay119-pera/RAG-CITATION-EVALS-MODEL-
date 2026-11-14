"""Tests for RefusalDetector."""
import unittest
from rag_evals.generation.refusal_detector import RefusalDetector

class TestRefusalDetector(unittest.TestCase):
    def test_detects_refusals_and_answers(self):
        self.assertTrue(RefusalDetector.is_refusal("I don't know based on the provided documents."))
        self.assertFalse(RefusalDetector.is_refusal("Students require 75% attendance [c1]."))
