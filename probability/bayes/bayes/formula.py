from IPython.display import display, Markdown


def P(event: str) -> str:
    return 'P(' + event + ')'


def P_cond(A: str, B: str) -> str:
    return P(A + '|' + B)


def dfrac(top: str, bottom: str) -> str:
    return r'\dfrac{' + top + '}{' + bottom + '}'


def neg(val: str) -> str:
    return r'\neg{' + val + '}'


class Formula:
    def __init__(self,
                 eventA: str,
                 eventB: str) -> None:
        self._eventA = eventA
        self._eventB = eventB

    @property
    def basic(self):
        A, B = self._eventA, self._eventB
        left = P_cond(A, B)
        top = P_cond(B, A) + P(A)
        bottom = P(B)
        display(Markdown('$' + left + ' = ' + dfrac(top, bottom) + '$'))

    @property
    def long(self):
        A, B = self._eventA, self._eventB
        left = P_cond(A, B)
        top = P_cond(B, A) + P(A)
        bottom_left = P_cond(B, A) + P(A)
        bottom_right = P_cond(B, neg(A)) + P(neg(A))
        bottom = bottom_left + ' + ' + bottom_right
        display(Markdown('$' + left + ' = ' + dfrac(top, bottom) + '$'))
