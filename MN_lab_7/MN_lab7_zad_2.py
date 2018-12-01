#ZADANIE 2
#Wykorzystujac funkcje 'curve_fit()' wykonaj szukanie modelu
#matematycznego poprzez dobor parametrow funkcji 
#f(x)=exp (- a * x) - b tak, aby dopasowala sie do zbioru danych.
#Najpierw wygeneruj zaszumione dane pomiarowe, na bazie
#wymienionej funkcji, celem stworzenia zbioru danych dla
#aproksymacji. Nastepnie wykonaj procedure doboru parametrow a
#i b wymienionej funkcji celem aproksymacji. Przy realizacji
#zadania pomocny moze byc kod omowiony w przykladzie
#prezentowanym w wykladzie nr 7. Przedstaw wnioski w
#sprawozdaniu.

import numpy as np
import pylab
from scipy.optimize import curve_fit

def f(x, a, b, c):
    return np.exp(-a * x) - b

x = np.linspace(0, 4, 50)
y = f(x, a = 2.5, b = 1.3, c = 0.5)
yi = y + 0.2 * np.random.normal(size = len(x))

popt, pcov = curve_fit(f, x, yi)

a, b, c = popt
print("Parametry optymalne a = %g, b = %g, c = %g" % (a, b, c))

yfitted = f(x, * popt)

pylab.plot(x, yi, 'o', label = 'data $y_i$')
pylab.plot(x, yfitted, '-', label = 'fit $f(x_i)$')
pylab.xlabel('x')
pylab.legend()
pylab.schow()

#W biblitece scipy istnieje funkcja curve_fit.
#Jest to aproksymacja odpowiednio dobrana krzywa.
#Funkcja ta korzysta z technik optymalizacji.
#Pozwala ona na optymalne znalezienie parametrow modelu matematycznego.