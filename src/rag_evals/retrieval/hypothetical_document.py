"""Hypothetical Document Embeddings (HyDE) for query expansion."""
from typing import List, Callable, Optional

class HyDERetriever:
    """Generates a hypothetical answer passage before embedding search."""
    def __init__(self, generator_fn: Optional[Callable[[str], str]] = None):
        self.generator_fn = generator_fn or self._default_mock_generator

    @staticmethod
    def _default_mock_generator(query: str) -> str:
        return f"Regarding {query}, university policy outlines requirements, deadlines, and standard procedures."

    def generate_hypothetical_doc(self, query: str) -> str:
        return self.generator_fn(query)

    def expand_query(self, query: str) -> str:
        hypo = self.generate_hypothetical_doc(query)
        return f"{query} {hypo}"
