#ZADANIE 4
##Oblicz wspolczynniki zmiennosci bledow dla wszystkich wariantow z zadania 2.
#Przedstaw wnioski.

import numpy as np

def tbernoulli(n):
    if n<0 and n>20:
        return 0
    else:
        temp=[1, 1/2, 1/6, 0, -1/30, 0, 1/42, 0, -1/30, 0, 5/66, 0, -691/2730, 0, 7/6, 0, -3617/510, 0, 43867/798, 0, -174611/330]
        return temp[n]

def silnia(x):
    sil = 1
    while x > 0:
        sil = sil * x
        x = x - 1
    return sil
    
def tsin(x):
    sum_sin=0
    for i in range(0,6):
        sum_sin=sum_sin+((-1)**i)*(x**(2*i+1))/float(silnia(2*i+1))
    return sum_sin

def tcos(x):
    sum_cos=0
    for i in range(0,6):
        sum_cos=sum_cos+((-1)**i)*(x**(2*i))/float(silnia(2*i))
    return sum_cos

def texp(x):
    sum_exp=0
    for i in range(0,6):
        sum_exp=sum_exp+(x**i)/float(silnia(i))
    return sum_exp

def ttan(x):
    sum_tan=0
    for i in range(0,6):
        sum_tan=sum_tan+tbernoulli(2*i)*((-4)**i)*(1-(4**i))*(x**(2*i-1))/float(silnia(2*i))
    return sum_tan

def blad_bw_V(f1,f2,xp,xk,k):
    srednia=0
    bledy=[np.abs(f1(i)-f2(i)) for i in np.arange(xp,xk,k)]
    srednia=sum(bledy)/len(bledy)
    return np.std(bledy)/srednia

print("Sin")
print(blad_bw_V(tsin,np.sin,-3*np.pi,0,0.1))
print(blad_bw_V(tsin,np.sin,0,np.pi/4,0.1))
print(blad_bw_V(tsin,np.sin,-3*np.pi,3*np.pi,0.1))

print("\nCos")
print(blad_bw_V(tcos,np.cos,-3*np.pi,0,0.1))
print(blad_bw_V(tcos,np.cos,0,np.pi/4,0.1))
print(blad_bw_V(tcos,np.cos,-3*np.pi,3*np.pi,0.1))

print("\nExp")
print(blad_bw_V(texp,np.exp,0,20,0.1))
print(blad_bw_V(texp,np.exp,0,1,0.1))

print("\nTan")
print(blad_bw_V(ttan,np.tan,-np.pi,2,0.1))
print(blad_bw_V(ttan,np.tan,0.1,np.pi/2,0.1))
print(blad_bw_V(ttan,np.tan,-np.pi/2,np.pi/2,0.1))

#Wspolczynnik zmiennosci rosnie,
#wraz z poszerzaniem sie zakresu danych.
#Wspolczynnik zmiennosci pokazuje ze algorytm nie radzi sobie z obliczeniami,
#szczegolnie w szerokim zakresie danych.