"""Split golden evaluation datasets while preserving unanswerable ratios."""
from typing import List, Dict, Tuple

class StratifiedSplitter:
    """Deterministic stratified train/dev/test splitter."""

    @staticmethod
    def split(cases: List[Dict], holdout_ratio: float = 0.2) -> Tuple[List[Dict], List[Dict]]:
        answerable = [c for c in cases if not c.get("is_unanswerable", False)]
        unanswerable = [c for c in cases if c.get("is_unanswerable", False)]

        def take_holdout(group: List[Dict]):
            n_hold = max(1, int(len(group) * holdout_ratio)) if group and holdout_ratio > 0 else 0
            return group[n_hold:], group[:n_hold]

        a_main, a_hold = take_holdout(answerable)
        u_main, u_hold = take_holdout(unanswerable)
        return a_main + u_main, a_hold + u_hold
