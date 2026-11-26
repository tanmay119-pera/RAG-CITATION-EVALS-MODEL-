"""Build KPI card dictionaries for Streamlit evaluation tab."""
from typing import Dict, Any

class DashboardSummaryBuilder:
    """Formats evaluation scores into display-ready percentages."""

    @staticmethod
    def build_cards(metrics: Dict[str, float]) -> Dict[str, str]:
        return {
            "Recall@5": f"{metrics.get('recall_at_5', 0.0) * 100:.1f}%",
            "Faithfulness": f"{metrics.get('faithfulness', 0.0) * 100:.1f}%",
            "Citation Fidelity": f"{metrics.get('cfi', 0.0) * 100:.1f}%",
        }
