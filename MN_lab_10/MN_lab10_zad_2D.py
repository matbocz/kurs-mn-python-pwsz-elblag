#ZADANIE 2D
#Wykorzystaj metode Kramera do znalezienia rozwiazan
#ukladow rownan a) – d). Wykonaj obliczenia przy uzyciu
#programu napisanego w Python.

import numpy as np

def det(A):
    return sum([(-1)**i * A[i, 0] * det(np.delete(np.delete(A, 0, 1), i, 0)) for i in range(A.shape[0])]) if A.shape != (1, 1) else A[0, 0]

R = np.array([[1, 3, 5], [2, 5, 1], [2, 3, 8]])
V = np.array([10, 8, 3])

R.shape = (3, 3)
V.shape = (1, 3)

print('R = ', R)
print('V = ', V)

print('Generuje macierze pomocnicze R1 - R3')
R1 = np.copy(R)
R2 = np.copy(R)
R3 = np.copy(R)
print('R1 = ', R1)
print('R2 = ', R2)
print('R3 = ', R3)

print('Podstawienie macierzy V do R1 - R3')
R1[:, 0] = V[:]
R2[:, 1] = V[:]
R3[:, 2] = V[:]
print('R1 = ', R1)
print('R2 = ', R2)
print('R3 = ', R3)

print('Rozwiazanie')
I1 = np.linalg.det(R1) / np.linalg.det(R)
I2 = np.linalg.det(R2) / np.linalg.det(R)
I3 = np.linalg.det(R3) / np.linalg.det(R)
print('I1 = ', I1)
print('I2 = ', I2)
print('I3 = ', I3)