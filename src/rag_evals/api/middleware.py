"""API request logging and error handling middleware."""
import time
from typing import Callable, Dict, Any

class APIMiddleware:
    """Wraps endpoint calls to provide structured telemetry and standard error responses."""
    def __init__(self, logger_fn: Callable[[Dict[str, Any]], None] = None):
        self.logger_fn = logger_fn or (lambda x: None)

    def handle(self, endpoint_name: str, handler: Callable[[], Dict[str, Any]]) -> Dict[str, Any]:
        t0 = time.perf_counter()
        try:
            res = handler()
            status = "success"
            error = None
        except Exception as e:
            res = {}
            status = "error"
            error = str(e)
        elapsed_ms = round((time.perf_counter() - t0) * 1000.0, 2)
        self.logger_fn({"endpoint": endpoint_name, "status": status, "latency_ms": elapsed_ms, "error": error})
        if status == "error":
            return {"error": error, "status": 500}
        return {"data": res, "status": 200, "latency_ms": elapsed_ms}
