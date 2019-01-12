#ZADANIE 1
#Napisz program realizujacy poszukiwanie miejsc zerowych
#powyzszych funkcji z punktu a) i b). Wykorzystaj metode graficzna,
#liniowej inkrementacji i bisekcji. Stworz odpowiednie funkcje
#implementujace wymienione metody poszukiwania miejsc zerowych.
#Dobierz odpowiednio obszary wyszukiwania. Wykonaj analize bledow.
#Opisz w sprawozdaniu wnioski.

import numpy as np
import matplotlib.pyplot as plt

def fxA(x):
    return 7 * x**5 + 9 * x**2 - 5 * x

def fxB(x):
    return (1 / ((x - 0.3)**2 + 0.01)) - (1 / ((x - 0.8)**2) + 0.04)

def linearIncremental(fx, xstart, xd, maxincr):
    x = xstart
    fstart = fx(x)
    for i in range(maxincr):
        x = xstart + i * xd
        if fstart * fx(x) < 0:
            break
    if fstart * fx(x) > 0:
        raise Exception("Nie znaleziono rozwiazania!")
    else:
        return x - (xd * fx(x)) / (fx(x)-fx(x - xd))

def bisection(fx, a, b, err):
    while np.absolute(b - a) > err:
        midPoint = (a + b) * 0.5
        if fx(midPoint) * fx(a) < 0:
            b = midPoint
        midPoint = (a + b) * 0.5
        if fx(midPoint) * fx(b) < 0:
            a = midPoint
    return b - (b - a) * fx(b) / (fx(b) - fx(a))

print("Funkcja A")
print("\nTest metody graficznej")
x = np.arange(-3, 3, 0.1)
plt.plot(x, fxA(x), 'r.')
plt.grid(True)
plt.show()

print("\nTest metody inkrementacji")
err = fxA(linearIncremental(fxA, -3, 0.01, 500))
print("x1 = ",linearIncremental(fxA, -3, 0.01, 500), "fx(x1) = ", err)
err = fxA(linearIncremental(fxA, 0, 0.01, 500))
print("x2 = ",linearIncremental(fxA, 0, 0.01, 500), "fx(x2) = ", err)
err = fxA(linearIncremental(fxA, 0.5, 0.01, 500))
print("x3 = ",linearIncremental(fxA, 0.5, 0.01, 500), "fx(x3) = ", err)

print("\nTest metody bisekcji")
print("x1 = ", bisection(fxA, -5, 1, 0.001))
print("x2 = ", bisection(fxA, -4, 1, 0.001))
print("x3 = ", bisection(fxA, -3, 1, 0.001))


print("\n\nFunkcja B")
print("\nTest metody graficznej")
x = np.arange(-3, 3, 0.1)
plt.plot(x, fxB(x), 'y.')
plt.grid(True)
plt.show()

print("\nTest metody inkrementacji")
err = fxB(linearIncremental(fxB, -3, 0.01, 500))
print("x1 = ",linearIncremental(fxB, -3, 0.01, 500), "fx(x1) = ", err)
err = fxB(linearIncremental(fxB, 0, 0.01, 500))
print("x2 = ",linearIncremental(fxB, 0, 0.01, 500), "fx(x2) = ", err)
err = fxB(linearIncremental(fxB, 0.5, 0.01, 500))
print("x3 = ",linearIncremental(fxB, 0.5, 0.01, 500), "fx(x3) = ", err)

print("\nTest metody bisekcji")
print("x1 = ", bisection(fxB, -5, 1, 0.001))
print("x2 = ", bisection(fxB, -4, 1, 0.001))
print("x3 = ", bisection(fxB, -3, 1, 0.001))

#Program umozliwia znalezienie miejsc zerowych funkcji na trzy sposoby:
#- metody graficznej,
#- metody liniowej inkrementacji,
#- metody bisekcji.
#Przedstawione w programie metody znalezienia miejsc zerowych nie sa idealne.
#Metoda liniowej inkrementacji zwraca wysoki blad.
#Metoda bisekcji nie zwraca dokladnych wartosci miejsc zerowych.