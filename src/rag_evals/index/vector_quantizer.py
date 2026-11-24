"""8-bit scalar vector quantizer for reduced memory footprint."""
import math
from typing import List, Tuple

class ScalarQuantizer:
    """Quantizes float32 vectors to uint8 with min-max scaling."""
    def quantize(self, vector: List[float]) -> Tuple[List[int], float, float]:
        if not vector:
            return [], 0.0, 1.0
        v_min = min(vector)
        v_max = max(vector)
        v_range = v_max - v_min if v_max != v_min else 1.0
        q = [int(round(255.0 * (x - v_min) / v_range)) for x in vector]
        return q, v_min, v_max

    def dequantize(self, q_vector: List[int], v_min: float, v_max: float) -> List[float]:
        v_range = v_max - v_min
        return [round(v_min + (x / 255.0) * v_range, 4) for x in q_vector]
