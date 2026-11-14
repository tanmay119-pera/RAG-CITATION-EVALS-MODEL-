"""Map text span offsets back to PDF source page numbers."""
from typing import List, Tuple

class PageOffsetMapper:
    """Resolves character offsets across concatenated multi-page text."""
    def __init__(self, page_lengths: List[int]):
        self.boundaries: List[Tuple[int, int, int]] = []
        cursor = 0
        for idx, length in enumerate(page_lengths, start=1):
            self.boundaries.append((idx, cursor, cursor + length))
            cursor += length

    def page_for_offset(self, offset: int) -> int:
        for page_num, start, end in self.boundaries:
            if start <= offset < end:
                return page_num
        return self.boundaries[-1][0] if self.boundaries else 1
