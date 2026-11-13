"""High-resolution execution stopwatch."""
import time

class Stopwatch:
    """Measures elapsed wall-clock milliseconds."""
    def __init__(self):
        self.start_ns = 0
        self.elapsed_ms = 0.0

    def __enter__(self):
        self.start_ns = time.perf_counter_ns()
        return self

    def __exit__(self, *_args):
        self.elapsed_ms = (time.perf_counter_ns() - self.start_ns) / 1_000_000.0
