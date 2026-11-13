"""Deterministic retry wrapper for transient I/O errors."""
import time
from typing import Callable, TypeVar

T = TypeVar("T")

def retry_call(fn: Callable[[], T], max_attempts: int = 3, base_delay: float = 0.01) -> T:
    last_exc: Exception = RuntimeError("No attempts run")
    for attempt in range(max_attempts):
        try:
            return fn()
        except Exception as exc:
            last_exc = exc
            if attempt < max_attempts - 1 and base_delay > 0:
                time.sleep(base_delay * (2 ** attempt))
    raise last_exc
