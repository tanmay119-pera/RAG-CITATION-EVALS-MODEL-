"""Monitor embedding distribution drift over corpus updates."""
import math
from typing import List
from dataclasses import dataclass

@dataclass
class DriftReport:
    mean_shift: float
    variance_ratio: float
    is_drifted: bool
    details: str

class EmbeddingDriftMonitor:
    """Detects statistical distribution shifts in embedding representations."""
    def __init__(self, mean_threshold: float = 0.1, var_threshold: float = 2.0):
        self.mean_threshold = mean_threshold
        self.var_threshold = var_threshold

    def _stats(self, vectors: List[List[float]]) -> dict:
        if not vectors:
            return {"mean": 0.0, "var": 0.0, "count": 0}
        n = len(vectors)
        dim = len(vectors[0])
        norms = [math.sqrt(sum(v[i]**2 for i in range(dim))) for v in vectors]
        mean_norm = sum(norms) / n
        var_norm = sum((x - mean_norm)**2 for x in norms) / max(n - 1, 1)
        return {"mean": mean_norm, "var": var_norm, "count": n}

    def check(self, baseline: List[List[float]], current: List[List[float]]) -> DriftReport:
        bs = self._stats(baseline)
        cs = self._stats(current)
        shift = abs(cs["mean"] - bs["mean"])
        var_ratio = cs["var"] / max(bs["var"], 1e-9)
        drifted = shift > self.mean_threshold or var_ratio > self.var_threshold
        details = f"baseline_n={bs['count']} current_n={cs['count']} mean_shift={shift:.4f}"
        return DriftReport(mean_shift=round(shift, 6), variance_ratio=round(var_ratio, 4), is_drifted=drifted, details=details)
