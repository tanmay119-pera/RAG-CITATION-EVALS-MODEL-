"""Runtime environment readiness inspector."""
import os, sys
from typing import Dict, Any

class EnvironmentInspector:
    """Checks Python runtime compatibility and configured providers."""

    @staticmethod
    def report() -> Dict[str, Any]:
        return {
            "python_version": sys.version.split()[0],
            "has_gemini_key": bool(os.getenv("GEMINI_API_KEY")),
            "offline_mock_ready": True,
        }
