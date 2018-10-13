#Zadanie 4
#Napisz funkcje rysuj, ktora umozliwi rysowanie wykresow funkcji przekazanych jako parametr.
#Funkcja ma posiadac nastepujace parametry: f – funkcja, xp – poczatek zakresu, xk – koniec zakresu, k – krok.
#Funkcja ma miec zaimplementowana pelna procedure rysowania przy uzyciu 'plot' (biblioteka matplotlib.pyplot).

import matplotlib.pyplot as plt
import numpy as np

def funkcja(i):
    return i**2

def rysuj(f,xp,xk,k):
    x=[i for i in np.arange(xp,xk,k)]
    y=[f(i) for i in np.arange(xp,xk,k)]
    plt.plot(x,y)
    plt.ylabel('f(x)')
    plt.xlabel('x')
    plt.title('f(x)=x^2')
    plt.show()
    
rysuj(funkcja,-2,2,0.1)