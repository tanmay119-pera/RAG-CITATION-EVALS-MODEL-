"""Compare evaluation runs across configurations."""
from typing import List, Dict
from dataclasses import dataclass

@dataclass
class EvalSummary:
    config_name: str
    recall: float
    mrr: float
    faithfulness: float
    cfi: float

class BatchComparator:
    """Ranks and aggregates evaluation runs across experimental configurations."""
    def __init__(self):
        self.runs: List[EvalSummary] = []

    def add_run(self, summary: EvalSummary):
        self.runs.append(summary)

    def rank_by(self, metric: str = "cfi") -> List[EvalSummary]:
        return sorted(self.runs, key=lambda x: getattr(x, metric), reverse=True)

    def summary_table(self) -> List[Dict]:
        return [{"config": r.config_name, "recall": r.recall, "mrr": r.mrr, "cfi": r.cfi} for r in self.runs]
