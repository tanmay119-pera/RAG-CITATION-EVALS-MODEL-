"""Detect performance regressions between evaluation iterations."""
from typing import Dict, List
from dataclasses import dataclass

@dataclass
class RegressionAlert:
    metric: str
    baseline: float
    current: float
    drop_pct: float

class RegressionDetector:
    """Flags any metric degradation exceeding the configured tolerance threshold."""
    def __init__(self, tolerance_pct: float = 0.05):
        self.tolerance = tolerance_pct

    def evaluate(self, baseline: Dict[str, float], current: Dict[str, float]) -> List[RegressionAlert]:
        alerts = []
        for k, b_val in baseline.items():
            if k in current:
                c_val = current[k]
                if b_val > 0 and (b_val - c_val) / b_val > self.tolerance:
                    drop = round((b_val - c_val) / b_val, 4)
                    alerts.append(RegressionAlert(metric=k, baseline=b_val, current=c_val, drop_pct=drop))
        return alerts
