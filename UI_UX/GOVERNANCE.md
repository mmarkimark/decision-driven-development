# UI/UX Governance

This document establishes the governance workflow for User Interface (UI) and User Experience (UX) changes.

## Philosophy
**Design is a Specification.**
UI/UX designs are not suggestions; they are visual specifications. Like all specs, they must derive from a Decision.

## Workflow

1.  **Decision**: A `DR` defines the need for a UI change (e.g., "DR-005: Adopt Dark Mode").
2.  **Design Phase**:
    *   Designers create artifacts (Figma, Sketch, Wireframes).
    *   **Review**: Stakeholders review the design against the Decision's constraints.
3.  **Specification**:
    *   A `UC` (Use Case) is created in `USE_CASES/` referencing the Design URL (e.g., Figma link).
    *   The Spec must detail interactions, states (hover, error, loading), and accessibility requirements.
4.  **Implementation**:
    *   Frontend code is written to match the Spec.

## Accessibility (a11y)
*   All UI changes must comply with WCAG 2.1 AA standards.
*   This is a standing Non-Functional Requirement (see `NON_FUNCTIONAL/README.md`).

## Hand-off
*   Designers must provide:
    *   Assets (SVG, PNG).
    *   Design Tokens (Colors, Typography).
    *   Responsive behavior definitions.
