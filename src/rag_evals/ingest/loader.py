"""Load documents from raw files with metadata preservation."""

from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Dict, Any

@dataclass
class Document:
    doc_id: str
    content: str
    metadata: Dict[str, Any] = field(default_factory=dict)

    @property
    def file_name(self) -> str:
        return self.metadata.get("file_name", "")

    @property
    def page_number(self) -> int:
        return self.metadata.get("page_number", 1)

class DocumentLoader:
    """Loads plain text, markdown, or PDF documents into structured Document objects."""

    @staticmethod
    def load_file(file_path: Path) -> List[Document]:
        file_path = Path(file_path)
        if not file_path.is_file():
            raise FileNotFoundError(f"File not found: {file_path}")

        suffix = file_path.suffix.lower()
        if suffix in (".txt", ".md"):
            return DocumentLoader._load_text(file_path)
        elif suffix == ".pdf":
            return DocumentLoader._load_pdf(file_path)
        else:
            raise ValueError(f"Unsupported file format: {suffix}")

    @staticmethod
    def _load_text(file_path: Path) -> List[Document]:
        text = file_path.read_text(encoding="utf-8")
        # Approximate 500-word pages for text files
        paragraphs = text.split("\n\n")
        pages = []
        current_page_text = []
        current_word_count = 0
        page_num = 1

        for para in paragraphs:
            para = para.strip()
            if not para:
                continue
            words = len(para.split())
            if current_word_count + words > 450 and current_page_text:
                pages.append(Document(
                    doc_id=f"{file_path.stem}_p{page_num}",
                    content="\n\n".join(current_page_text),
                    metadata={
                        "file_name": file_path.name,
                        "file_path": str(file_path),
                        "page_number": page_num
                    }
                ))
                page_num += 1
                current_page_text = [para]
                current_word_count = words
            else:
                current_page_text.append(para)
                current_word_count += words

        if current_page_text:
            pages.append(Document(
                doc_id=f"{file_path.stem}_p{page_num}",
                content="\n\n".join(current_page_text),
                metadata={
                    "file_name": file_path.name,
                    "file_path": str(file_path),
                    "page_number": page_num
                }
            ))
        return pages

    @staticmethod
    def _load_pdf(file_path: Path) -> List[Document]:
        try:
            from pypdf import PdfReader
            reader = PdfReader(str(file_path))
            docs = []
            for i, page in enumerate(reader.pages):
                text = page.extract_text() or ""
                docs.append(Document(
                    doc_id=f"{file_path.stem}_p{i+1}",
                    content=text.strip(),
                    metadata={
                        "file_name": file_path.name,
                        "file_path": str(file_path),
                        "page_number": i + 1
                    }
                ))
            return docs
        except ImportError:
            # Fallback if pypdf is not installed
            return DocumentLoader._load_text(file_path)
