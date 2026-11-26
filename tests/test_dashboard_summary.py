"""Tests for DashboardSummaryBuilder."""
import unittest
from rag_evals.ui.dashboard_summary import DashboardSummaryBuilder

class TestDashboardSummary(unittest.TestCase):
    def test_formats_percentages(self):
        cards = DashboardSummaryBuilder.build_cards({"recall_at_5": 0.85, "faithfulness": 0.92, "cfi": 0.88})
        self.assertEqual(cards["Recall@5"], "85.0%")
        self.assertEqual(cards["Citation Fidelity"], "88.0%")
