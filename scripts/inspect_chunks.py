#!/usr/bin/env python3
"""Inspect stored chunk metadata summary."""
import json
from pathlib import Path

def main():
    p = Path("data/processed/chunks.jsonl")
    if not p.exists():
        print("No processed chunks yet.")
        return
    rows = [json.loads(l) for l in p.read_text().splitlines() if l.strip()]
    print(f"Loaded {len(rows)} chunks.")

if __name__ == "__main__":
    main()
