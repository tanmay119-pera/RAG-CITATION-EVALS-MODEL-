"""Hierarchical chunking preserving parent and child relationships."""
from typing import List, Dict

class HierarchicalChunker:
    """Creates parent sections and child sub-chunks with bidirectional link IDs."""
    def __init__(self, parent_size: int = 1000, child_size: int = 300, overlap: int = 50):
        self.parent_size = parent_size
        self.child_size = child_size
        self.overlap = overlap

    def _split(self, text: str, size: int, overlap: int) -> List[str]:
        words = text.split()
        chunks, i = [], 0
        while i < len(words):
            chunk = " ".join(words[i:i + size])
            if chunk:
                chunks.append(chunk)
            i += max(1, size - overlap)
        return chunks

    def chunk(self, doc: Dict) -> List[Dict]:
        text = doc.get("text", "")
        src = doc.get("source", "doc")
        parents = self._split(text, self.parent_size, 0)
        out = []
        for pi, pt in enumerate(parents):
            pid = f"{src}_p{pi}"
            parent_chunk = {"chunk_id": pid, "text": pt, "source": src, "level": "parent", "children": []}
            children = self._split(pt, self.child_size, self.overlap)
            for ci, ct in enumerate(children):
                cid = f"{pid}_c{ci}"
                child_chunk = {"chunk_id": cid, "text": ct, "source": src, "level": "child", "parent_id": pid}
                parent_chunk["children"].append(cid)
                out.append(child_chunk)
            out.append(parent_chunk)
        return out
