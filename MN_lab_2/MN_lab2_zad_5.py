#ZADANIE 5
#Funkcje rysuj z zadania 4 wyposaz w parametr opcja=1.
#Gdy opcja=1 to wlaczona jest siatka oraz kropki w punktach dla ktorych liczona byla funkcja.

import matplotlib.pyplot as plt
import numpy as np

def funkcja(i):
    return i**2

def rysuj(f,xp,xk,k,opcja):
    x=[i for i in np.arange(xp,xk,k)]
    y=[f(i) for i in np.arange(xp,xk,k)]
    plt.ylabel('f(x)')
    plt.xlabel('x')
    plt.title('f(x)=x^2')
    if opcja==1:
        plt.plot(x,y,'ro')
        plt.grid(True)
    else:
        plt.plot(x,y)
    plt.show()
    
rysuj(funkcja,-2,2,0.1,1)