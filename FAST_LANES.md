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
