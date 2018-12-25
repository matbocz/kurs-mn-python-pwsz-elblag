#ZADANIE 1
#Napisz program realizujacy poszukiwanie miejsc zerowych
#funkcji a) – b). Wykorzystaj metode siecznych oraz metodę Newtona-
#Raphsona. Stworz odpowiednie funkcje implementujace wymienione
#metody poszukiwania miejsc zerowych. Dobierz odpowiednio obszary
#wyszukiwania. Wykonaj analize bledow. Opisz w sprawozdaniu wnioski.

import numpy as np
import matplotlib.pyplot as plt

def fxA(x):
    return 7 * x**5 + 9 * x**2 + 3 * x

def fxB(x):
    return (1 / ((x - 0.3)**2 + 0.01)) - (1 / ((x - 0.8)**2 + 0.04))

def secant(fx, a, b, err):
    fb = fx(b)
    while np.absolute(fb) > err:
        midPoint = b - (b - a) * fb / (fb-fx(a))
        a = b
        b = midPoint
        fb = fx(b)
    return b

def newton_raphson(fx, x0, err):
    x = x0
    h = 0.1e-5
    while np.absolute(fx(x)) > err:
        d1fx = (fx(x + h / 2.0) - fx(x - h / 2.0)) / h
        x = x - fx(x) / d1fx
    return x

print("Test metody siecznych - funkcja A")
print("x1 = ", secant(fxA, -3., -1., 0.0001))
print("x2 = ", secant(fxA, 0., 1., 0.0001))
print("x3 = ", secant(fxA, 1., 2., 0.0001))

print("\nTest metody newton_raphson - funkcja A")
print("x1 = ", newton_raphson(fxA, -2., 0.0001))
print("x2 = ", newton_raphson(fxA, 0., 0.0001))
print("x3 = ", newton_raphson(fxA, 1.5, 0.0001))

x = np.arange(-3, 3, 0.1)
plt.plot(x, fxA(x), 'r.')
plt.grid(True)
plt.show()

print("\nTest metody siecznych - funkcja B")
print("x1 = ", secant(fxB, -3., -1., 0.0001))
print("x2 = ", secant(fxB, 0., 1., 0.0001))
print("x3 = ", secant(fxB, 1., 2., 0.0001))

print("\nTest metody newton_raphson - funkcja B")
print("x1 = ", newton_raphson(fxB, -2., 0.0001))
print("x2 = ", newton_raphson(fxB, 0., 0.0001))
print("x3 = ", newton_raphson(fxB, 1.5, 0.0001))

x = np.arange(-3, 3, 0.1)
plt.plot(x, fxB(x), 'r.')
plt.grid(True)
plt.show()

#Program umozliwia znalezienie miejsc zerowych funkcji na trzy sposoby:
#- metody graficznej,
#- metody siecznych,
#- metody Newthona-Raphsona.
#Przedstawione w programie metody znalezienia miejsc zerowych nie sa idealne.
#Metody siecznych i Newthona-Raphsona nie zwracają dokladnych wartosci miejsc zerowych.