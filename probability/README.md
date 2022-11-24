# Probability

Let's dig dipper into probability. With a rolling window, we are simulating what a trader will see in any moment. The best he can do is to estimate probability of some events, and then use that probability to make trading decision. We can simulate this action in a backtest. 


## Bayes' Theorem:

Normally when the market is efficient, the probability that everyone sees are the same, and there is no edge to place any bet. However, if a trader can see some evidence that is not well know, he should have an edge and hopefully can have an edge on trading. Bayes Theorem is found useful to update a prior probability which is giving no edge, to a posterior probability that maybe profitable to trade on.

### Formula

$P(A|B) = \dfrac{P(B|A)\ P(A)}{P(B)}$

or

$P(A|B) = \dfrac{P(B|A)P(A)}{P(B|A)P(A) + P(B|A')P(A')}$

or

$P(A|B) = \dfrac{P(B|A)P(A)}{\sum_{A'}{P(B|A')}{P(A')}}$

### Example
let

$P(A) =P(up5d),\ i.e.\ P(price\ increased\ in\ 5\ days)$

$P(B) =P(above),\ i.e.\ P(sma50 > sma200)$

then 

$P(up5d|above) = \dfrac{P(above|up5d)P(up5d)}{P(above|up5d)P(up5d)+P(above|\neg up5d)P(\neg up5d)}$