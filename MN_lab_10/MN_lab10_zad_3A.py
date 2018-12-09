#ZADANIE 3A
#Sprawdz poprawnosc rozwiazan ukladow rownan 
#a) – d) wykonujac obliczenia przy uzyciu funkcji
#numpy.linalg.solve().

import numpy as np

R = np.array([[3, 1, -1], [1, 2, -1], [1, 1, 5]])
V = np.array([181.05, 108.35, 142.55])

X = np.linalg.solve(R, V)
print(X)

#Roznica pomiedzy napisana wlasnorecznie implementacja
#metody Kramera a funkcja numpy.linalg.solve jest niewielka.
#Mozna przyjac ze wyniki zwracane przez napisana wlasnorecznie
#implementacja metody Kramera sa poprawne.