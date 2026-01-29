# Decisions

This directory contains the Decision Records (DRs) for the project.

## Purpose
Decisions are the primary unit of governance. They define **why** we are doing something and **what** constraints apply. They are the single source of truth for architectural and process choices.

## Process

1.  **Draft**: Copy `TEMPLATE.md` to `DR-XXXX-short-title.md`. Use the next available number.
2.  **Propose**: Open a Pull Request with the new DR. The status should be "Proposed".
3.  **Review**: The team (and/or AI agents) reviews the context, decision, and consequences.
4.  **Accept**: Once agreed, the status is changed to "Accepted" and merged.
5.  **Immutability**: Once merged, the file is **immutable**. Typos can be fixed, but the semantic meaning cannot change.
6.  **Supersede**: If a decision is no longer valid, create a NEW decision that "Supersedes" the old one. Mark the old one as "Superseded By: [New DR]".

## Numbering
Decisions are numbered sequentially (e.g., `DR-0001`, `DR-0002`).

## Validation
*   Every significant change to the system or process requires a Decision.
*   Implementation PRs should reference the Decision they are fulfilling.
