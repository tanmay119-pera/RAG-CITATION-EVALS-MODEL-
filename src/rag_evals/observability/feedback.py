"""User feedback collection and citation evaluation telemetry."""

import json
import time
from pathlib import Path
from typing import Dict, Any

class FeedbackCollector:
    """Logs end-user feedback, thumbs up/down, and citation error reports."""

    def __init__(self, log_path: Path = Path("data/feedback.jsonl")):
        self.log_path = Path(log_path)
        self.log_path.parent.mkdir(parents=True, exist_ok=True)

    def log_feedback(self, query: str, answer: str, is_helpful: bool, user_comment: str = ""):
        entry = {
            "timestamp": time.time(),
            "query": query,
            "answer": answer,
            "is_helpful": is_helpful,
            "comment": user_comment
        }
        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")
