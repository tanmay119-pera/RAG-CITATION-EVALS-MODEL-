"""Knowledge Graph entity and relation extractor for Graph RAG."""

import re
from dataclasses import dataclass, field
from typing import List, Dict, Set

@dataclass
class KnowledgeTriple:
    subject: str
    predicate: str
    object_: str
    chunk_id: str

class EntityGraph:
    """Builds an in-memory knowledge graph of academic entities and their relationships."""

    def __init__(self):
        self.triples: List[KnowledgeTriple] = []
        self.entity_to_chunks: Dict[str, Set[str]] = {}

    def extract_and_add(self, chunk_id: str, text: str):
        # Extract Clause X.Y references
        clauses = re.findall(r"Clause\s+(\d+\.\d+)", text)
        for c in clauses:
            t = KnowledgeTriple(subject=f"Clause {c}", predicate="defined_in", object_="University Regulations", chunk_id=chunk_id)
            self.triples.append(t)
            self.entity_to_chunks.setdefault(f"Clause {c}".lower(), set()).add(chunk_id)

        # Extract entities like Dean, Registrar, Ethics Board
        for entity in ["Dean of Students", "Departmental Ethics Board", "Registrar's Office", "Disciplinary Committee"]:
            if entity.lower() in text.lower():
                self.entity_to_chunks.setdefault(entity.lower(), set()).add(chunk_id)

    def get_related_chunks(self, entity: str) -> List[str]:
        return list(self.entity_to_chunks.get(entity.lower(), set()))
