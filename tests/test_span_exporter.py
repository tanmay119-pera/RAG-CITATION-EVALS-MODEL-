"""Tests for SpanExporter."""
import unittest
from rag_evals.observability.span_exporter import SpanExporter

class TestSpanExporter(unittest.TestCase):
    def test_export(self):
        exp = SpanExporter()
        exp.record_span("t1", "retrieval", 23.5, {"top_k": 5})
        raw = exp.export_json()
        self.assertIn("retrieval", raw)
        self.assertEqual(len(exp.spans), 1)
