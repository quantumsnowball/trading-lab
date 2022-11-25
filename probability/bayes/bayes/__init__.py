from .event import Event
from .formula import Formula


class Bayes:
    def __init__(self,
                 eventA: Event,
                 eventB: Event) -> None:
        self._a = eventA
        self._b = eventB
        self._formula = Formula(self._a.name,
                                self._b.name)

    @property
    def formula(self):
        return self._formula
