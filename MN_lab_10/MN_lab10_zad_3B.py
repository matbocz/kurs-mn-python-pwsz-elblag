#ZADANIE 3B
#Sprawdz poprawnosc rozwiazan ukladow rownan 
#a) – d) wykonujac obliczenia przy uzyciu funkcji
#numpy.linalg.solve().

import numpy as np

R = np.array([[1, -1, 2], [3, 2, 1], [2, -3, -2]])
V = np.array([5, 10, -10])

X = np.linalg.solve(R, V)
print(X)

#Roznica pomiedzy napisana wlasnorecznie implementacja
#metody Kramera a funkcja numpy.linalg.solve jest niewielka.
#Mozna przyjac ze wyniki zwracane przez napisana wlasnorecznie
#implementacja metody Kramera sa poprawne.