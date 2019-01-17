#ZADANIE 1
#Wykorzystaj metode iteracyjna Jacobiego do
#znalezienia rozwiazan ukladow rownan a) – d). Wykonaj
#obliczenia w przy uzyciu arkusza kalkulacyjnego oraz programu
#napisanego w Python.

import numpy as np;

def diag_dom_test(a):
    test = []
    for i in range(len(a)):
        s = sum([np.abs(a[i,j]) for j in range(len(a)) if i!=j])
        if np.abs(a[i,i])>=s:
            test.append(1)
        else:
            test.append(0)
    return test

def Jacobi_iter(a,b,max_iter):
    x = np.zeros_like(b)
    for k in range(max_iter):
        x_k = np.zeros_like(x)
        for i in range(a.shape[0]):
            s = sum([a[i,j]*x[j] for j in range(a.shape[0]) if i != j])
            x_k[i] = (b[i]-s)/a[i,i]
        if np.allclose(x, x_k, rtol=1e-8):
            break
        x=np.copy(x_k)
    print("Rozwiazanie:")
    print(x)
    error = np.dot(a, x) - b
    print("Blad:")
    print(error)
    print("Liczba iteracji:")
    print(k)
    
a1 = np.array([[3.0, 1.0, -1.0], [1.0, 2.0, -1.0], [1.0, 1.0, 5.0]])
b1 = np.array([181.05, 108.35, 142.55])
print(30*'-')
print("Przyklad A\n")
print("Sprawdzenie czy macierz a jest diagonalnie dominujaca. Jesli zwrocony zostal wektor jedynek to jest diagonalnie dominujaca.")
print(diag_dom_test(a1))
print("Jesli macierz a nie jest diagonalnie dominujaca to wyniki sa niepoprawne.\n")
Jacobi_iter(a1, b1, 100)
print(30*'-')

a2 = np.array([[1.0, -1.0, 2.0], [3.0, 2.0, 1.0], [2.0, -3.0, -2.0]])
b2 = np.array([5.0, 10.0, -10.0])
print(30*'-')
print("Przyklad B\n")
print("Sprawdzenie czy macierz a jest diagonalnie dominujaca. Jesli zwrocony zostal wektor jedynek to jest diagonalnie dominujaca.")
print(diag_dom_test(a2))
print("Jesli macierz a nie jest diagonalnie dominujaca to wyniki sa niepoprawne.\n")
Jacobi_iter(a2, b2, 100)
print(30*'-')

a3 = np.array([[5.0, 1.0, 1.0, 1.0], [2.0, -1.0, -1.0, 1.0], [3.0, -1.0, 2.0, -2.0], [5.0, -4.0, 3.0, -2.0]])
b3 = np.array([685.0, 165.0, 256.0, 361.0])
print("Przyklad C\n")
print("Sprawdzenie czy macierz a jest diagonalnie dominujaca. Jesli zwrocony zostal wektor jedynek to jest diagonalnie dominujaca.")
print(diag_dom_test(a3))
print("Jesli macierz a nie jest diagonalnie dominujaca to wyniki sa niepoprawne.\n")
Jacobi_iter(a3, b3, 100)
print(30*'-')

a4 = np.array([[1.0, 3.0, 5.0], [2.0, 5.0, 1.0], [2.0, 3.0, 8.0]])
b4 = np.array([10.0, 8.0, 3.0])
print("Przyklad D\n")
print("Sprawdzenie czy macierz a jest diagonalnie dominujaca. Jesli zwrocony zostal wektor jedynek to jest diagonalnie dominujaca.")
print(diag_dom_test(a4))
print("Jesli macierz a nie jest diagonalnie dominujaca to wyniki sa niepoprawne.\n")
Jacobi_iter(a4, b4, 100)
print(30*'-')

#Metoda iteracyjna Jacobiego moze byc uzyta tylko wtedy gdy:
#- macierz a jest diagonalnie dominujaca
#- lub gdy macierz a jest macierza symetryczna
#- lub gdy macierz a jest dodatnio okreslona
#Tylko pierwsza z macierzy a podanych w przykladach powyzej jest diagonalnie dominujaca.
#Pozostale trzy macierze a nie sa diagonalnie dominujace.
#Wyniki jakie zwraca metoda iteracyjna Jacobiego dla ostatnich trzech przykladow nie sa poprawne.