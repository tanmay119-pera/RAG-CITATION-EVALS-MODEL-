"""ASCII and HTML citation relationship visualizer."""
from typing import List, Dict

class CitationGraphView:
    """Renders textual dependency trees between queries, answers, and source citations."""
    def render_ascii(self, query: str, citations: List[str], chunk_titles: Dict[str, str] = None) -> str:
        titles = chunk_titles or {}
        lines = [f"Query: \"{query}\"", " └── Citations:"]
        for i, c in enumerate(citations):
            prefix = "     ├──" if i < len(citations) - 1 else "     └──"
            t = titles.get(c, "Document Segment")
            lines.append(f"{prefix} [{c}] {t}")
        return "\n".join(lines)
