#!/usr/bin/env python3
"""Print sample Streamlit KPI card formatting."""
import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from rag_evals.ui.dashboard_summary import DashboardSummaryBuilder

if __name__ == "__main__":
    print(json.dumps(DashboardSummaryBuilder.build_cards({"recall_at_5": 0.88, "faithfulness": 0.91, "cfi": 0.86}), indent=2))
