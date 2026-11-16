"""Evaluates whether generated answers are strictly faithful to retrieved context."""

import re
from typing import List

class FaithfulnessJudge:
    @staticmethod
    def evaluate_faithfulness(answer: str, retrieved_texts: List[str]) -> float:
        if not answer.strip():
            return 0.0
        if "I do not have sufficient information" in answer:
            return 1.0

        claims = [s.strip() for s in re.split(r"[.!?]\s+", answer) if s.strip()]
        if not claims:
            return 1.0

        combined_context = " ".join(retrieved_texts).lower()
        supported = 0
        for claim in claims:
            clean = re.sub(r"\[[^\]]+\]", "", claim).lower()
            words = [w for w in re.findall(r"\w+", clean) if len(w) > 3]
            if not words:
                supported += 1
                continue
            matches = sum(1 for w in words if w in combined_context)
            if (matches / len(words)) >= 0.5:
                supported += 1
        return supported / len(claims)
