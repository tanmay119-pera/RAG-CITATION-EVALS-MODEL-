"""Structured JSON logging with request tracing."""

import json
import time
from typing import Dict, Any

class StructuredLogger:
    @staticmethod
    def log(event: str, data: Dict[str, Any]):
        payload = {
            "timestamp": time.time(),
            "event": event,
            "data": data
        }
        print(f"[JSON_LOG] {json.dumps(payload)}")
