"""Query latency timer and API token cost estimation."""

import time
from dataclasses import dataclass, field
from typing import Dict, Any

@dataclass
class QueryTrace:
    query: str
    start_time: float = field(default_factory=time.time)
    end_time: float = 0.0
    retrieval_ms: float = 0.0
    generation_ms: float = 0.0
    total_tokens: int = 0
    estimated_cost_usd: float = 0.0

class QueryTracer:
    """Tracks latency metrics and calculates approximate Gemini API usage costs."""

    # gemini-3.8-flash pricing estimations ($/1M tokens)
    PRICE_PER_M_INPUT = 0.15
    PRICE_PER_M_OUTPUT = 0.60

    @classmethod
    def estimate_cost(cls, input_tokens: int, output_tokens: int) -> float:
        cost = (input_tokens / 1_000_000) * cls.PRICE_PER_M_INPUT + (output_tokens / 1_000_000) * cls.PRICE_PER_M_OUTPUT
        return round(cost, 6)
