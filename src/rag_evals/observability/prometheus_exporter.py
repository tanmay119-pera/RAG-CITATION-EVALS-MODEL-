"""Prometheus metrics text exporter."""
from typing import Dict

class PrometheusExporter:
    """Formats internal pipeline counters into Prometheus exposition format."""
    def __init__(self):
        self.counters: Dict[str, float] = {}

    def inc(self, metric_name: str, value: float = 1.0):
        self.counters[metric_name] = self.counters.get(metric_name, 0.0) + value

    def export(self) -> str:
        lines = []
        for k, v in sorted(self.counters.items()):
            lines.append(f"# TYPE {k} counter")
            lines.append(f"{k} {v}")
        return "\n".join(lines) + "\n"
