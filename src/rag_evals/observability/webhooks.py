"""Webhook notification dispatcher for pipeline lifecycle events."""
import time
from typing import List, Dict, Callable, Optional
from enum import Enum

class EventType(Enum):
    INGESTION_DONE = "ingestion_done"
    EVAL_DONE = "eval_done"
    ALERT = "alert"

class WebhookManager:
    """Dispatches asynchronous notification events to registered webhooks."""
    def __init__(self):
        self.subscribers: List[Dict] = []
        self.delivery_log: List[Dict] = []

    def subscribe(self, url: str, events: List[EventType]):
        self.subscribers.append({"url": url, "events": events})

    def dispatch(self, event: EventType, payload: Dict, sender: Optional[Callable] = None):
        entry = {"event": event.value, "payload": payload, "ts": time.time()}
        for s in self.subscribers:
            if event in s["events"]:
                status = "sent" if sender and sender(s["url"], entry) else "recorded"
                self.delivery_log.append({"url": s["url"], "status": status, **entry})
