"""Ingest raw documents, clean text, split into chunks, and output chunks.jsonl."""

import json
from pathlib import Path
from rag_evals.config import load_config
from rag_evals.ingest.loader import DocumentLoader
from rag_evals.ingest.chunker import Chunker

def run_ingestion() -> Path:
    config = load_config()
    config.ensure_directories()
    raw_files = sorted(list(config.raw_data_dir.glob("*.txt")) + list(config.raw_data_dir.glob("*.pdf")))
    if not raw_files:
        raise RuntimeError("No raw documents found in data/raw")

    chunker = Chunker(
        target_chunk_tokens=config.chunk_size_tokens,
        overlap_tokens=config.chunk_overlap_tokens
    )

    all_chunks = []
    for file in raw_files:
        docs = DocumentLoader.load_file(file)
        for d in docs:
            chunks = chunker.split_document(d)
            all_chunks.extend(chunks)

    output_path = config.processed_data_dir / "chunks.jsonl"
    with open(output_path, "w", encoding="utf-8") as f:
        for c in all_chunks:
            record = {
                "chunk_id": c.chunk_id,
                "text": c.text,
                "token_count": c.token_count,
                "metadata": c.metadata
            }
            f.write(json.dumps(record) + "\n")

    print(f"Ingestion complete: Generated {len(all_chunks)} chunks -> {output_path}")
    return output_path

if __name__ == "__main__":
    run_ingestion()
