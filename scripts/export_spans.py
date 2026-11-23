#!/usr/bin/env python3
"""Dump OpenTelemetry execution spans to stdout."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from rag_evals.observability.span_exporter import SpanExporter

def main():
    exp = SpanExporter()
    exp.record_span("demo_trace", "bm25_retrieval", 12.4, {"k": 5})
    print(exp.export_json())

if __name__ == "__main__":
    main()
