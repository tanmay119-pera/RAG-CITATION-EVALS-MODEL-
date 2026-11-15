"""Programmatic verification of chunk IDs and citation faithfulness."""

import re
from dataclasses import dataclass, field
from typing import List, Set

@dataclass
class VerificationResult:
    is_valid: bool
    cited_ids: List[str]
    valid_ids: List[str]
    invalid_ids: List[str]
    uncited_claims: List[str] = field(default_factory=list)

class CitationVerifier:
    @staticmethod
    def extract_citations(text: str) -> List[str]:
        return re.findall(r"\[([a-zA-Z0-9_\.-]+)\]", text)

    @classmethod
    def verify(cls, answer: str, valid_chunk_ids: Set[str]) -> VerificationResult:
        cited = cls.extract_citations(answer)
        valid = [cid for cid in cited if cid in valid_chunk_ids]
        invalid = [cid for cid in cited if cid not in valid_chunk_ids]

        sentences = [s.strip() for s in re.split(r"[.!?]\s+", answer) if s.strip()]
        uncited = []
        for s in sentences:
            if not re.search(r"\[[a-zA-Z0-9_\.-]+\]", s):
                uncited.append(s)

        is_valid = len(invalid) == 0 and len(valid) > 0
        return VerificationResult(
            is_valid=is_valid,
            cited_ids=cited,
            valid_ids=valid,
            invalid_ids=invalid,
            uncited_claims=uncited
        )
