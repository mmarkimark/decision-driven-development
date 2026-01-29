# Architecture Rules

This document defines the Meta-Architecture of the Decision-Driven Development methodology using Domain-Driven Design (DDD) principles. The methodology itself is the "System Under Design".

## The Layered Architecture

The repository is organized into three strict concentric layers. The Dependency Rule applies: source code dependencies can only point inwards. Nothing in an inner circle can know anything at all about something in an outer circle.

### 1. The Domain Layer (Core)
*   **Definition**: The heart of the methodology. It defines the "Why" and the "Rules". It is pure policy and completely independent of tools, workflows, or specific implementation technologies.
*   **Components**:
    *   `DECISIONS/` (The Aggregates)
    *   `GOVERNANCE/` (The Domain Services)
    *   `docs/domain/` (The Domain Definitions)
*   **Characteristics**:
    *   **Immutable**: Decisions are recorded facts.
    *   **Tool-Agnostic**: A Decision is valid regardless of whether we use Git, SVN, or stone tablets.
    *   **Forbidden**: No implementation details, no "how-to" guides.

### 2. The Application Layer (Orchestration)
*   **Definition**: Defines the jobs the methodology is supposed to do. It directs the flow of work from Decisions to Realization. It orchestrates the domain entities.
*   **Components**:
    *   `USE_CASES/` (Application Services/Specs)
    *   `Fast-Lanes` (Emergency/Specific Workflows)
    *   `AGENTS.md` (Role Orchestration)
*   **Characteristics**:
    *   **Derivation**: Every Use Case must trace back to a Decision (Domain).
    *   **Orchestration**: Coordination of Agents (Human and AI) to fulfill a Decision.

### 3. The Infrastructure Layer (Mechanisms)
*   **Definition**: The tools, frameworks, and mechanisms used to execute the methodology.
*   **Components**:
    *   `GIT/` (Version Control mechanisms)
    *   `PROMPTS/` (AI Interface mechanisms)
    *   `NON_FUNCTIONAL/` (Quality Gates)
    *   `UI_UX/` (Design Delivery mechanisms)
    *   `CONTRIBUTING.md` (External Interface)
*   **Characteristics**:
    *   **Volatile**: Tools (Git, GitHub, CI) can change without changing the Domain (Decisions).
    *   **Pluggable**: We could swap `PROMPTS/JULES.md` for another agent interface without changing the core Rules.

## The Dependency Rule

1.  **Infrastructure depends on Application**: The Git workflow (`GIT/GOVERNANCE.md`) exists to support the Use Cases and Fast Lanes.
2.  **Application depends on Domain**: Use Cases (`USE_CASES/`) exist solely to realize Decisions (`DECISIONS/`).
3.  **Domain depends on Nothing**: Decisions (`DECISIONS/`) stand alone. They do not reference Git branches or CI pipelines.

## Violation Examples (Do Not Do This)

*   *Domain Leaking to Infra*: A Decision Record mentioning "GitHub Actions". (Decisions should speak of "Automated Verification", not specific tools).
*   *Infra Leaking to Domain*: Using a Git Branch structure that forces a change in how Decisions are numbered.
*   *App Bypassing Domain*: A Fast-Lane that changes a core policy (e.g., "Skip Tests") without a supporting Decision.
