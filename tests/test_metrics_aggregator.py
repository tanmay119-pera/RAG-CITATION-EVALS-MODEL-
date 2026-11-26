"""Tests for MetricsAggregator."""
import unittest
from rag_evals.observability.metrics_aggregator import MetricsAggregator

class TestMetricsAggregator(unittest.TestCase):
    def test_percentiles_and_confidence(self):
        ma = MetricsAggregator()
        for lat, conf in [(10.0, 0.9), (20.0, 0.8), (100.0, 0.7)]:
            ma.record(lat, conf)
        s = ma.summary()
        self.assertEqual(s["count"], 3)
        self.assertEqual(s["p50_ms"], 20.0)
        self.assertEqual(s["avg_confidence"], 0.8)
