"""Heuristic hallucination risk grader."""
import re
from typing import List, Dict, Set

class HallucinationGrader:
    """Measures lexical and named entity grounding between generated answers and source passages."""
    def extract_keywords(self, text: str) -> Set[str]:
        words = re.findall(r"\b[a-zA-Z0-9_-]{3,}\b", text.lower())
        stops = {"the", "and", "for", "with", "that", "this", "from", "are", "have"}
        return set(w for w in words if w not in stops)

    def grade(self, answer: str, source_texts: List[str]) -> Dict[str, float]:
        ans_kw = self.extract_keywords(answer)
        if not ans_kw:
            return {"grounding_ratio": 1.0, "hallucination_risk": 0.0}
        src_kw = set()
        for st in source_texts:
            src_kw.update(self.extract_keywords(st))
        grounded = ans_kw & src_kw
        ratio = round(len(grounded) / len(ans_kw), 4)
        return {
            "grounding_ratio": ratio,
            "hallucination_risk": round(1.0 - ratio, 4),
        }
