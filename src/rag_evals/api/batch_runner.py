"""Run batch evaluation queries across mock/live RAG pipelines."""
from typing import Callable, List, Dict, Any

class BatchPipelineRunner:
    """Executes ordered queries against any callable pipeline function."""
    def __init__(self, pipeline_fn: Callable[[str], Dict[str, Any]]):
        self.pipeline_fn = pipeline_fn

    def run_all(self, queries: List[str]) -> List[Dict[str, Any]]:
        results = []
        for q in queries:
            res = self.pipeline_fn(q)
            results.append({"query": q, **res})
        return results
