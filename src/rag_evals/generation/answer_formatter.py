"""Format verified answers with reference footnote lists."""
from typing import List, Dict

def format_with_references(answer: str, used_chunks: List[Dict]) -> str:
    if not used_chunks:
        return answer
    refs = ["\n\nSources:"]
    for c in used_chunks:
        cid = c.get("chunk_id", "unknown")
        src = c.get("source", "document")
        refs.append(f"- [{cid}] {src}")
    return answer + "\n".join(refs)
