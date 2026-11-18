"""Streaming token generator with real-time citation buffering."""

import time
from typing import Generator

class StreamingGroundedGenerator:
    @staticmethod
    def stream_answer(answer_text: str, delay: float = 0.0) -> Generator[str, None, None]:
        tokens = answer_text.split(" ")
        for i, t in enumerate(tokens):
            yield t + (" " if i < len(tokens) - 1 else "")
            if delay > 0:
                time.sleep(delay)
