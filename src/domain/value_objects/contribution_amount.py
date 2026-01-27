from dataclasses import dataclass

@dataclass(frozen=True)
class ContributionAmount:
    value: float

    def __post_init__(self):
        if self.value < 0:
            raise ValueError("Contribution amount cannot be negative")

    def __mul__(self, other: float) -> 'ContributionAmount':
        if not isinstance(other, (int, float)):
             raise TypeError("Multiplication only supported with scalar values")
        return ContributionAmount(round(self.value * other, 2))

    def __add__(self, other: 'ContributionAmount') -> 'ContributionAmount':
        if not isinstance(other, ContributionAmount):
             raise TypeError("Addition only supported with ContributionAmount")
        return ContributionAmount(round(self.value + other.value, 2))
