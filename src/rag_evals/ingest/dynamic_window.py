"""Dynamic chunk window sizing based on text density and structure."""

class DynamicWindowAdjuster:
    """Computes optimal token targets and overlap sizes based on document characteristics."""

    @staticmethod
    def get_optimal_window(text: str, base_tokens: int = 450) -> int:
        lines = text.split("\n")
        # Dense policies with tables or bullet points prefer smaller chunks
        has_dense_lists = sum(1 for line in lines if line.strip().startswith(("-", "*", "|", "1.", "2.")))
        if has_dense_lists > 10:
            return max(200, int(base_tokens * 0.75))
        # Narrative text works better with larger context windows
        return base_tokens
