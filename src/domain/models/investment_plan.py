from dataclasses import dataclass
from uuid import UUID

@dataclass(frozen=True)
class InvestmentPlan:
    id: UUID
    asset_symbol: str
    base_contribution_amount: float
    is_active: bool
