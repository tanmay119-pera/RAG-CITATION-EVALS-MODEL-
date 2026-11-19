"""Graph-enhanced retriever traversing entity relationship triples."""

from typing import List, Set
from rag_evals.retrieval.hybrid import RetrievedChunk, HybridRetriever
from rag_evals.index.entity_graph import EntityGraph

class GraphEnhancedRetriever:
    """Expands candidate retrieval sets using knowledge graph relationship traversals."""

    def __init__(self, base_retriever: HybridRetriever, graph: EntityGraph):
        self.retriever = base_retriever
        self.graph = graph

    def retrieve_with_graph(self, query: str, top_k: int = 5) -> List[RetrievedChunk]:
        base_hits = self.retriever.retrieve(query, top_k=top_k)
        seen_ids = {c.chunk_id for c in base_hits}

        # Check query for recognized entities
        for entity in ["ethics board", "disciplinary committee", "registrar", "dean"]:
            if entity in query.lower():
                linked_chunk_ids = self.graph.get_related_chunks(entity)
                for cid in linked_chunk_ids:
                    if cid not in seen_ids:
                        meta = self.retriever.vstore.metadata_store.get(cid, {})
                        base_hits.append(RetrievedChunk(chunk_id=cid, text=meta.get("text", ""), score=0.85, rank=len(base_hits)+1, metadata=meta))
                        seen_ids.add(cid)

        return base_hits[:top_k]
