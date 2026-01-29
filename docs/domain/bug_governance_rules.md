# Bug Governance Rules

This document defines how "Bugs" are treated within the Domain Model. A Bug is not just an error; it is a signal of misalignment between layers.

## 1. Taxonomy of Bugs

### Type A: Implementation Defect (Application Layer)
*   **Definition**: The Code does not behave as the Spec says it should.
*   **Root Cause**: Coding error, configuration error, infrastructure failure.
*   **Resolution**: **Fast-Lane**. Fix the code to match the Spec.
*   **Governance**: Low. No Decision change required.

### Type B: Specification Defect (Domain/App Boundary)
*   **Definition**: The Code does exactly what the Spec says, but the result is wrong/harmful.
*   **Root Cause**: The Spec failed to account for a scenario, or the logic in the Spec is flawed.
*   **Resolution**: **Update Spec** (and potentially Code).
*   **Governance**: Medium. Requires Use Case review.

### Type C: Policy Failure (Domain Layer)
*   **Definition**: The System is behaving "correctly" according to Specs and Decisions, but the outcome is unacceptable (e.g., unintended business consequence).
*   **Root Cause**: The Decision (Policy) itself is flawed.
*   **Resolution**: **New Decision**.
*   **Governance**: High. Requires full Decision Derivation Cycle.

## 2. Escalation Protocol

1.  **Triage**: Identify the Taxonomy (A, B, or C).
2.  **Constraint**: You cannot fix a Type C bug with a Type A solution. (Do not "hack" the code to bypass a bad policy; change the policy).
3.  **Audit**: All Type C bugs must result in a Post-Mortem linked to the new Decision.

## 3. The "Stop the Bleeding" Exception
In a Critical Severity event (Data Loss, Security Breach), a temporary "Technical Bypass" (Fast-Lane) is permitted to stabilize the system, even if it contradicts a policy.
*   **Condition**: A Retroactive Decision MUST be filed immediately (within 24 hours) to legitimize or correct the bypass.
