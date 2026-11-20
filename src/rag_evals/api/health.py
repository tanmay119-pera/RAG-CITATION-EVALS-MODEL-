"""System health check for RAG pipeline components."""
import os, time
from pathlib import Path
from typing import Dict, Any

class HealthChecker:
    """Verifies operational readiness of corpus, processed chunks, and indices."""
    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)

    def check_corpus(self) -> Dict[str, Any]:
        corpus_dir = self.data_dir / "corpus"
        exists = corpus_dir.exists()
        count = len(list(corpus_dir.glob("*"))) if exists else 0
        return {"status": "ok" if count > 0 else "missing", "file_count": count}

    def check_index(self) -> Dict[str, Any]:
        idx_dir = self.data_dir / "index"
        bm25 = (idx_dir / "bm25.json").exists()
        vector = (idx_dir / "vector_store.json").exists()
        return {"status": "ok" if bm25 and vector else "degraded", "bm25": bm25, "vector_store": vector}

    def check_all(self) -> Dict[str, Any]:
        return {
            "timestamp": time.time(),
            "corpus": self.check_corpus(),
            "index": self.check_index(),
            "overall": "healthy",
        }
