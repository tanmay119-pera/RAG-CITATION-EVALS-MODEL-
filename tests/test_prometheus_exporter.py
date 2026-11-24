"""Tests for PrometheusExporter."""
import unittest
from rag_evals.observability.prometheus_exporter import PrometheusExporter

class TestPrometheusExporter(unittest.TestCase):
    def test_metrics_export(self):
        pe = PrometheusExporter()
        pe.inc("rag_queries_total", 5)
        raw = pe.export()
        self.assertIn("rag_queries_total 5", raw)
