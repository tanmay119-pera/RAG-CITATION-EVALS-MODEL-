"""Track nested section titles for chunk metadata."""
import re
from typing import List

class SectionStackTracker:
    """Maintains current heading path across markdown/policy lines."""
    def __init__(self):
        self._levels: dict = {}

    def update(self, line: str):
        m = re.match(r"^(#{1,4})\s+(.+)$", line.strip())
        if not m:
            return
        depth = len(m.group(1))
        title = m.group(2).strip()
        self._levels[depth] = title
        for k in [lv for lv in self._levels if lv > depth]:
            del self._levels[k]

    def current_path(self) -> str:
        return " > ".join(self._levels[k] for k in sorted(self._levels)) or "Root"
