# AI Constraints & Permissions

This document defines the boundaries for Artificial Intelligence agents operating within the Decision-Driven Development methodology. It enforces the Domain-Driven Design separation of concerns.

## 1. The Prime Directive
**AI Agents are Subordinate to Human Governance.**
An AI Agent can never authorize a Policy. It can only propose, validate, or implement.

## 2. Layer-Specific Constraints

### Domain Layer (`DECISIONS/`, `GOVERNANCE/`)
*   **Permission**: `READ`, `DRAFT`
*   **Prohibition**: `AUTHORIZE`, `DELETE`
*   **Constraint**: An AI Agent **MUST NOT** change the status of a Decision Record to `Accepted`. Only a Human can Ratify a Decision.
*   **Constraint**: An AI Agent **MUST NOT** modify the text of an `Accepted` Decision (except for explicit "Janitorial" tasks requested by a human).

### Application Layer (`USE_CASES/`, `Fast-Lanes`)
*   **Permission**: `READ`, `WRITE`
*   **Constraint**: An AI Agent generated Use Case **MUST** explicitly cite the Decision ID (`DR-XXX`) it derives from.
*   **Constraint**: An AI Agent **MUST NOT** invent requirements that contradict the cited Decision.

### Infrastructure Layer (Code, Git, Tests)
*   **Permission**: `READ`, `WRITE`, `EXECUTE`
*   **Constraint**: An AI Agent **MUST NOT** commit code that fails the derivation check (i.e., code without a spec).
*   **Constraint**: An AI Agent **MUST** run all `NON_FUNCTIONAL` checks before requesting review.

## 3. The "Hallucination Firewall"
To prevent AI hallucinations from polluting the Domain:
1.  **Reference Check**: AI must provide links/paths to the specific Decision files it is relying on.
2.  **Scope Containment**: If an AI cannot find a Decision to support a requested feature, it **MUST** stop and request Human intervention (Proposal of a new Decision). It **MUST NOT** infer the policy.

## 4. Meta-Governance
*   **Self-Modification**: AI Agents are **FORBIDDEN** from modifying `AGENTS.md` or this file (`AI_CONSTRAINTS.md`) unless explicitly instructed by a Human Architect as part of a formal Governance upgrade.
