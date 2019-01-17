import matplotlib.pyplot as plt
import math as mp


def poisson(x, ld):
    a = (ld ** x) * mp.exp(-1 * ld) / mp.factorial(x)
    return a


def binomial(x, n, p):
    a = (mp.factorial(n) / (mp.factorial(x) * mp.factorial(n - x))) * (p ** x) * ((1 - p) ** (n - x))
    return a


n = 500
lam = 6
p = lam / n
plt.figure(1)
plt.subplot(211)
for i in range(20):
    s = binomial(i, n, p)
    plt.scatter(i, s)

plt.subplot(212)
for i in range(20):
    pos = poisson(i, lam)
    plt.scatter(i, pos)

print("n = %s  ,  lam = %s  ,  p = %s" % (n, lam, p))
plt.title("n = %s" % n)
plt.show()
