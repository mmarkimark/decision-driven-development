from dataclasses import dataclass

@dataclass(frozen=True)
class SMAValue:
    value: float

    def __post_init__(self):
        if self.value < 0:
            raise ValueError("SMA value cannot be negative")
