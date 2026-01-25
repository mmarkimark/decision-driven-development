# Workflow & Process

This document defines the operational workflow for the Decision-Driven Development framework.

## Git Workflow

We follow a strict Feature Branch workflow.
*   **`main`**: The source of truth. Protected. No direct commits.
*   **Branches**: Created for each Decision, Spec, or Implementation task.
    *   Format: `type/ID-short-description` (e.g., `decision/DR-001-init`, `feat/UC-005-login`).

## Pull Request (PR) Lifecycle

Every change requires a PR. The PR description must answer:
1.  **What** is changing?
2.  **Why** is it changing? (Link to Decision/Spec)
3.  **How** was it verified?

### Validation Rules

The following rules are enforced (manually or via CI):

1.  **Code Changes**: Must reference an approved **Spec** (`UC-XXXX`).
    *   *Violation*: PR is blocked.
2.  **Spec Changes**: Must reference an approved **Decision** (`DR-XXXX`).
    *   *Violation*: PR is blocked.
3.  **Decision Changes**: Must follow the Decision Process (Discussion -> Accept).
    *   *Note*: Decisions are immutable. Editing a decision usually means fixing typos or marking it as superseded.

## Review Process

*   **Reviewers**: At least one human reviewer is required for Decisions and Specs.
*   **AI Review**: AI agents can perform preliminary reviews (linting, NFR checks, consistency checks).

## Definition of Done

*   **Decision**: Accepted and merged.
*   **Spec**: Approved and merged.
*   **Code**: Tests pass, NFRs met, linked to Spec, merged.
