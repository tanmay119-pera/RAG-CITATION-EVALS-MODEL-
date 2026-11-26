#!/usr/bin/env python3
"""Audit golden dataset integrity."""
import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from rag_evals.eval.golden_audit import GoldenSetAuditor

def main():
    candidates = list(Path("data").rglob("*eval*.json")) if Path("data").exists() else []
    if not candidates:
        print("No dataset file specified; sample audit:", GoldenSetAuditor.audit([]))
        return
    data = json.loads(candidates[0].read_text())
    rows = data if isinstance(data, list) else data.get("cases", [])
    print(json.dumps(GoldenSetAuditor.audit(rows), indent=2))

if __name__ == "__main__":
    main()
