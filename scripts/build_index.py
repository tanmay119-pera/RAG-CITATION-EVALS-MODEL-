"""Build both BM25 and VectorStore indexes from chunks.jsonl."""

import json
from pathlib import Path
from rag_evals.config import load_config
from rag_evals.index.bm25 import BM25Index
from rag_evals.index.vector_store import VectorStore
from rag_evals.index.embedder import GeminiEmbedder
from rag_evals.index.cache import EmbeddingCache

def build_all_indexes():
    config = load_config()
    config.ensure_directories()
    chunks_path = config.processed_data_dir / "chunks.jsonl"
    if not chunks_path.is_file():
        raise FileNotFoundError(f"Missing processed chunks: {chunks_path}")

    chunk_ids = []
    texts = []
    metadata_list = []

    with open(chunks_path, "r", encoding="utf-8") as f:
        for line in f:
            item = json.loads(line)
            chunk_ids.append(item["chunk_id"])
            texts.append(item["text"])
            meta = item["metadata"]
            meta["text"] = item["text"]
            metadata_list.append(meta)

    # 1. Build BM25
    bm25 = BM25Index()
    bm25.build(chunk_ids, texts)
    bm25_file = config.index_dir / "bm25.json"
    bm25.save(bm25_file)
    print(f"BM25 index saved: {bm25_file}")

    # 2. Build Dense Vector Store
    cache = EmbeddingCache(config.index_dir / "embedding_cache.sqlite3")
    embedder = GeminiEmbedder(config)
    vstore = VectorStore()

    for cid, txt, meta in zip(chunk_ids, texts, metadata_list):
        cached = cache.get(txt, config.embedding_model)
        if cached is None:
            cached = embedder.embed_texts([txt])[0]
            cache.put(txt, config.embedding_model, cached)
        vstore.add(cid, cached, meta)

    vstore_file = config.index_dir / "vector_store.json"
    vstore.save(vstore_file)
    print(f"VectorStore index saved: {vstore_file}")

if __name__ == "__main__":
    build_all_indexes()
