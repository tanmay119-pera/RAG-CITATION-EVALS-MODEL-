"""Input text normalizer and invisible character sanitizer."""
import re
import unicodedata

class InputSanitizer:
    """Strips zero-width spaces, controls, and normalizes Unicode."""
    def sanitize(self, text: str) -> str:
        # Normalize Unicode NFC
        text = unicodedata.normalize("NFC", text)
        # Strip zero-width and control characters
        text = re.sub(r"[\u200B-\u200D\uFEFF]", "", text)
        # Strip raw HTML tags
        text = re.sub(r"<[^>]+>", "", text)
        # Collapse excessive whitespace
        text = re.sub(r"\s+", " ", text).strip()
        return text
