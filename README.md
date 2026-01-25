# Decision-Driven Development

Governance-first, spec-driven framework for AI-assisted software development.

The goal of this project is to fully document and formalize a complete development methodology that prioritizes decision-making and specifications over raw code production, ensuring that AI agents and humans work in a strictly governed environment.

## Documentation Map

### Core Governance
*   [Governance Model](GOVERNANCE.md): The constitution of the project.
*   [Principles](PRINCIPLES.md): The inviolable rules.
*   [Agents & Roles](AGENTS.md): Responsibilities for Humans and AI.

### The Methodology
The development flow moves strictly from top to bottom:

1.  **[Decisions](decisions/README.md)**: The "Why" and "Constraints". Immutable records.
2.  **[Specs & Use Cases](specs/README.md)**: The "What". Functional requirements derived from Decisions.
3.  **Implementation**: The "How". Code, Tests, and Config.

### Process & Workflow
*   [Workflow](WORKFLOW.md): Git flow, Pull Request validation rules.
*   [Fast Lanes](FAST_LANES.md): Explicitly approved shortcuts for low-risk changes.
*   [Non-Functional Requirements](NFR.md): Handling Security, Performance, etc.
*   [AI Practices](AI_PRACTICES.md): Guidelines for safe AI-assisted development.

## Quick Start
1.  Read `GOVERNANCE.md` to understand the philosophy.
2.  Review `decisions/` to understand existing constraints.
3.  To propose a change, start by copying `decisions/TEMPLATE.md` to a new Decision Record.

## License
See [LICENSE](LICENSE).
