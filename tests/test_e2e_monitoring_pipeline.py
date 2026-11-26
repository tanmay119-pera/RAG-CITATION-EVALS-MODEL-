"""End-to-end monitoring and verification pipeline test."""
import unittest
from rag_evals.api.batch_runner import BatchPipelineRunner
from rag_evals.generation.citation_highlighter import CitationSpanExtractor
from rag_evals.observability import MetricsAggregator, AlertRuleEngine

class TestE2EMonitoring(unittest.TestCase):
    def test_full_monitoring_flow(self):
        runner = BatchPipelineRunner(lambda q: {"answer": "Attendance is 75% [c1].", "latency_ms": 120.0})
        runs = runner.run_all(["Attendance rule?"])
        spans = CitationSpanExtractor.extract(runs[0]["answer"])
        self.assertTrue(spans[0]["grounded"])
        ma = MetricsAggregator()
        ma.record(runs[0]["latency_ms"], 0.95)
        alerts = AlertRuleEngine().evaluate({**ma.summary(), "cfi": 0.95})
        self.assertEqual(alerts, [])
