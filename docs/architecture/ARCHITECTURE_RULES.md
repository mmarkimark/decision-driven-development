# Architecture Rules (Method-Level DDD)

This repository models a development methodology using Domain-Driven Design principles.

## Layer Mapping (Method as System)

| DDD Layer | Method Equivalent |
|----------|-------------------|
| Domain | Decisions, Derivation Rules, Governance Constraints |
| Application | Fast-Lanes, Git workflow, PR execution |
| Infrastructure | GitHub, CI, Templates, Automation scripts |

## Mandatory Rules

1. Domain MUST NOT depend on Application.
2. Domain MUST NOT depend on Infrastructure.
3. Application MUST NOT contain Domain logic.
4. Infrastructure MUST NOT contain Decision logic.
5. Decisions are the only source of architectural authority.
6. Fast-Lanes execute change but never redefine the model.
