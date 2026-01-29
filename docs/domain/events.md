# Domain Events

These events represent significant state transitions within the Decision-Driven Development lifecycle.

## 1. Governance Events

### `DecisionProposed`
*   **Trigger**: A new `DR-XXX.md` file is created with status `Proposed`.
*   **Meaning**: The organization is considering a new rule.
*   **Action**: Review process begins.

### `DecisionAccepted`
*   **Trigger**: A `DR-XXX.md` file status changes to `Accepted` (via PR merge).
*   **Meaning**: The rule is now Law. All future work must comply.
*   **Side Effect**: May trigger `DecisionSuperseded` for older records.

### `DecisionRejected`
*   **Trigger**: A `DR-XXX.md` file status changes to `Rejected`.
*   **Meaning**: The proposal is dead.

## 2. Specification Events

### `UseCaseDefined`
*   **Trigger**: A new Use Case is committed to `USE_CASES/`.
*   **Meaning**: A specific functional requirement is ready for implementation.
*   **Constraint**: Must link to a valid `DecisionAccepted` event.

## 3. Execution Events

### `FastLaneTriggered`
*   **Trigger**: A branch created with `fast-lane/` prefix.
*   **Meaning**: Expedited execution path activated.
*   **Audit**: Requires `FastLaneCompleted` event to close loop.

### `PostMortemPublished`
*   **Trigger**: A new Post-Mortem document is added.
*   **Meaning**: Analysis of a failure is complete.
*   **Action**: May trigger a `DecisionProposed` event (if policy change is needed).
