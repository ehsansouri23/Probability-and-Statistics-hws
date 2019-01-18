import math as mp


def poisson(x, ld):
    a = (ld ** x) * mp.exp(-1 * ld) / mp.factorial(x)
    return a


def binomial(x, n, p):
    if n - x >= 0:
        a = (mp.factorial(n) / (mp.factorial(x) * mp.factorial(n - x))) * (p ** x) * ((1 - p) ** (n - x))
    else:
        a = 0
    return a
