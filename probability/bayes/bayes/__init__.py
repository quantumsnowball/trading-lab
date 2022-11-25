from .event import Event
from .formula import Formula


def Pcond(p_A: float, p_B: float, p_B_given_A: float):
    p_A_given_B = p_B_given_A * p_A / p_B
    return p_A_given_B


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

    @property
    def prob(self) -> float:
        p_A = self._a.prob
        p_B = self._b.prob
        p_B_given_A = self._b.cond_prob(self._a)
        assert isinstance(p_A, float)
        assert isinstance(p_B, float)
        assert isinstance(p_B_given_A, float)
        p_A_given_B = Pcond(p_A, p_B, p_B_given_A)
        return p_A_given_B
