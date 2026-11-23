# Hallucination Mitigation Guide

## Strategy
1. **Source Grounding**: Pass labeled chunk identifiers in the system prompt.
2. **Lexical Overlap Verification**: Compute factual keyword coverage with `HallucinationGrader`.
3. **Programmatic Citation Check**: Ensure every claim is cited with existing chunk IDs.
4. **Strict Refusal**: Return fallback refusal when retrieved contexts do not provide direct evidence.
