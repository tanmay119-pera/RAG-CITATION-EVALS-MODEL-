"""Tests for IntentClassifier."""
import unittest
from rag_evals.retrieval.intent_classifier import IntentClassifier, QueryIntent

class TestIntentClassifier(unittest.TestCase):
    def setUp(self):
        self.clf = IntentClassifier()

    def test_intents(self):
        self.assertEqual(self.clf.classify("When is the exam?"), QueryIntent.FACTUAL)
        self.assertEqual(self.clf.classify("Compare CS and IT syllabus"), QueryIntent.COMPARISON)
        self.assertEqual(self.clf.classify("How to apply for leave?"), QueryIntent.PROCEDURAL)
        self.assertEqual(self.clf.classify("What is CGPA?"), QueryIntent.DEFINITION)
        self.assertEqual(self.clf.classify(""), QueryIntent.UNANSWERABLE)

    def test_routing(self):
        self.assertEqual(self.clf.route_top_k(QueryIntent.COMPARISON), 10)
        self.assertEqual(self.clf.route_top_k(QueryIntent.DEFINITION), 3)
