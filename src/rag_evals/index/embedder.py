"""Gemini embedding client using google-genai or offline deterministic embeddings."""

import math
import hashlib
from typing import List
from rag_evals.config import AppConfig, load_config

class GeminiEmbedder:
    """Produces embeddings using gemini-embedding-001 or offline mock vectors."""

    def __init__(self, config: AppConfig | None = None):
        self.config = config or load_config()
        self.client = None
        if self.config.has_api_key:
            try:
                from google import genai
                self.client = genai.Client(api_key=self.config.gemini_api_key)
            except Exception:
                self.client = None

    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        if not texts:
            return []

        if self.client:
            try:
                response = self.client.models.embed_content(
                    model=self.config.embedding_model,
                    contents=texts
                )
                if hasattr(response, "embeddings"):
                    return [e.values for e in response.embeddings]
            except Exception as e:
                print(f"Warning: Gemini API call failed ({e}), using offline embeddings.")

        return [self._mock_embed(t) for t in texts]

    def embed_query(self, query: str) -> List[float]:
        return self.embed_texts([query])[0]

    @staticmethod
    def _mock_embed(text: str, dim: int = 128) -> List[float]:
        """Deterministic normalized vector derived from text content for offline execution."""
        vec = [0.0] * dim
        tokens = text.lower().split()
        for i, word in enumerate(tokens):
            h = int(hashlib.md5(word.encode()).hexdigest(), 16)
            idx = h % dim
            vec[idx] += 1.0 / (1.0 + (i % 5))
        # Normalize
        norm = math.sqrt(sum(v * v for v in vec))
        if norm > 0:
            vec = [v / norm for v in vec]
        else:
            vec[0] = 1.0
        return vec

# Compatibility alias
Embedder = GeminiEmbedder
