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
# Fast Lanes

Fast Lanes are explicit, documented exceptions to the standard full process (Decision -> Spec -> Code). They are used to optimize for speed in specific, low-risk scenarios.

**WARNING**: Fast Lanes are **not** the default. They are valid only for the scenarios listed below.

## 1. Hotfix Lane
**Scenario**: Critical production bug requiring immediate resolution.
*   **Process**:
    1.  Create branch `hotfix/incident-ID`.
    2.  Fix code.
    3.  **Post-Mortem**: A Decision (`DR`) and Spec (`UC`) must be retroactively created to document the fix and prevent recurrence within 24 hours.
*   **Approval**: Expedited review (1 senior engineer).

## 2. Documentation Lane
**Scenario**: Typos, clarification of comments, or updating `README` files (excluding Governance/Principles).
*   **Process**:
    1.  Direct PR to `main`.
    2.  No Decision or Spec required.
*   **Approval**: Standard review.

## 3. Dependency Update Lane
**Scenario**: Minor version updates of dependencies (e.g., security patches).
*   **Process**:
    1.  Automated PR or manual branch.
    2.  Must pass all existing tests.
    3.  No new Spec required unless functionality changes.
*   **Approval**: CI Pass + 1 Review.

## 4. Experimental / PoC Lane
**Scenario**: Exploration to inform a future Decision.
*   **Process**:
    1.  Code must live in a dedicated `experiments/` directory or a separate branch that is NEVER merged to `main` as production code.
    2.  **Output**: A Decision Record (`DR`) summarizing findings.
*   **Restriction**: PoC code cannot be promoted to production without going through the standard Decision -> Spec pipeline.
