"""Tests for PathValidator."""
import unittest
from pathlib import Path
from rag_evals.utils.file_guards import PathValidator

class TestPathValidator(unittest.TestCase):
    def test_within_base(self):
        base = Path("/tmp/corpus")
        self.assertTrue(PathValidator.is_within_base(base, base / "doc.pdf"))
        self.assertFalse(PathValidator.is_within_base(base, Path("/etc/passwd")))

    def test_extensions(self):
        self.assertTrue(PathValidator.has_allowed_extension(Path("a.PDF"), ["pdf", "txt"]))
        self.assertFalse(PathValidator.has_allowed_extension(Path("a.exe"), ["pdf", "txt"]))
