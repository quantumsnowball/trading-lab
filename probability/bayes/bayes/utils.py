from fractions import Fraction


class Value:
    def __init__(self, value: float) -> None:
        self._value = float(value)
        self._fraction = Fraction(self._value)

    def __repr__(self) -> str:
        return str(self._fraction.limit_denominator())

    @property
    def value(self) -> float:
        return self._value
