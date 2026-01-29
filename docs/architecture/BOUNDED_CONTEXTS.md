# Bounded Contexts

This document identifies the Bounded Contexts within the Decision-Driven Development methodology. Each context represents a specific linguistic and operational boundary where terms have specific meanings.

## 1. The Governance Context

*   **Focus**: Authority, Policy, and Constraints.
*   **Key Artifacts**: `DECISIONS/`, `GOVERNANCE.md`.
*   **Ubiquitous Language**:
    *   **Decision**: An immutable record of a choice and its context.
    *   **Constraint**: A limitation imposed by a Decision.
    *   **Ratification**: The formal acceptance of a Decision by a Human.
    *   **Supersede**: Replacing an old Decision with a new one.
*   **Role**: To define the "Rules of the Game".

## 2. The Specification Context

*   **Focus**: Requirements translation and Functional Definition.
*   **Key Artifacts**: `USE_CASES/`, `UI_UX/`.
*   **Ubiquitous Language**:
    *   **Spec / Use Case**: A functional description derived from Decisions.
    *   **Scenario**: A concrete example of system behavior.
    *   **Actor**: The entity initiating a Use Case.
    *   **Pre-condition**: State required before execution.
*   **Role**: To translate "Rules" into "Requirements".

## 3. The Delivery Context (Execution)

*   **Focus**: Implementation, Verification, and Deployment.
*   **Key Artifacts**: `GIT/`, Source Code, Tests, CI/CD.
*   **Ubiquitous Language**:
    *   **Pull Request (PR)**: The unit of work delivery.
    *   **Fast-Lane**: An expedited delivery path for specific scenarios.
    *   **Build**: The process of assembling the system.
    *   **Failure**: A breakdown in verification.
*   **Role**: To realize "Requirements" into "Working Software".

## Context Mappings

### Governance -> Specification (Upstream -> Downstream)
*   **Relationship**: Customer/Supplier.
*   **Description**: Governance supplies the Rules. Specification consumes them to create Specs. Specification cannot change Rules.

### Specification -> Delivery (Upstream -> Downstream)
*   **Relationship**: Customer/Supplier.
*   **Description**: Specification supplies the Requirements. Delivery consumes them to build the software. Delivery cannot invent Requirements.

### Delivery -> Governance (Feedback Loop)
*   **Relationship**: Conformist / Feedback.
*   **Description**: Delivery encounters reality. If Reality contradicts Governance, Delivery raises a "Constraint Conflict", triggering a new Governance cycle (New Decision).
