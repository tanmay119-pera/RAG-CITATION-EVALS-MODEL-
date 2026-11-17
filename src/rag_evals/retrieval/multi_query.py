"""Generates multi-query semantic reformulations to boost retrieval recall."""

import re
from typing import List

class MultiQueryGenerator:
    """Produces query expansions and keyword variations for comprehensive retrieval."""

    SYNONYMS = {
        "penalty": ["sanction", "punishment", "consequence"],
        "plagiarism": ["academic dishonesty", "cheating", "unauthorized collaboration"],
        "withdraw": ["drop course", "course cancellation", "w grade"],
        "refund": ["tuition reimbursement", "money back", "financial credit"],
        "repeat": ["retake course", "second attempt"]
    }

    @classmethod
    def expand(cls, query: str) -> List[str]:
        expansions = [query]
        q_lower = query.lower()

        for term, syns in cls.SYNONYMS.items():
            if term in q_lower:
                for syn in syns[:2]:
                    reformulated = re.sub(re.escape(term), syn, q_lower, flags=re.IGNORECASE)
                    if reformulated not in expansions:
                        expansions.append(reformulated)

        return expansions[:3]
