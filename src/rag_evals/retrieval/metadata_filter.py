"""Pre- and post-retrieval metadata filtering for scoped document search."""

from typing import List, Dict, Any
from rag_evals.retrieval.hybrid import RetrievedChunk

class MetadataFilter:
    """Filters candidate chunks based on section titles, page ranges, or source documents."""

    @staticmethod
    def filter_chunks(
        chunks: List[RetrievedChunk],
        section_prefix: str = "",
        min_page: int = 1,
        max_page: int = 9999
    ) -> List[RetrievedChunk]:
        filtered = []
        for c in chunks:
            page = c.metadata.get("page_number", 1)
            sec = c.metadata.get("section_title", "").lower()
            if page < min_page or page > max_page:
                continue
            if section_prefix and section_prefix.lower() not in sec:
                continue
            filtered.append(c)
        return filtered
