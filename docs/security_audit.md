# Security Audit Report

## Audit Scope
- Input validation and injection attacks
- PII filtering
- Prompt leakage containment
- Resource exhaustion mitigations

## Audit Summary
- **Prompt Injection Defense**: Guardrails in `security/guardrails.py` block pattern-based jailbreaks.
- **PII Scrubbing**: Regex scrubber removes emails, phone numbers, and IDs before LLM prompts.
- **Output Sanitization**: System prompt boundary protection verified via `output_guard.py`.
- **Throttling**: Token bucket rate limiter restricts bursts to safe bounds.
