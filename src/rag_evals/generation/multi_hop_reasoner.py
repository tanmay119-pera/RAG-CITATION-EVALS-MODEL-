"""Iterative multi-hop question answering pipeline."""
from typing import List, Dict, Callable

class MultiHopReasoner:
    """Decomposes compound queries and gathers progressive evidence."""
    def __init__(self, retriever_fn: Callable, generator_fn: Callable):
        self.retriever_fn = retriever_fn
        self.generator_fn = generator_fn

    def answer_multi_hop(self, query: str, hops: int = 2) -> Dict:
        gathered_chunks: List[Dict] = []
        seen_ids = set()
        current_query = query
        intermediate_steps = []

        for h in range(hops):
            chunks = self.retriever_fn(current_query)
            new_chunks = [c for c in chunks if c.get("chunk_id") not in seen_ids]
            for nc in new_chunks:
                seen_ids.add(nc.get("chunk_id"))
            gathered_chunks.extend(new_chunks)
            step_ans = self.generator_fn(current_query, new_chunks)
            intermediate_steps.append({"hop": h + 1, "query": current_query, "answer": step_ans})
            current_query = f"{query} context: {step_ans}"

        final_ans = self.generator_fn(query, gathered_chunks)
        return {
            "query": query,
            "final_answer": final_ans,
            "total_chunks_consulted": len(gathered_chunks),
            "steps": intermediate_steps,
        }
