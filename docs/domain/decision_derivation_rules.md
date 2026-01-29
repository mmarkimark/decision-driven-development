# Decision Derivation Rules

These rules govern the Domain Layer of the methodology, specifically how Decisions dictate reality.

## 1. The Golden Rule of Derivation
**"No Implementation without Specification; No Specification without Decision."**

Every line of code, every configuration change, and every process step must be traceable back to a `DECISION` record.

## 2. Traceability Requirements
The derivation chain must be explicit:
1.  **Decision ID**: `DR-XXX` (Why we are doing this)
2.  **Use Case ID**: `UC-XXX` (What we are doing)
3.  **PR / Commit**: Implementation (How we did it)

*   A PR must reference a Use Case.
*   A Use Case must reference a Decision.

## 3. Immutability of Decisions
*   **State**: Once a Decision file (`DR-XXX.md`) status is set to `Accepted`, the content of that file is **Immutable**.
*   **Correction**: You cannot edit an Accepted Decision to change the rules. You must create a new Decision.
*   **Clarification**: Typographical errors or non-semantic clarifications *may* be allowed via a dedicated "Janitorial" process, but the semantic intent must remain untouched.

## 4. The Supersession Process
To change a rule, you must Supersede it.
1.  Create a new Decision Record (`DR-New`).
2.  In `DR-New`, explicitly state: "Supersedes `DR-Old`".
3.  Once `DR-New` is accepted:
    *   Mark `DR-Old` status as `Superseded`.
    *   Link `DR-Old` to `DR-New`.

## 5. Decision Scope
Decisions are for **Policy**, not **Procedure**.
*   *Valid Decision*: "We will use Python for all backend services."
*   *Invalid Decision*: "Run `pip install flask`." (This belongs in Implementation/Docs).
