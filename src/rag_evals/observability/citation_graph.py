"""Generates Mermaid diagrams visualizing query-to-citation-clause relationships."""

from typing import List, Dict, Any

class CitationGraphVisualizer:
    @staticmethod
    def generate_mermaid_graph(query: str, cited_chunks: List[Dict[str, Any]]) -> str:
        lines = [
            "flowchart LR",
            f'  Q["Query: {query[:30]}..."]'
        ]
        for c in cited_chunks:
            cid = c.get("chunk_id", "chunk")
            sec = c.get("section_title", "Section")[:25]
            lines.append(f'  Q --> C_{cid}["[{cid}]<br/>{sec}"]')
        return "\n".join(lines)
