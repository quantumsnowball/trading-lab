from typing import Self


class Event:
    def __init__(self,
                 name: str,
                 prob: float | None = None) -> None:
        self._name = name
        self._prob = prob
        self._cond_probs: dict[Event, float] = dict()

    @property
    def name(self) -> str:
        return self._name

    @property
    def prob(self) -> float | None:
        return self._prob

    @prob.setter
    def prob(self, val: float | int) -> None:
        assert 0 <= val <= 1
        self._prob = float(val)

    def cond_prob(self, event: Self) -> float | None:
        return self._cond_probs.get(event, None)

    def given(self, event: Self, cond_prob: float | int) -> Self:
        assert 0 <= cond_prob <= 1
        self._cond_probs[event] = float(cond_prob)
        return self
