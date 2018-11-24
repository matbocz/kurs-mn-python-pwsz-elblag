#ZADANIE 1
#Napisz funkcje implementujaca aproksymacje liniowa sredniokwadratowa.
#Wykonaj test dzialania funkcji, podstawiajac do niej zbior danych wygenerowany metoda jak nizej.
#Funkcja powinna obliczac wspolczynniki a i b regresji liniowej f(x)=a+bx.
#Przedstaw graficznie rozwiazanie zadania.

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

plt.plot(x, y, '^r', xlin, ylin, '-g')
plt.grid()
plt.show()