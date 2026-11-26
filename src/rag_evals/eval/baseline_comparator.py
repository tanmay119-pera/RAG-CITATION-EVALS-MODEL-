"""Compare latest evaluation summary against saved baseline numbers."""
from typing import Dict

class BaselineDeltaTracker:
    """Computes metric deltas across evaluation checkpoints."""

    @staticmethod
    def compute_deltas(baseline: Dict[str, float], current: Dict[str, float]) -> Dict[str, float]:
        return {
            k: round(current[k] - baseline[k], 4)
            for k in baseline
            if k in current and isinstance(baseline[k], (int, float))
        }
