"""Tests for APIMiddleware."""
import unittest
from rag_evals.api.middleware import APIMiddleware

class TestAPIMiddleware(unittest.TestCase):
    def test_success(self):
        mw = APIMiddleware()
        res = mw.handle("query", lambda: {"ans": "42"})
        self.assertEqual(res["status"], 200)
        self.assertEqual(res["data"]["ans"], "42")

    def test_error(self):
        mw = APIMiddleware()
        def fail(): raise ValueError("DB down")
        res = mw.handle("query", fail)
        self.assertEqual(res["status"], 500)
        self.assertIn("DB down", res["error"])
