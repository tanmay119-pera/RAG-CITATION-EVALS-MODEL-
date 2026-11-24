"""LLM query inference cost calculator."""
from typing import Dict, Any

_PRICING_PER_1M = {
    "gemini-1.5-flash": {"prompt": 0.075, "completion": 0.30},
    "gemini-1.5-pro": {"prompt": 1.25, "completion": 5.00},
}

class CostCalculator:
    """Estimates monetary API expenditure based on token metrics."""
    def calculate(self, model: str, prompt_tokens: int, completion_tokens: int) -> Dict[str, Any]:
        pricing = _PRICING_PER_1M.get(model, {"prompt": 0.10, "completion": 0.40})
        prompt_cost = (prompt_tokens / 1_000_000.0) * pricing["prompt"]
        completion_cost = (completion_tokens / 1_000_000.0) * pricing["completion"]
        total = prompt_cost + completion_cost
        return {
            "model": model,
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "total_tokens": prompt_tokens + completion_tokens,
            "estimated_cost_usd": round(total, 6),
        }
