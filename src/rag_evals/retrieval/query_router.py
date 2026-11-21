"""Route queries to optimal retrieval strategies."""
from typing import List, Dict, Callable
from rag_evals.retrieval.intent_classifier import IntentClassifier, QueryIntent

class QueryRouter:
    """Routes queries to registered retriever strategies based on classified intent."""
    def __init__(self):
        self.classifier = IntentClassifier()
        self.routes: Dict[QueryIntent, Callable] = {}
        self.default_strategy: Callable = None

    def register(self, intent: QueryIntent, strategy: Callable):
        self.routes[intent] = strategy

    def set_default(self, strategy: Callable):
        self.default_strategy = strategy

    def route(self, query: str) -> tuple:
        intent = self.classifier.classify(query)
        handler = self.routes.get(intent, self.default_strategy)
        return intent, handler

    def retrieve(self, query: str) -> List[Dict]:
        _, handler = self.route(query)
        if handler is None:
            return []
        return handler(query)
