#ZADANIE 2A
#Napisz program realizujacy poszukiwanie miejsc zerowych
#funkcji a) – b). Wykorzystaj metode siecznych oraz metode Newtona-
#Raphsona. Stworz odpowiednie funkcje implementujace wymienione
#metody poszukiwania miejsc zerowych. Dobierz odpowiednio obszary
#wyszukiwania. Wykonaj analize bledow. Opisz w sprawozdaniu wnioski.

import scipy.optimize as opt
import timeit

f = lambda x: 7 * x**5 + 9 * x**2 + 3 * x

def bis(f):
    return opt.bisect(f, 0, 1)

def newt(f):
    return opt.newton(f, -0.2)

def ridd(f):
    return opt.ridder(f, 0, 1)

def bren(f):
    return opt.brenth(f, 0, 1)

def test():
    L = []
    for i in range(100):
        L.append(i)

if __name__ == '__main__':
    print("Test metody bisekcji - funkcja biblioteczna")
    print("x0 = ", opt.bisect(f, 0, 1))
    print("Czas obliczeń: ")
    print(timeit.timeit("bis(f)", number = 100, setup = "from __main__ import f, bis"))
    
    print("\nTest metody NR - funkcja biblioteczna")
    print("x0 = ", opt.newton(f, -0.2))
    print("Czas obliczeń: ")
    print(timeit.timeit("newt(f)", number = 100, setup = "from __main__ import f, newt"))
    
    print("\nTest metody Ridder - funkcja biblioteczna")
    print("x0 = ", opt.ridder(f, 0, 1))
    print("Czas obliczeń: ")
    print(timeit.timeit("ridd(f)", number = 100, setup = "from __main__ import f, ridd"))
    
    print("\nTest metody Brenth - funkcja biblioteczna")
    print("x0 = ", opt.brenth(f, 0, 1))
    print("Czas obliczeń: ")
    print(timeit.timeit("bren(f)", number = 100, setup = "from __main__ import f, bren"))
    
#Wszystkie funkcje biblioteczne zwracaja wartosc identyczne wyniki, czyli 0.
#Wyjatkiem jest funkcja NR, ktora zwraca troche inny wynik.
#Test szybkosci dla 100 wywolan wykazal ze funkcje biblioteczne dzialaja bardzo szybko.