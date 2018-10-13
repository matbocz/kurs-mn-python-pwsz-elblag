#Zadanie 3
#Napisz funkcje suma i funkcje iloczyn, ktora zwraca wynik sumy oraz iloczynu.
#Funkcja ma posiadac nastepujace parametry: f – funkcja, xp – poczatek zakresu, xk – koniec zakresu, k – krok.
#Przetestuj dzialanie funkcji dla zakresu xp=-3.14, xk = 3.14 i kroku 0.01.
#Napisz wlasna funkcje realizujaca f(x)=1/x.
#Podstaw ja do funkcji suma i iloczyn.
#Podstaw rowniez funkcje f(x)=sin(x) (z biblioteki numpy: numpy.sin()).

import numpy as np

def suma(xp,xk,k):
    wynik=0
    while xp<=xk:
        wynik=wynik+xp
        xp=xp+k
    return wynik

def iloczyn(xp,xk,k):
    wynik=1
    while xp<=xk:
        wynik=wynik*xp
        xp=xp+k
    return wynik

def odwroc(x):
    try:
        wynik=1.0/x
    except ZeroDivisionError:
        wynik=0
    return wynik

def sinus(x):
    return np.sin(x)
   
print("%f" % suma(-3.14,3.14,0.01))
print("%f" % iloczyn(1,5,1))
print("%f" % odwroc(4))
print("%f" % sinus(90))