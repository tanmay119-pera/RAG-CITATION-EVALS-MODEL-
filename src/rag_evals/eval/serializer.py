"""Serialize evaluation metrics to JSON, CSV, and markdown."""
import json, csv, io
from typing import List, Dict

class EvalSerializer:
    """Encodes evaluation metric dictionaries into multiple reporting formats."""
    def to_json(self, rows: List[Dict]) -> str:
        return json.dumps(rows, indent=2)

    def to_csv(self, rows: List[Dict]) -> str:
        if not rows: return ""
        buf = io.StringIO()
        w = csv.DictWriter(buf, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
        return buf.getvalue()

    def to_markdown(self, rows: List[Dict]) -> str:
        if not rows: return ""
        keys = list(rows[0].keys())
        lines = ["| " + " | ".join(keys) + " |", "| " + " | ".join(["---"] * len(keys)) + " |"]
        for r in rows:
            lines.append("| " + " | ".join(str(r.get(k, "")) for k in keys) + " |")
        return "\n".join(lines)
