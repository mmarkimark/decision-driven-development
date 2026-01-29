# DECISION-003 — File Naming Convention for Governance vs Documentation

## Status
Accepted

## Date
2026-01-29

## Context
The Decision-Driven Development (DDD) framework is a governance system, not just documentation.

Over time, file naming drift (mixed casing, inconsistent styles) creates:

- Ambiguity about what is authoritative
- Confusion for AI agents
- Duplicate files across OS (Linux vs Windows case handling)
- Loss of hierarchy between rules and explanations

The system requires a visual and structural distinction between:

- Artifacts that govern the system
- Documents that describe or explain the system

---

## Decision
The repository adopts a semantic naming convention based on authority level.

### UPPERCASE = Governing Artifacts (System Authority)

These files and folders define rules, constraints, and process behavior.

They are considered part of the operational model of the framework.

Examples:

DECISIONS/
USE_CASES/
AGENTS.md
README.md
ROADMAP.md
CHANGELOG.md
GOVERNANCE.md
AI_CONSTRAINTS.md

Meaning:
This artifact changes how the system operates.

---

### lowercase = Explanatory / Structural Documentation

These documents describe the model but do not govern behavior directly.

They represent the conceptual domain, not the execution contract.

Examples:

docs/domain/value_objects.md
docs/domain/events.md
docs/domain/change_types.md
docs/architecture/bounded_contexts.md
docs/architecture/rule_hierarchy.md

Meaning:
This artifact explains the system but does not command it.

---

### Rules
1. All governing artifacts MUST use uppercase names.
2. All explanatory documentation MUST use lowercase names.
3. Mixed-case filenames are prohibited.
4. AI agents must follow this convention when generating files.

---

## Rationale
This rule provides:

### 3.1 Visual Hierarchy
Developers and AI can immediately identify authority level.

### 3.2 AI Stability
Reduces accidental duplication such as:

Governance.md vs GOVERNANCE.md
Readme.md vs README.md

### 3.3 OS Compatibility
Prevents case-sensitivity conflicts across platforms.

### 3.4 Architectural Clarity

DDD Concept → Mapping
Domain Model → lowercase docs/
Contracts / Rules → UPPERCASE
Ubiquitous Language → GLOSSARY.md

---

## Impact
Positive:
- Stronger governance clarity
- Reduced AI drift
- Cleaner repo structure
- Better onboarding

Negative:
- Existing files may require renaming
- Short-term PR churn

---

## References
<!-- ACTION: to be defined by human decision owner -->
