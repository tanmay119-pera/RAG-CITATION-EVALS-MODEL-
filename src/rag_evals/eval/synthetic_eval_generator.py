"""Generate synthetic evaluation cases from raw text chunks."""
import re
from typing import List, Dict

class SyntheticEvalGenerator:
    """Creates synthetic question-answer-evidence triples from chunks."""
    def generate_from_chunk(self, chunk: Dict) -> List[Dict]:
        text = chunk.get("text", "")
        cid = chunk.get("chunk_id", "c0")
        sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if len(s.split()) >= 6]
        cases = []
        for i, s in enumerate(sentences[:2]):
            q = f"According to {cid}, what is stated regarding: {s[:30]}...?"
            cases.append({
                "synthetic_id": f"syn_{cid}_{i}",
                "query": q,
                "golden_answer": s,
                "source_chunk_ids": [cid],
            })
        return cases

    def batch_generate(self, chunks: List[Dict]) -> List[Dict]:
        all_cases = []
        for c in chunks:
            all_cases.extend(self.generate_from_chunk(c))
        return all_cases
