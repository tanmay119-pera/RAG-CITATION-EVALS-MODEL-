"""Centralized system prompt templates for grounded citation generation."""

from typing import Dict

class PromptRegistry:
    TEMPLATES: Dict[str, str] = {
        "academic": """You are an academic regulations advisor. Answer strictly from the provided chunks. Cite [chunk_id] after every claim. Say 'I do not have sufficient information in the provided documents to answer this question.' if ungrounded.""",
        "legal": """You are a compliance officer. Cite the exact clause ID for every statutory rule. Do not infer beyond the written text.""",
        "concise": """Provide a direct, bullet-pointed answer citing [chunk_id] for each fact."""
    }

    @classmethod
    def get_template(cls, domain: str = "academic") -> str:
        return cls.TEMPLATES.get(domain, cls.TEMPLATES["academic"])
