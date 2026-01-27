from dataclasses import dataclass
from datetime import date
from uuid import UUID

@dataclass(frozen=True)
class MonthlyDecision:
    plan_id: UUID
    decision_date: date
    total_amount: float
    base_amount: float
    reinforcement_amount: float
    reason: str
