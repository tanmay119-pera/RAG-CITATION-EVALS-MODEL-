"""Tests for AlertRuleEngine."""
import unittest
from rag_evals.observability.alert_rules import AlertRuleEngine

class TestAlertRules(unittest.TestCase):
    def test_triggers_alerts(self):
        eng = AlertRuleEngine(max_p95_ms=500.0, min_cfi=0.80)
        alerts = eng.evaluate({"p95_ms": 900.0, "cfi": 0.65})
        self.assertEqual(len(alerts), 2)
        self.assertEqual(eng.evaluate({"p95_ms": 200.0, "cfi": 0.90}), [])
