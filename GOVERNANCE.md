# Governance

This document establishes the governance model for the Decision-Driven Development framework. It serves as the constitution for the project, defining how decisions are made, how work is organized, and the hierarchy of authority.

## Core Philosophy

**Governance-First**: Governance is not an afterthought; it is the foundation. All development activities, whether performed by humans or AI, must align with the established governance rules.

**Decision-Driven**: We prioritize the "Why" and "What" over the "How". Decisions record the intent and constraints that guide all subsequent work.

**Spec-Driven**: Implementation is a derivative of specifications. We do not code into the void; we code to satisfy a specific, documented requirement.

## Document Hierarchy

The following hierarchy establishes the precedence of documentation:

1.  **Governance (`GOVERNANCE.md`, `PRINCIPLES.md`)**: The supreme laws of the project. These define the rules of engagement.
2.  **Decisions (`decisions/*.md`)**: Immutable records of architectural, design, and process choices. A Decision constrains the solution space.
3.  **Use Cases / Specs (`specs/*.md`)**: Functional and non-functional specifications derived strictly from Decisions. These define the expected behavior.
4.  **Implementation**: The code, configuration, and artifacts that realize the Specs.

## Authority and Compliance

*   **Humans and AI**: Both human developers and AI agents are subject to the same governance rules.
*   **Traceability**: Every line of code must be traceable to a Spec. Every Spec must be traceable to a Decision (or a set of Decisions).
*   **Violation**: Changes that violate this hierarchy (e.g., "Cowboy Coding" without specs) will be rejected during PR validation.
