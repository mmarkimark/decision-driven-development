from dataclasses import dataclass

@dataclass(frozen=True)
class Drawdown:
    # Represented as a percentage (e.g., -15.0 for -15%)
    value: float

    def __post_init__(self):
        # Drawdown is typically 0 or negative.
        if self.value > 0:
            raise ValueError("Drawdown cannot be positive")
