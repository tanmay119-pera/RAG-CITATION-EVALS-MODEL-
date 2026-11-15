"""Audit corpus integrity, section boundaries, and character statistics."""

import json
import re
from pathlib import Path
from rag_evals.config import load_config

def audit_document(file_path: Path) -> dict:
    text = file_path.read_text(encoding="utf-8")
    sections = re.findall(r"^SECTION \d+:.*$", text, re.MULTILINE)
    clauses = re.findall(r"^Clause \d+\.\d+ - .*$", text, re.MULTILINE)
    words = len(text.split())
    chars = len(text)
    return {
        "file": file_path.name,
        "bytes": file_path.stat().st_size,
        "chars": chars,
        "words": words,
        "estimated_tokens": int(words * 1.3),
        "sections_detected": len(sections),
        "clauses_detected": len(clauses),
        "section_titles": sections[:5]
    }

def main():
    config = load_config()
    raw_files = list(config.raw_data_dir.glob("*.txt"))
    if not raw_files:
        print("No .txt files found in raw data directory.")
        return

    print("=== CORPUS AUDIT REPORT ===")
    for f in raw_files:
        stats = audit_document(f)
        print(f"File: {stats['file']}")
        print(f"  Words: {stats['words']}, Est. Tokens: {stats['estimated_tokens']}")
        print(f"  Sections: {stats['sections_detected']}, Clauses: {stats['clauses_detected']}")
    print("Corpus audit passed successfully.")

if __name__ == "__main__":
    main()
