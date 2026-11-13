"""Configuration management for the RAG Citation & Evals system."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Mapping


def _parse_bool(value: str | bool | None, default: bool = False) -> bool:
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    return value.strip().lower() in {"1", "true", "yes", "on"}


def _read_env_file(path: Path) -> dict[str, str]:
    """Parse a simple KEY=VALUE .env file without external dependencies."""
    env_vars: dict[str, str] = {}
    if not path.is_file():
        return env_vars

    with open(path, "r", encoding="utf-8") as f:
        for raw_line in f:
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, val = line.split("=", 1)
            key = key.strip()
            val = val.strip().strip("'\"")
            if key:
                env_vars[key] = val
    return env_vars


@dataclass
class AppConfig:
    """Strongly typed application configuration."""

    gemini_api_key: str = ""
    embedding_model: str = "gemini-embedding-001"
    generation_model: str = "gemini-3.8-flash"

    chunk_size_tokens: int = 450
    chunk_overlap_tokens: int = 50

    top_k_retrieve: int = 10
    top_n_rerank: int = 5
    use_hybrid: bool = True
    use_reranker: bool = True

    raw_data_dir: Path = field(default_factory=lambda: Path("data/raw"))
    processed_data_dir: Path = field(default_factory=lambda: Path("data/processed"))
    index_dir: Path = field(default_factory=lambda: Path("data/index"))
    eval_dir: Path = field(default_factory=lambda: Path("data/eval"))

    def ensure_directories(self) -> None:
        """Create configured data directories if they do not exist."""
        for path in (
            self.raw_data_dir,
            self.processed_data_dir,
            self.index_dir,
            self.eval_dir,
        ):
            path.mkdir(parents=True, exist_ok=True)

    @property
    def has_api_key(self) -> bool:
        """Check if a Gemini API key is configured."""
        return bool(self.gemini_api_key.strip())


def load_config(
    env_path: Path | str | None = None,
    overrides: Mapping[str, str] | None = None,
) -> AppConfig:
    """Load configuration from environment, .env file, and optional overrides."""
    source_env: dict[str, str] = {}

    target_env_file = Path(env_path) if env_path else Path(".env")
    if target_env_file.is_file():
        source_env.update(_read_env_file(target_env_file))

    # os.environ takes precedence over .env file
    source_env.update(dict(os.environ))

    # explicit overrides take highest precedence
    if overrides:
        source_env.update(overrides)

    raw_data = Path(source_env.get("RAW_DATA_DIR", "data/raw"))
    processed_data = Path(source_env.get("PROCESSED_DATA_DIR", "data/processed"))
    index_dir = Path(source_env.get("INDEX_DIR", "data/index"))
    eval_dir = Path(source_env.get("EVAL_DIR", "data/eval"))

    return AppConfig(
        gemini_api_key=source_env.get("GEMINI_API_KEY", "").strip(),
        embedding_model=source_env.get("EMBEDDING_MODEL", "gemini-embedding-001").strip(),
        generation_model=source_env.get("GENERATION_MODEL", "gemini-3.8-flash").strip(),
        chunk_size_tokens=int(source_env.get("CHUNK_SIZE_TOKENS", 450)),
        chunk_overlap_tokens=int(source_env.get("CHUNK_OVERLAP_TOKENS", 50)),
        top_k_retrieve=int(source_env.get("TOP_K_RETRIEVE", 10)),
        top_n_rerank=int(source_env.get("TOP_N_RERANK", 5)),
        use_hybrid=_parse_bool(source_env.get("USE_HYBRID"), default=True),
        use_reranker=_parse_bool(source_env.get("USE_RERANKER"), default=True),
        raw_data_dir=raw_data,
        processed_data_dir=processed_data,
        index_dir=index_dir,
        eval_dir=eval_dir,
    )
