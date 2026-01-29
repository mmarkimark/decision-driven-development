# Specifications (Specs) & Use Cases

This directory contains the Specifications (Use Cases) for the project.

## Philosophy
**Spec-Driven Development** means that we define **what** we are building before we build it. Code is a liability; Specs are an asset.

## Relationship to Decisions
*   Specs derive strictly from Decisions.
*   You cannot have a Spec without a parent Decision (unless it's a minor maintenance task, which still falls under general governance).

## Process
1.  **Draft**: Copy `TEMPLATE.md` to `UC-XXXX-short-title.md`.
2.  **Link**: Ensure the "Derived From" field links to an Accepted Decision.
3.  **Refine**: Define the flow, edge cases, and NFRs.
4.  **Review**: PR review focuses on completeness and alignment with the Decision.
5.  **Approve**: Once approved, implementation can begin.

## Relationship to Code
*   Implementation PRs must link to the Spec they implement.
*   Tests should verify the "Verification Plan" defined in the Spec.
