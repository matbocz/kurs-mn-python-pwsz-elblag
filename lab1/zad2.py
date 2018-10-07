#Napisz program drukujacy tablice wartosci 4 funkcji trygonometrycznych dla podanego zakresu [xp, xk].
#Wartosci xp i xk moga byc hardkodowane w programie.

import numpy as np

xp=0
xk=2*np.pi
krok=0.1

liczba_punktow=np.abs((xk-xp)/krok) #wyznacz liczbe punktow
liczba_punktow_int=int(np.ceil(liczba_punktow)) #zadbaj o zgodnosc typow

print("Liczba punktow wartosci x: %d \n" % liczba_punktow)

x=xp
for i in range(0,liczba_punktow_int):
    x=x+krok
    print("%d. sin(%f) = %f, cos(%f) = %f, tan(%f) = %f, ctg(%f) = %f" % (i,x,np.sin(x),x,np.cos(x),x,np.tan(x),x,1.0/np.sin(x)))