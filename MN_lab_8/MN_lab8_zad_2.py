#ZADANIE 2
#Znajdz wybrana metoda najmniejszą wartosc miejsca zerowego
#funkcji podanej w punkcie c).

import numpy as np
import matplotlib.pyplot as plt

def fx(x):
    return x**4 - 6.4 * x**3 + 6.45 * x**2 + 20.538 * x - 31.752

def bisection(fx, a, b, err):
    while np.absolute(b - a) > err:
        midPoint = (a + b) * 0.5
        if fx(midPoint) * fx(a) < 0:
            b = midPoint
        midPoint = (a + b) * 0.5
        if fx(midPoint) * fx(b) < 0:
            a = midPoint
    return b - (b - a) * fx(b) / (fx(b) - fx(a))

print("Najmniejsza wartosc miejsca zerowego funkcji")

x = np.arange(-2, 2, 0.1)
plt.plot(x, fx(x), 'r.')
plt.grid(True)
plt.show()

print("x = ", bisection(fx, -2, 2, 0.001))