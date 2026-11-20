"""Token-bucket rate limiter for API endpoints."""
import time, threading

class RateLimiter:
    """Thread-safe token-bucket rate limiter."""
    def __init__(self, tokens_per_sec: float = 10.0, bucket_size: int = 20):
        self.rate = tokens_per_sec
        self.bucket_size = bucket_size
        self._tokens = float(bucket_size)
        self._last = time.monotonic()
        self._lock = threading.Lock()

    def _refill(self):
        now = time.monotonic()
        elapsed = now - self._last
        self._tokens = min(self.bucket_size, self._tokens + elapsed * self.rate)
        self._last = now

    def acquire(self, tokens: int = 1) -> bool:
        with self._lock:
            self._refill()
            if self._tokens >= tokens:
                self._tokens -= tokens
                return True
            return False

    def wait(self, tokens: int = 1, timeout: float = 5.0) -> bool:
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            if self.acquire(tokens):
                return True
            time.sleep(0.05)
        return False
