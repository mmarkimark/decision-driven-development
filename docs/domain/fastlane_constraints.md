# Fast-Lane Constraints

Fast-Lanes are strictly defined Application Layer maneuvers that allow for expedited execution without a full Decision cycle. They are "Exceptions Managed by Rule".

## 1. The Domain Boundary
*   **Constraint**: A Fast-Lane **MUST NOT** change, contradict, or invalidate an existing Decision.
*   **Constraint**: A Fast-Lane **MUST NOT** introduce new Architectural Policy.

*If a Fast-Lane requires changing a rule, it is no longer a Fast-Lane; it is a Proposal for a new Decision.*

## 2. Valid Fast-Lane Scenarios
Fast-Lanes are permissible for:
1.  **Bug Fixes**: correcting implementation that deviates from the Spec.
2.  **Hotfixes**: critical security or stability interventions.
3.  **Docs**: Typo fixes or clarification in non-normative documentation.
4.  **Chore**: dependency updates (patch versions only).

## 3. The "Fast" in Fast-Lane
"Fast" refers to the *Process* (skipping the Decision review), not the *Quality*.
*   Fast-Lane PRs must still pass all automated checks.
*   Fast-Lane PRs must still be reviewed by a Human.

## 4. Lifecycle
1.  **Trigger**: An incident or minor task is identified.
2.  **Check**: Does this require a policy change?
    *   Yes -> Abort Fast-Lane. Go to Decision.
    *   No -> Proceed.
3.  **Execute**: Implement fix.
4.  **Verify**: Ensure no Decision was violated.
