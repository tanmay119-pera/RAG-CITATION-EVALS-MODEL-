"""Tests for WebhookManager."""
import unittest
from rag_evals.observability.webhooks import WebhookManager, EventType

class TestWebhooks(unittest.TestCase):
    def test_dispatch(self):
        wm = WebhookManager()
        wm.subscribe("https://example.com/webhook", [EventType.EVAL_DONE])
        wm.dispatch(EventType.EVAL_DONE, {"score": 0.95})
        self.assertEqual(len(wm.delivery_log), 1)
        self.assertEqual(wm.delivery_log[0]["event"], "eval_done")
