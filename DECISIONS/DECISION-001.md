# DECISION-001 — Adopt Decision-Driven Development

## Status
Accepted

## Date
2023-10-27

## Context
Software development often suffers from "drift," where code diverges from intent, and "amnesia," where the reasons for past choices are lost. We need a rigorous framework to ensure that every line of code is traceable to a specific requirement and intent, especially in an AI-assisted environment where code generation speed can outpace human understanding.

## Decision
We will adopt the **Decision-Driven Development** framework.
1.  **Governance-First**: All work begins with Governance rules.
2.  **Decision-Centric**: No features without a recorded Decision (`DR`).
3.  **Spec-Driven**: No code without a Specification (`UC`) derived from a Decision.
4.  **Immutable History**: Decisions are never deleted or rewritten, only superseded.

## Rationale
<!-- ACTION: to be defined by human decision owner -->

## Impact
### Positive
*   **Traceability**: Complete lineage from Code -> Spec -> Decision.
*   **Clarity**: "Why" is always answered before "How".
*   **AI Safety**: Limits AI hallucination by constraining generation to specific Specs.

### Negative
*   **Overhead**: Requires more upfront writing and review.
*   **Friction**: Slows down "quick hacks" or "cowboy coding" (intentionally).

## References
*   [UC-001] Create a Decision Record
