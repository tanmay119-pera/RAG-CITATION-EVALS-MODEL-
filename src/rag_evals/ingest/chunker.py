"""Token-aware sliding-window chunker with citation metadata."""

from dataclasses import dataclass, field
from typing import List, Dict, Any
from rag_evals.ingest.loader import Document
from rag_evals.ingest.cleaner import TextCleaner

@dataclass
class Chunk:
    chunk_id: str
    text: str
    token_count: int
    metadata: Dict[str, Any] = field(default_factory=dict)

    @property
    def section_title(self) -> str:
        return self.metadata.get("section_title", "Unknown Section")

    @property
    def page_number(self) -> int:
        return self.metadata.get("page_number", 1)

    @property
    def file_name(self) -> str:
        return self.metadata.get("file_name", "")

class Chunker:
    def __init__(self, target_chunk_tokens: int = 450, overlap_tokens: int = 50):
        self.target_tokens = target_chunk_tokens
        self.overlap = overlap_tokens

    @staticmethod
    def _approx_token_count(text: str) -> int:
        # Standard heuristic: 1 word ~= 1.3 tokens
        return max(1, int(len(text.split()) * 1.3))

    def split_document(self, doc: Document) -> List[Chunk]:
        cleaned_text = TextCleaner.clean(doc.content)
        paragraphs = cleaned_text.split("\n\n")

        chunks: List[Chunk] = []
        current_paragraphs: List[str] = []
        current_tokens = 0
        chunk_idx = 1

        for para in paragraphs:
            para = para.strip()
            if not para:
                continue
            para_tokens = self._approx_token_count(para)

            if current_tokens + para_tokens > self.target_tokens and current_paragraphs:
                chunk_text = "\n\n".join(current_paragraphs)
                section = TextCleaner.extract_section_title(chunk_text)
                chunk_id = f"{doc.metadata.get('file_name', 'doc')[:8]}_p{doc.page_number}_c{chunk_idx}"
                chunks.append(Chunk(
                    chunk_id=chunk_id,
                    text=chunk_text,
                    token_count=current_tokens,
                    metadata={
                        "file_name": doc.file_name,
                        "page_number": doc.page_number,
                        "section_title": section,
                        "chunk_index": chunk_idx
                    }
                ))
                chunk_idx += 1
                # Overlap: keep the last paragraph if possible
                if self.overlap > 0 and len(current_paragraphs) > 1:
                    last_para = current_paragraphs[-1]
                    current_paragraphs = [last_para, para]
                    current_tokens = self._approx_token_count(last_para) + para_tokens
                else:
                    current_paragraphs = [para]
                    current_tokens = para_tokens
            else:
                current_paragraphs.append(para)
                current_tokens += para_tokens

        if current_paragraphs:
            chunk_text = "\n\n".join(current_paragraphs)
            section = TextCleaner.extract_section_title(chunk_text)
            chunk_id = f"{doc.metadata.get('file_name', 'doc')[:8]}_p{doc.page_number}_c{chunk_idx}"
            chunks.append(Chunk(
                chunk_id=chunk_id,
                text=chunk_text,
                token_count=current_tokens,
                metadata={
                    "file_name": doc.file_name,
                    "page_number": doc.page_number,
                    "section_title": section,
                    "chunk_index": chunk_idx
                }
            ))

        return chunks
