"""Threshold-based alerting rules for production RAG monitoring."""
from typing import Dict, List

class AlertRuleEngine:
    """Evaluates telemetry metrics against configured warning thresholds."""
    def __init__(self, max_p95_ms: float = 1500.0, min_cfi: float = 0.75):
        self.max_p95_ms = max_p95_ms
        self.min_cfi = min_cfi

    def evaluate(self, stats: Dict[str, float]) -> List[str]:
        alerts: List[str] = []
        if stats.get("p95_ms", 0.0) > self.max_p95_ms:
            alerts.append(f"HIGH_LATENCY: p95={stats['p95_ms']}ms exceeds {self.max_p95_ms}ms")
        if stats.get("cfi", 1.0) < self.min_cfi:
            alerts.append(f"LOW_CFI: cfi={stats['cfi']} below {self.min_cfi}")
        return alerts
