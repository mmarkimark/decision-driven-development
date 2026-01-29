# Value Objects

These Value Objects define the standard types and enumerations used within the Decision-Driven Development domain.

## 1. Decision Status
Represents the lifecycle state of a Decision Record.

*   **Proposed**: Draft stage. Open for discussion. Not binding.
*   **Accepted**: Ratified by Governance. Binding. Immutable.
*   **Rejected**: Discussed but denied. Kept for historical context.
*   **Superseded**: Replaced by a newer Decision. No longer active.
*   **Deprecated**: No longer relevant (e.g., feature removed).

## 2. Impact Level
Represents the severity or scope of a change or bug.

*   **None**: Documentation only.
*   **Low**: Isolated component, no public API change.
*   **Medium**: Public API change, backward compatible.
*   **High**: Breaking change, requires migration.
*   **Critical**: Security, Data Loss, or System Outage.

## 3. Compliance State
Represents the validity of an Artifact against the Rules.

*   **Compliant**: Fully aligned with all Decisions and Specs.
*   **Violation**: Contradicts a Decision or Spec. (Must be fixed).
*   **Waiver**: Explicitly allowed Violation for a specific duration (Requires Decision).
