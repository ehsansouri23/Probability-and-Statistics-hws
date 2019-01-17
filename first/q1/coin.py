import random
import matplotlib.pyplot as plt

tail = 0
head = 0
y = {}
x = {}
n = 1000

for untilNow in range(1, n + 1):
    if random.randint(0, 100) < 70:
        head = head + 1
    else:
        tail = tail + 1
    x[untilNow] = untilNow
    y[untilNow] = head / untilNow

print("Head = %s   ,   Tail = %s   Head / Tail = %s   n = %s" % (head, tail, y[n], n))

plt.title("Y = (Head / Flip) , X = Flip")
plt.plot(x.values(), y.values(), color='red', scalex=1)
plt.show()
