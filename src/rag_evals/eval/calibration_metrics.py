"""Expected Calibration Error (ECE) and Brier Score metrics."""
from typing import Sequence

class CalibrationEvaluator:
    """Evaluates whether answer confidence scores match empirical accuracy."""

    @staticmethod
    def brier_score(probs: Sequence[float], outcomes: Sequence[int]) -> float:
        if not probs:
            return 0.0
        total = sum((p - y) ** 2 for p, y in zip(probs, outcomes))
        return round(total / len(probs), 4)

    @staticmethod
    def expected_calibration_error(probs: Sequence[float], outcomes: Sequence[int], bins: int = 5) -> float:
        if not probs:
            return 0.0
        n = len(probs)
        ece = 0.0
        for b in range(bins):
            lo, hi = b / bins, (b + 1) / bins
            idxs = [i for i, p in enumerate(probs) if (lo <= p < hi or (b == bins - 1 and p == 1.0))]
            if not idxs:
                continue
            avg_p = sum(probs[i] for i in idxs) / len(idxs)
            avg_y = sum(outcomes[i] for i in idxs) / len(idxs)
            ece += (len(idxs) / n) * abs(avg_p - avg_y)
        return round(ece, 4)
