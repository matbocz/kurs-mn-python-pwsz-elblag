#ZADANIE 2
#Oblicz blad wzgledny i bezwzgledny dla aproksymacji z zadania 1.
#Wyciagnij wnioski.

import matplotlib.pyplot as plt
import numpy as np

def linear_approx(x, y):
    sredniaX = np.mean(x)
    sredniaY = np.mean(y)
    
    licznikB = 0
    mianownikB = 0
    
    n = len(x)
    for i in range(0, n):
        licznikB = licznikB + y[i] * (x[i] - sredniaX)
        mianownikB = mianownikB + x[i] * (x[i] - sredniaX)

    b = licznikB / mianownikB
    a = sredniaY - sredniaX * b
    
    return(a, b)
    
x = np.arange(-20, 20)
y = 0.5 * x**3 + 1.5 * x**2 - 2.5 * x + 69 + np.random.normal(scale=200, size=len(x))

a, b = linear_approx(x, y)

xlin = np.arange(-20, 20)
ylin = a + b * xlin

n = len(x)
for i in range(0, n):
    print("Blad bezwzgledny:")
    bladBW = np.abs(y[i] - (a + b * x[i]))
    print(bladBW)
    
    print("Blad wzgledny:")
    bladWZ = (bladBW / i) * 100
    print(bladWZ)

plt.plot(x, y, '^r', xlin, ylin, '-g')
plt.grid()
plt.show()

#Bledy bezwzgledne i wzgledne czasami maja wartosci mniejsze a czasami wieksze,
#co jest zgodne z graficznym rozwiazaniem zadania.
#Bledy pomiedzy wartoscia mierzona a modelowana sa czyms normalnym.
#Funkcja powinna dopasowywac sie jak najlepiej,
#czyli z jak najmniejszym bledem miedzy wartoscia mierzona a modelowana.