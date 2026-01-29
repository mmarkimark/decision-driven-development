from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class DecisionDate:
    value: date
