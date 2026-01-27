# Programming Rules

This project follows deterministic, governance-driven development.

## General Rules
- Documentation defines behavior
- Code implements documentation
- No implicit behavior is allowed
- Determinism is mandatory

## Architecture
- Domain-Driven Design (DDD)
- Domain layer must have no infrastructure dependencies
- No I/O in domain logic
- No system time usage inside core logic

## Python Rules
- Use type hints
- Prefer pure functions
- Avoid mutable shared state
- Explicit data models

## UI Rules
- Interfaces are read-only
- No business logic in UI
- UI does not make decisions

## AI Agents
- Must not invent rules
- Must stop if documentation is missing
- Must follow DECISION documents strictly
