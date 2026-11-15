"""Generates answers with mandatory chunk citations and refusal mechanisms."""

from typing import List, Tuple
from rag_evals.config import AppConfig, load_config
from rag_evals.retrieval.hybrid import RetrievedChunk

REFUSAL_STRING = "I do not have sufficient information in the provided documents to answer this question."

SYSTEM_PROMPT = """You are an academic regulations assistant. Answer questions truthfully and strictly using ONLY the provided numbered document chunks.

CRITICAL CITATION RULES:
1. Every factual statement or claim MUST be immediately followed by the chunk citation format [chunk_id].
2. If the user question cannot be fully answered from the provided chunks, output EXACTLY:
"I do not have sufficient information in the provided documents to answer this question."
3. Do NOT make up any citations or use external knowledge.
"""

class GroundedGenerator:
    def __init__(self, config: AppConfig | None = None):
        self.config = config or load_config()

    def format_context(self, chunks: List[RetrievedChunk]) -> str:
        formatted = []
        for c in chunks:
            formatted.append(f"--- BEGIN CHUNK [{c.chunk_id}] ---\n{c.text}\n--- END CHUNK [{c.chunk_id}] ---")
        return "\n\n".join(formatted)

    def generate(self, question: str, chunks: List[RetrievedChunk]) -> Tuple[str, bool]:
        if not chunks:
            return REFUSAL_STRING, True

        context_str = self.format_context(chunks)
        user_prompt = f"Context Documents:\n{context_str}\n\nQuestion: {question}\n\nAnswer:"

        if self.config.has_api_key:
            try:
                from google import genai
                client = genai.Client(api_key=self.config.gemini_api_key)
                response = client.interactions.create(
                    model=self.config.generation_model,
                    system_instruction=SYSTEM_PROMPT,
                    input=user_prompt
                )
                answer = response.output_text or ""
                is_refused = REFUSAL_STRING in answer
                return answer, is_refused
            except Exception as e:
                print(f"Warning: Gemini generation failed ({e}), falling back to deterministic answer.")

        return self._mock_generate(question, chunks)

    def _mock_generate(self, question: str, chunks: List[RetrievedChunk]) -> Tuple[str, bool]:
        q_words = set(w.lower() for w in question.split() if len(w) > 3)
        best_chunk = chunks[0]
        chunk_words = set(w.lower() for w in best_chunk.text.split())

        overlap = q_words.intersection(chunk_words)
        if len(overlap) < 2:
            return REFUSAL_STRING, True

        answer = f"According to university policy, {best_chunk.text[:120].strip()}... [{best_chunk.chunk_id}]"
        return answer, False
