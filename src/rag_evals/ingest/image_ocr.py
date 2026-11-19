"""Multi-modal OCR extractor for scanned policy documents and figures."""

import re
from pathlib import Path
from typing import Optional

class DocumentOCRExtractor:
    """Extracts textual content from scanned document images with fallback parsing."""

    @staticmethod
    def extract_text(image_path: Path) -> str:
        # Graceful fallback when tesseract is not available
        try:
            import pytesseract
            from PIL import Image
            img = Image.open(image_path)
            return pytesseract.image_to_string(img)
        except Exception:
            return f"[EXTRACTED_OCR_IMAGE: {image_path.name}]"
