"""Unit tests for streaming generator."""

import unittest
from rag_evals.generation.streaming import StreamingGroundedGenerator

class TestStreaming(unittest.TestCase):
    def test_streaming_tokens(self):
        text = "This is a streamed answer with citations [c1]."
        streamed = list(StreamingGroundedGenerator.stream_answer(text, delay=0.0))
        self.assertEqual("".join(streamed), text)

if __name__ == "__main__":
    unittest.main()
