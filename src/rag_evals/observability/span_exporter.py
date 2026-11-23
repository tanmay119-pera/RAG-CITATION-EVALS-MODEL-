"""OpenTelemetry-compatible trace span serialization."""
import json, time
from typing import List, Dict, Any

class SpanExporter:
    """Serializes pipeline execution spans for telemetry ingestion."""
    def __init__(self):
        self.spans: List[Dict[str, Any]] = []

    def record_span(self, trace_id: str, span_name: str, duration_ms: float, attributes: Dict[str, Any] = None):
        span = {
            "trace_id": trace_id,
            "span_name": span_name,
            "duration_ms": duration_ms,
            "attributes": attributes or {},
            "timestamp": time.time(),
        }
        self.spans.append(span)

    def export_json(self) -> str:
        return json.dumps(self.spans, indent=2)

    def clear(self):
        self.spans.clear()
