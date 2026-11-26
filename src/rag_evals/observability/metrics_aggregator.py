"""Rolling metrics aggregator for telemetry dashboards."""
from typing import List, Dict

class MetricsAggregator:
    """Tracks historical query latencies and citation confidence distributions."""
    def __init__(self):
        self.latencies_ms: List[float] = []
        self.confidences: List[float] = []

    def record(self, latency_ms: float, confidence: float):
        self.latencies_ms.append(latency_ms)
        self.confidences.append(confidence)

    def percentile_latency(self, p: float) -> float:
        if not self.latencies_ms:
            return 0.0
        s = sorted(self.latencies_ms)
        idx = min(len(s) - 1, max(0, int(round((p / 100.0) * (len(s) - 1)))))
        return round(s[idx], 2)

    def summary(self) -> Dict[str, float]:
        n = len(self.latencies_ms)
        avg_conf = round(sum(self.confidences) / n, 4) if n else 0.0
        return {"count": n, "p50_ms": self.percentile_latency(50), "p95_ms": self.percentile_latency(95), "avg_confidence": avg_conf}
