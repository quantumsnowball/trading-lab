# Probability

Let's dig dipper into probability. With a rolling window, we are simulating what a trader will see in any moment. The best he can do is to estimate probability of some events, and then use that probability to make trading decision. We can simulate this action in a backtest. 


## Bayes' Theorem:

[Wikipedia](https://en.wikipedia.org/wiki/Bayes%27_theorem)

[Visualize](https://static.laszlokorte.de/stochastic/)

Normally when the market is efficient, the probability that everyone sees are the same, and there is no edge to place any bet. However, if a trader can see some evidence that is not well know, he should have an edge and hopefully can have an edge on trading. Bayes Theorem is found useful to update a prior probability which is giving no edge, to a posterior probability that maybe profitable to trade on.

### Formula

$P(A|B) = \dfrac{P(B|A)\ P(A)}{P(B)}$

or

$P(A|B) = \dfrac{P(B|A)P(A)}{P(B|A)P(A) + P(B|A')P(A')}$

or

$P(A|B) = \dfrac{P(B|A)P(A)}{\sum_{A'}{P(B|A')}{P(A')}}$

### Example
let

$P(A) =P(6),\ i.e.\ P(dice\ 6)$

$P(B) =P(even),\ i.e.\ P(dice\ even)$

then 

$P(6|even) = \dfrac{P(even|6)P(6)}{P(even)} = \dfrac{(1)1/6}{1/2} = \dfrac{1}{3}$

### Example
let

$P(A) =P(up5d),\ i.e.\ P(price\ increased\ in\ 5\ days)$

$P(B) =P(above),\ i.e.\ P(sma50 > sma200)$

then 

$P(up5d|above) = \dfrac{P(above|up5d)P(up5d)}{P(above|up5d)P(up5d)+P(above|\neg up5d)P(\neg up5d)}$

## Kelly Criterion 

[Wikipedia](https://en.wikipedia.org/wiki/Kelly_criterion)

In probability theory, the Kelly criterion (or Kelly strategy or Kelly bet), is a formula that determines the optimal theoretical size for a bet.

### Formula (Gambling)

$f* = p - \dfrac{q}{b} = p - \dfrac{(1-p)}{b}$ 

where 

* $f^{*}$ is the fraction of the current bankroll to wager.
* $p$ is the probability of a win.
* $q$ is the probability of a loss.
* $b$ is the proportion of the bet gained with a win. E.g. If betting $10 on a 2-to-1 odds bet, (upon win you are returned $30, winning you $20), then b=2.

### Formula (Investment)

$f* = \dfrac{p}{a} - \dfrac{q}{b}$

where

* $f^{*}$ is the fraction of the assets to apply to the security.
* $p$ is the probability that the investment increases in value.
* $q$ is the probability that the investment decreases in value.
* $a$ is the fraction that is lost in a negative outcome. If the security price falls 10%, then $a=0.1$.
* $b$ is the fraction that is gained in a positive outcome. If the security price rises 10%, then $b=0.1$.