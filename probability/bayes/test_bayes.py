from bayes import Bayes, Event


def test_formula():
    a = Event('A')
    b = Event('B')
    bayes = Bayes(a, b)
    print(bayes.formula.basic)
    print(bayes.formula.long)
