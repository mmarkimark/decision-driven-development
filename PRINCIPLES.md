# Core Principles

This document outlines the inviolable principles of the Decision-Driven Development framework.

## 1. Decisions are Immutable
Once a Decision Record (DR) is accepted and merged, it is **immutable**. It captures the context and agreement at a point in time.
*   To change a decision, a new Decision Record must be created that explicitly supersedes the previous one.
*   We do not rewrite history.

## 2. Derivation Chain
The flow of value and truth is unidirectional:
`Decision -> Use Case (Spec) -> Implementation`
*   **Decisions** define the constraints and direction.
*   **Use Cases** derive strictly from Decisions.
*   **Implementation** derives strictly from Use Cases.
*   Backward flow (changing a Decision to fit Code) is forbidden.

## 3. Explicit Over Implicit
*   Nothing is assumed.
*   If it is not documented in a Decision or Spec, it does not exist.
*   "Tribal knowledge" is considered a failure of governance.

## 4. First-Class Non-Functional Requirements
*   Non-Functional Requirements (NFRs) such as security, performance, and scalability are not appendices.
*   They must be explicitly defined in Decisions and Specs.

## 5. Fast Lanes are Explicit
*   Shortcuts (Fast Lanes) are permitted but must be explicitly defined and documented.
*   They are never the default mode of operation.
*   Use of a Fast Lane requires explicit justification.

## 6. Tool-Agnosticism
*   The methodology does not depend on specific tools (e.g., GitHub, Jira, specific AI models).
*   It depends on artifacts (files) and processes that can be implemented in any version control system.
