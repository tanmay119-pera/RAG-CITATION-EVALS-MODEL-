"""Unit tests for structured logger and cost tracer."""

import unittest
from rag_evals.observability.logger import StructuredLogger
from rag_evals.observability.tracer import QueryTracer

class TestObservability(unittest.TestCase):
    def test_structured_logger(self):
        # Should execute without throwing error
        StructuredLogger.log("query_start", {"query": "test query"})

    def test_cost_estimator(self):
        cost = QueryTracer.estimate_cost(input_tokens=1000, output_tokens=500)
        self.assertGreater(cost, 0.0)
        self.assertLess(cost, 0.01)

if __name__ == "__main__":
    unittest.main()
