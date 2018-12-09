#ZADANIE 3C
#Sprawdz poprawnosc rozwiazan ukladow rownan 
#a) – d) wykonujac obliczenia przy uzyciu funkcji
#numpy.linalg.solve().

import numpy as np

R = np.array([[5, 1, 1, 1], [2, -1, -1, 1], [3, -1, 2, -2], [5, -4, 3, -2]])
V = np.array([685, 165, 256, 361])

X = np.linalg.solve(R, V)
print(X)

#Roznica pomiedzy napisana wlasnorecznie implementacja
#metody Kramera a funkcja numpy.linalg.solve jest niewielka.
#Mozna przyjac ze wyniki zwracane przez napisana wlasnorecznie
#implementacja metody Kramera sa poprawne.