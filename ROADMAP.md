# Roadmap

This document outlines the strategic direction and upcoming milestones for the Decision-Driven Development framework.

## Phase 1: Foundation (Current)
*   [x] Establish Core Governance (`GOVERNANCE.md`).
*   [x] Define Decision Record process (`DECISIONS/`).
*   [x] Define Use Case process (`USE_CASES/`).
*   [x] Establish Git Workflow and Fast Lanes (`GIT/GOVERNANCE.md`).
*   [x] Define Agent Roles (`AGENTS.md`).

## Phase 2: Tooling & Automation
*   [ ] **CLI Tool**: Develop a CLI to scaffold Decisions and Use Cases (e.g., `ddd new decision`).
*   [ ] **Linter**: Create a linter to verify that every Spec links to a Decision and every PR links to a Spec.
*   [ ] **AI Agents**: Implement the "Scribe" and "Validator" agents defined in `AGENTS.md`.

## Phase 3: Expansion
*   [ ] **IDE Integration**: VS Code extension to visualize the Decision -> Spec -> Code graph.
*   [ ] **Dashboard**: Web view of the project's decision history and compliance status.

## Phase 4: Ecosystem
*   [ ] **Plugin System**: Allow custom governance rules.
*   [ ] **Templates**: specialized templates for different domains (Mobile, Backend, AI).
