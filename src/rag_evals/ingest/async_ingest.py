"""Concurrent multi-threaded document loader for high-throughput batch ingestion."""

import concurrent.futures
from pathlib import Path
from typing import List
from rag_evals.ingest.loader import Document, DocumentLoader

class ConcurrentLoader:
    """Loads multiple documents concurrently across thread workers."""

    def __init__(self, max_workers: int = 4):
        self.max_workers = max_workers

    def load_files(self, file_paths: List[Path]) -> List[Document]:
        documents = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_file = {executor.submit(DocumentLoader.load_file, fp): fp for fp in file_paths}
            for future in concurrent.futures.as_completed(future_to_file):
                try:
                    docs = future.result()
                    documents.extend(docs)
                except Exception as e:
                    print(f"Error loading {future_to_file[future]}: {e}")
        return documents
