from bayes import Bayes


def test_basic():
    bayes = Bayes(eventA='A', eventB='B')
    bayes.formula
    bayes.formula_long
