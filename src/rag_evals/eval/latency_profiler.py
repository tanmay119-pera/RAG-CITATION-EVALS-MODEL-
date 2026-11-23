"""Stage-by-stage latency execution profiler."""
import time
from typing import Dict, Any
from contextlib import contextmanager

class LatencyProfiler:
    """Profiles duration of retrieval, reranking, generation, and verification stages."""
    def __init__(self):
        self.timings: Dict[str, float] = {}

    @contextmanager
    def measure(self, stage_name: str):
        t0 = time.perf_counter()
        try:
            yield
        finally:
            t1 = time.perf_counter()
            self.timings[stage_name] = round((t1 - t0) * 1000.0, 3)

    def total_latency_ms(self) -> float:
        return round(sum(self.timings.values()), 3)

    def summary(self) -> Dict[str, Any]:
        return {
            "stages_ms": dict(self.timings),
            "total_ms": self.total_latency_ms(),
        }
