from bayes import Bayes, Event
import pytest


def test_formula():
    a = Event('A')
    b = Event('B')
    bayes = Bayes(a, b)
    print(bayes.formula.basic)
    print(bayes.formula.long)


@pytest.mark.parametrize('A, p_A, B, p_B, p_B_given_A, p_A_given_B', [
    ('6', 1 / 6, 'even', 1 / 2, 1.0, 1 / 3, ),
    ('5', 1 / 13, 'red', 1 / 2, 1 / 2, 1 / 13, ),
    ('even', 5 / 13, 'red', 1 / 2, 10 / 20, 10 / 26),
])
def test_dice(A, p_A, B, p_B, p_B_given_A, p_A_given_B):
    a = Event(A, p_A)
    b = Event(B, p_B).given(a, p_B_given_A)
    ans = Bayes(a, b).prob
    assert round(ans.value, 6) == round(p_A_given_B, 6)
