"""Fetch and prepare the real-world document corpus for RAG ingestion."""

import argparse
import hashlib
import json
from pathlib import Path
from rag_evals.config import load_config

SAMPLE_URL = "https://raw.githubusercontent.com/tanmay119-pera/corpus-source/main/academic_regulations.txt"

def compute_sha256(filepath: Path) -> str:
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest()

def generate_manifest(raw_dir: Path, output_file: Path) -> dict:
    files = sorted(list(raw_dir.glob("*.txt")) + list(raw_dir.glob("*.pdf")) + list(raw_dir.glob("*.md")))
    manifest = {
        "corpus_name": "University Academic Regulations & Policy Handbook",
        "total_documents": len(files),
        "documents": []
    }
    for file in files:
        manifest["documents"].append({
            "filename": file.name,
            "bytes": file.stat().st_size,
            "sha256": compute_sha256(file),
            "format": file.suffix.lstrip(".")
        })
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
    return manifest

def main():
    parser = argparse.ArgumentParser(description="Acquire corpus documents and write manifest.")
    parser.add_argument("--output-dir", default=None, help="Directory to store raw corpus")
    args = parser.parse_args()

    config = load_config()
    raw_dir = Path(args.output_dir) if args.output_dir else config.raw_data_dir
    raw_dir.mkdir(parents=True, exist_ok=True)

    manifest_path = config.raw_data_dir.parent / "corpus_manifest.json"
    manifest = generate_manifest(raw_dir, manifest_path)
    print(f"Corpus manifest written with {manifest['total_documents']} documents.")

if __name__ == "__main__":
    main()
