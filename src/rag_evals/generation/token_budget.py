"""Track and enforce token budgets per query."""
from dataclasses import dataclass, field

@dataclass
class TokenBudget:
    """Tracks token usage against configured maximum limits."""
    max_prompt_tokens: int = 3000
    max_completion_tokens: int = 1000
    _prompt_used: int = field(default=0, init=False)
    _completion_used: int = field(default=0, init=False)

    @property
    def prompt_remaining(self) -> int:
        return max(0, self.max_prompt_tokens - self._prompt_used)

    @property
    def completion_remaining(self) -> int:
        return max(0, self.max_completion_tokens - self._completion_used)

    def consume_prompt(self, tokens: int) -> bool:
        if self._prompt_used + tokens > self.max_prompt_tokens:
            return False
        self._prompt_used += tokens
        return True

    def consume_completion(self, tokens: int) -> bool:
        if self._completion_used + tokens > self.max_completion_tokens:
            return False
        self._completion_used += tokens
        return True

    def reset(self):
        self._prompt_used = 0
        self._completion_used = 0

    def usage_report(self) -> dict:
        return {
            "prompt": {"used": self._prompt_used, "max": self.max_prompt_tokens, "remaining": self.prompt_remaining},
            "completion": {"used": self._completion_used, "max": self.max_completion_tokens, "remaining": self.completion_remaining},
        }
