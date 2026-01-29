# Decision-Driven Development

Governance-first, spec-driven framework for AI-assisted software development.

The goal of this project is to fully document and formalize a complete development methodology that prioritizes decision-making and specifications over raw code production, ensuring that AI agents and humans work in a strictly governed environment.

## Documentation Map

### Core Governance
*   [Agents & Roles](AGENTS.md): Responsibilities for Humans and AI.
*   [Git & Workflow Governance](GIT/GOVERNANCE.md): Git flow, Pull Request validation, and Fast Lanes.
*   [UI/UX Governance](UI_UX/GOVERNANCE.md): Design-to-Spec workflow.
*   [Roadmap](ROADMAP.md): Strategic direction.
*   Documentation Synchronization Rule (docs/domain/documentation_synchronization.md)

### The Methodology (Derivation Chain)
The development flow moves strictly from top to bottom:

1.  **[Decisions](DECISIONS/README.md)**: The "Why" and "Constraints". Immutable records.
2.  **[Use Cases](USE_CASES/README.md)**: The "What". Functional requirements derived from Decisions.
3.  **Implementation**: The "How". Code, Tests, and Config.

### Standards & Prompts
*   [Non-Functional Requirements](NON_FUNCTIONAL/README.md): Security, Performance, Reliability standards.
*   [AI Prompts](PROMPTS/JULES.md): System prompts and guidelines for AI agents.

## Quick Start
1.  Read `DECISIONS/DECISION-001.md` to understand the origin of this framework.
2.  Review `DECISIONS/` to see active constraints.
3.  To propose a change, copy `DECISIONS/TEMPLATE.md` to a new Decision Record.

## License
See [LICENSE](LICENSE).

## Governance Evolution Layer

This methodology now includes an explicit governance evolution model.

The system is no longer only specification-driven — it is also self-governed through:

- Rule hierarchy
- Change classification
- Decision lifecycle
- Conflict resolution
- Traceability enforcement
- AI operational boundaries

This transforms the methodology into a structured meta-architecture.

See:

- `docs/architecture/RULE_HIERARCHY.md`
- `docs/domain/change_types.md`
- `docs/domain/decision_lifecycle.md`
- `docs/domain/conflict_resolution.md`
- `docs/domain/traceability_rule.md`

---

## Changelog Policy

This repository maintains a changelog because the methodology itself evolves.

All structural or governance changes must be recorded in `CHANGELOG.md`.
