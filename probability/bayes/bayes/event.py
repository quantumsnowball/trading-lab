class Event:
    def __init__(self,
                 name: str,
                 prob: float | None = None) -> None:
        self._name = name
        self._prob = prob

    @property
    def name(self) -> str:
        return self._name

    @property
    def prob(self) -> float | None:
        return self._prob

    @prob.setter
    def prob(self, val: float) -> None:
        assert isinstance(val, float)
        assert 0 < val < 1
        self._prob = val
