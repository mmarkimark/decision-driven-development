# Agents & Roles

This document defines the roles and responsibilities within the Decision-Driven Development framework. "Agent" refers to any entity performing work, whether Human or Artificial Intelligence (AI).

## Human Agents

### 1. Architect / Lead
*   **Responsibility**: Governance, High-level Decisions (`DRs`), and System Consistency.
*   **Key Artifacts**: `GOVERNANCE.md`, `decisions/*.md`.
*   **Authority**: Final approver on Decisions.

### 2. Developer
*   **Responsibility**: Transforming Specs into Implementation.
*   **Key Artifacts**: Code, Tests.
*   **Authority**: Can propose Decisions and Specs.

### 3. Reviewer
*   **Responsibility**: Ensuring compliance with Governance and Quality standards.
*   **Key Artifacts**: PR Comments, Approval/Rejection.

## AI Agents

AI agents are treated as team members with specific constraints.

### 1. The Scribe (Documentation Assistant)
*   **Role**: Drafts Decisions and Specs based on prompt input.
*   **Constraint**: Cannot "Accept" a Decision. Only a Human can accept.

### 2. The Validator (Compliance Checker)
*   **Role**: Analyzing PRs to ensure `Code -> Spec -> Decision` traceability.
*   **Action**: Can block PRs if linkage is missing.

### 3. The Coder (Implementation Assistant)
*   **Role**: Generates code based *strictly* on a provided Spec.
*   **Constraint**: Must not hallucinate requirements not present in the Spec.

## Human-in-the-Loop (HITL)
*   All AI-generated artifacts (Decisions, Specs, Code) must be reviewed and explicitly accepted by a Human Agent.
*   The Human Agent assumes full liability for the AI's output.
