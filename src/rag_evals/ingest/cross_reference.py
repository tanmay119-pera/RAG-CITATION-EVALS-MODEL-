"""Link chunks that share domain entity mentions."""
import re
from typing import List, Dict, Set
from collections import defaultdict

_STOPS = {"The", "This", "That", "These", "Those", "There", "When", "What", "Where", "With", "From"}

class CrossReferenceLinker:
    """Discovers associative links across chunks via shared named entities."""
    def __init__(self, min_shared: int = 2):
        self.min_shared = min_shared

    def _extract(self, text: str) -> Set[str]:
        words = re.findall(r"\b[A-Z][a-zA-Z0-9_-]+\b", text)
        return set(w for w in words if w not in _STOPS and len(w) >= 3)

    def link(self, chunks: List[Dict]) -> Dict[str, List[str]]:
        ent_map = {c.get("chunk_id", str(i)): self._extract(c.get("text", "")) for i, c in enumerate(chunks)}
        links = defaultdict(list)
        ids = list(ent_map.keys())
        for i in range(len(ids)):
            for j in range(i + 1, len(ids)):
                shared = ent_map[ids[i]] & ent_map[ids[j]]
                if len(shared) >= self.min_shared:
                    links[ids[i]].append(ids[j])
                    links[ids[j]].append(ids[i])
        return dict(links)
