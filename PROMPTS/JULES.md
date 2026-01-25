# AI-Assisted Development Practices

This document outlines how to integrate AI into the Decision-Driven Development workflow effectively and safely.

## Core Principle
**AI is an accelerator, not a replacement for intent.**
AI can suggest the "How", but the "Why" (Decision) and "What" (Spec) must be strictly governed by Human intent (even if drafted by AI).

## Prompt Engineering as Governance
*   Prompts should include context about the Governance rules.
*   **System Prompt**: "You are an assistant in a Decision-Driven Development environment. Do not suggest code without a Spec. Do not suggest a Spec without a Decision."

## Workflow Integration

### 1. AI in Decision Making
*   **Use**: Brainstorming alternatives, summarizing trade-offs, drafting the `Consequences` section of a DR.
*   **Don't**: Letting AI decide the trade-off.

### 2. AI in Spec Writing
*   **Use**: Generating edge cases, formatting requirements, ensuring NFRs are addressed.
*   **Don't**: Generating features not requested by the Decision.

### 3. AI in Implementation
*   **Use**: "Here is the Spec [Link]. Write the code to satisfy it."
*   **Verification**: The test suite (derived from the Spec) determines if the AI did its job.

## Mixed Workflows
*   **Handoffs**: Clear boundaries. e.g., Human writes Decision -> AI drafts Spec -> Human refines Spec -> AI writes Code -> Human reviews Code.
*   **Transparency**: PR descriptions should indicate if code was AI-generated.
