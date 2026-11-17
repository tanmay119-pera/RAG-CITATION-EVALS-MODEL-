"""Unit tests for API schemas, server, and client SDK."""

import unittest
from rag_evals.api.schemas import QueryRequest, QueryResponse
from rag_evals.api.server import RAGApiServer
from rag_evals.api.client import RAGClient

class TestApi(unittest.TestCase):
    def test_api_server_query(self):
        server = RAGApiServer()
        req = QueryRequest(query="What is the penalty for plagiarism?", top_k=3)
        res = server.handle_query(req)
        self.assertEqual(res.query, req.query)
        self.assertGreater(len(res.answer), 10)
        self.assertGreaterEqual(res.latency_ms, 0.0)

    def test_client_sdk(self):
        client = RAGClient()
        res = client.query("What are the penalties for plagiarism violations?")
        self.assertIn("university policy", res.answer.lower())
        self.assertIn("[", res.answer)

if __name__ == "__main__":
    unittest.main()
