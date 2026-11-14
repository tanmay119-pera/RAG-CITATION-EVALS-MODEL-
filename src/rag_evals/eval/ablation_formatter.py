"""Render ablation experiment rows into publication-ready Markdown or LaTeX."""
from typing import List, Dict

class AblationTableFormatter:
    """Formats ablation metrics tables for README and technical reports."""

    @staticmethod
    def to_markdown(rows: List[Dict]) -> str:
        if not rows:
            return ""
        cols = list(rows[0].keys())
        header = "| " + " | ".join(cols) + " |"
        sep = "| " + " | ".join(["---"] * len(cols)) + " |"
        body = ["| " + " | ".join(str(r.get(c, "")) for c in cols) + " |" for r in rows]
        return "\n".join([header, sep, *body])
