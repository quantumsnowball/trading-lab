from IPython.display import display, Markdown


def dfrac(top: str, bottom: str) -> str:
    return r'\dfrac{' + top + '}{' + bottom + '}'


def neg(val: str) -> str:
    return r'\neg{' + val + '}'


class Bayes:
    def __init__(self,
                 *,
                 eventA: str,
                 eventB: str) -> None:
        self._eventA = eventA
        self._eventB = eventB

    @property
    def formula(self):
        str_left = f'P({self._eventA}|{self._eventB})'
        str_top = f"P({self._eventB}|{self._eventA}) P({self._eventA})"
        str_bottom = f'P({self._eventB})'
        display(Markdown(
            '$' + str_left + ' = ' + dfrac(str_top, str_bottom) + '$'
        ))

    @property
    def formula_long(self):
        str_left = f'P({self._eventA}|{self._eventB})'
        str_top = f"P({self._eventB}|{self._eventA}) P({self._eventA})"
        str_bottom_left = f"P({self._eventB}|{self._eventA}) P({self._eventA})"
        str_bottom_right = "P(" + self._eventB + r"|\neg{" + '}' + \
            self._eventA + r")P(\neg{" + self._eventA + r"})"
        str_bottom = str_bottom_left + " + " + str_bottom_right
        display(Markdown(
            '$' + str_left + ' = ' + dfrac(str_top, str_bottom) + '$'
        ))
