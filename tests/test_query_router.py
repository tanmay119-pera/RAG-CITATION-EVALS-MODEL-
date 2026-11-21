"""Tests for QueryRouter."""
import unittest
from rag_evals.retrieval.query_router import QueryRouter
from rag_evals.retrieval.intent_classifier import QueryIntent

class TestQueryRouter(unittest.TestCase):
    def test_routing(self):
        qr = QueryRouter()
        qr.register(QueryIntent.FACTUAL, lambda q: [{"chunk_id": "c1"}])
        qr.set_default(lambda q: [])
        intent, _ = qr.route("When is graduation?")
        self.assertEqual(intent, QueryIntent.FACTUAL)
        self.assertEqual(len(qr.retrieve("When is graduation?")), 1)
