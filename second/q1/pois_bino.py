import numpy as np
import matplotlib.pyplot as plt
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


x1 = 0
x2 = 0
x3 = 0

plt.figure(1)
plt.subplot(211)
plt.title("x1 + x2")
for i in range(0, 150):
    n1 = binomial(i, 100, 0.3)
    n2 = binomial(i, 100, 0.5)
    m = n1 + n2
    plt.scatter(i, m)

plt.subplot(212)
plt.title("x2 + x3")
for i in range(0, 150):
    n1 = binomial(i, 100, 0.5)
    n2 = binomial(i, 200, 0.5)
    m = n1 + n2
    plt.scatter(i, m)

plt.show()
