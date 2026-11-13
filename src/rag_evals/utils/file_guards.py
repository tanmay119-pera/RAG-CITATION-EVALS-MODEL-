"""Filesystem path validation helpers."""
from pathlib import Path
from typing import Iterable

class PathValidator:
    """Prevents directory escapes and filters allowed corpus extensions."""

    @staticmethod
    def is_within_base(base_dir: Path, target_path: Path) -> bool:
        try:
            target_path.resolve().relative_to(base_dir.resolve())
            return True
        except ValueError:
            return False

    @staticmethod
    def has_allowed_extension(path: Path, allowed: Iterable[str]) -> bool:
        norm = {ext.lower() if ext.startswith(".") else f".{ext.lower()}" for ext in allowed}
        return path.suffix.lower() in norm
