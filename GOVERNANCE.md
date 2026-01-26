# Governance Model

This project is governed by Decisions, not by code. The repository captures
architectural authority as canonical DECISION documents. Implementation and
execution evolve from those Decisions through Use Cases and Fast-Lanes.

---

## Change Types

### DECISIONS
Used for architectural, behavioral, or systemic changes. Decisions are the
single source of truth for "why" the system behaves as it does. Changes to a
Decision must be made via the Decision process and recorded as a new Decision
file (immutable once accepted).

### USE CASES
Operational or functional derivations of Decisions. Use Cases describe the
expected system behavior in concrete scenarios and are the input for
implementation tasks and tests.

### FAST-LANES
Used for rapid, bounded execution changes (bug fixes, small improvements).
Fast-Lanes allow the team to act quickly while protecting the Decision model
from ad-hoc changes.

#### FAST-LANE-BUG
Implementation defects with no architectural impact. These are corrected via
a Fast-Lane document, a short-lived branch, and a PR referencing the Fast-Lane.

#### FAST-LANE-HOTFIX
Critical failures requiring immediate action (data loss, security, availability).
Hotfixes follow a stricter flow and require a post-mortem after resolution.

---

## Bug Handling Policy (detailed)

The system supports rapid defect correction without invoking architectural
governance by default. Fast-Lanes exist to maintain execution speed while
preserving decision integrity. Follow the "Flow (detailed)" defined in the
README for step-by-step guidance.

### Roles & Responsibilities

- **Reporter**: captures initial evidence and severity; creates the Fast-Lane doc.
- **Owner (implementer)**: creates branch, implements the fix, opens PR referencing Fast-Lane.
- **Reviewer / QA**: validates the fix, ensures tests pass, approves PR.
- **Governance Owner**: if escalation to a Decision is required, prepares the Decision draft and coordinates review.

### Post-Mortem Requirements (for HOTFIX)

- A Post-Mortem must be written and published in `GOVERNANCE/BUGS/POST-MORTEM-TEMPLATE.md`,
  containing timeline, root cause analysis, impact and corrective actions.

### Escalation

If a bug reveals a conceptual flaw, follow these steps:

1. Create Fast-Lane mitigation to stop the immediate harm.
2. Draft a new DECISION documenting the corrected assumption, alternatives
   considered, constraints and impact.
3. Submit Decision for review following the standard DECISION intake process.
4. Only after Decision acceptance does the implementation approach become canonical.

---

## Governance Integrity Rules

- No Use Case may contradict a Decision.
- Fast-Lanes must never redefine system behavior permanently.
- Critical fixes require post-mortem analysis and may trigger Decision updates.
- Architectural changes require formal Decisions and acceptance by governance.

---

## Auditability & Artifacts

- Each Fast-Lane document must reference the PR and include validation artifacts.
- Post-Mortems are archived in `GOVERNANCE/BUGS/` and linked from the Decision repository when relevant.
- All Decisions, Use Cases and Fast-Lanes are permanent records retained in the repo.
