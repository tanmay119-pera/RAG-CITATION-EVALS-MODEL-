"""Tests for RateLimiter."""
import unittest, time
from rag_evals.api.rate_limiter import RateLimiter

class TestRateLimiter(unittest.TestCase):
    def test_acquire_within_budget(self):
        rl = RateLimiter(tokens_per_sec=100, bucket_size=10)
        self.assertTrue(rl.acquire(1))

    def test_acquire_exhausts_bucket(self):
        rl = RateLimiter(tokens_per_sec=0, bucket_size=3)
        self.assertTrue(rl.acquire(1))
        self.assertTrue(rl.acquire(1))
        self.assertTrue(rl.acquire(1))
        self.assertFalse(rl.acquire(1))

    def test_wait_refills(self):
        rl = RateLimiter(tokens_per_sec=100, bucket_size=1)
        rl.acquire(1)
        self.assertTrue(rl.wait(1, timeout=1.0))
