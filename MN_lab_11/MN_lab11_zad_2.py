#ZADANIE 2
#Wykorzystaj metode eliminacji Gaussa do znalezienia
#rozwiazan ukladow rownan a) – d). Wykonaj obliczenia przy
#uzyciu udostepnionej funkcji i programu napisanego w Python.
#Przeanalizuj i opisz w sprawozdaniu dzialanie funkcji realizującej
#metodę eliminacji Gaussa.

import numpy as np

def gaussElimin(a,b):
    n = len(b)
    #procedura eliminacji
    for k in range(0, n-1):
        for i in range(k+1, n):
            if a[i, k] != 0.0:
                lam = a[i, k] / float(a[k, k])
                a[i, k+1:n] = a[i, k+1:n] - lam * a[k, k+1:n]
                b[i] = b[i] - lam * b[k]
    #procedura wyliczania rozwiazania i zapisu do macierzy b
    for k in range(n-1, -1, -1):
        b[k] = (b[k] - np.dot(a[k, k+1:n], b[k+1:n])) / float(a[k, k])
    return b
    
def testA():
    #macierze jako float
    a = np.array([[3.0, 1.0, -1.0], [1.0, 2.0, -1.0], [1.0, 1.0, 5.0]])
    b = np.array([181.05, 108.35, 142.55])
    print('Rozwiazanie(np.linalg.solve):')
    print(np.linalg.solve(a, b))
    Iout = gaussElimin(a,b)
    print('Rozwiazanie(gaussElimin):')
    print(Iout)
    
def testB():
    #macierze jako float
    a = np.array([[1.0, -1.0, 2.0], [3.0, 2.0, 1.0], [2.0, -3.0, -2.0]])
    b = np.array([5.0, 10.0, -10.0])
    print('Rozwiazanie(np.linalg.solve):')
    print(np.linalg.solve(a, b))
    Iout = gaussElimin(a,b)
    print('Rozwiazanie(gaussElimin):')
    print(Iout)
    
def testC():
    #macierze jako float
    a = np.array([[5.0, 1.0, 1.0, 1.0], [2.0, -1.0, -1.0, 1.0], [3.0, -1.0, 2.0, -2.0], [5.0, -4.0, 3.0, -2.0]])
    b = np.array([685.0, 165.0, 256.0, 361.0])
    print('Rozwiazanie(np.linalg.solve):')
    print(np.linalg.solve(a, b))
    Iout = gaussElimin(a,b)
    print('Rozwiazanie(gaussElimin):')
    print(Iout) 
    
def testD():
    #macierze jako float
    a = np.array([[1.0, 3.0, 5.0], [2.0, 5.0, 1.0], [2.0, 3.0, 8.0]])
    b = np.array([10.0, 8.0, 3.0])
    print('Rozwiazanie(np.linalg.solve):')
    print(np.linalg.solve(a, b))
    Iout = gaussElimin(a,b)
    print('Rozwiazanie(gaussElimin):')
    print(Iout)

if __name__ == "__main__":
    print(30 * '-')
    print("Funkcja A")
    testA()
    print(30 * '-')
    
    print(30 * '-')
    print("Funkcja B")
    testB()
    print(30 * '-')
    
    print(30 * '-')
    print("Funkcja C")
    testC()
    print(30 * '-')
    
    print(30 * '-')
    print("Funkcja D")
    testD()
    print(30 * '-')
    
#Funkcja napisana samodzielnie w Python zwraca identyczne wyniki
#jak funkcja biblioteczna numpy.linalg.solve().
#Metoda eliminacji Gaussa wykorzystuje dwie fazy obliczen.
#Pierwsza faza jest faza eliminacji, ktora sprowadza problem obliczeniowy do Ux = c.
#Druga faza jest faza wstecznego podstawienia, ktora polega na podstawianiu
#uzyskanych rozwiazan za niewiadome.
#Wystepujaca w programie funkcja sklada sie z dwoch algorytmow.
#Pierwszy algorytm realizuje faze eliminacji.
#Drugi algorytm odpowiada za wyliczenie rozwiazan i ich zapis do macierzy b.