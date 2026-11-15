"""Schema definition for golden Q&A evaluation cases."""

from dataclasses import dataclass, field
from typing import List

@dataclass
class EvalCase:
    case_id: str
    query: str
    ground_truth_answer: str
    expected_clause: str
    is_answerable: bool = True
    keywords: List[str] = field(default_factory=list)
