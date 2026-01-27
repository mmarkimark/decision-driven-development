# DECISION-002 — Monthly Contribution Algorithm

Defines the deterministic contribution logic.

## Rules

- Base contribution P is always executed.
- Reinforcement applies only when:
  - price < SMA200
  - drawdown ≤ −15%
- Scaling:
  - drawdown > −15% → 1.0 × P
  - −15% to −25% → 1.5 × P
  - ≤ −25% → 2.0 × P
- Reinforcement is part of the same contribution.
- Missing market data disables reinforcement.
- No market prediction or timing.
