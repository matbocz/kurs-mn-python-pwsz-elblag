#ZADANIE 1
#Napisz funkcje tsin(x), tcos(x), texp(x) i ttan(x) realizujace takie same operacje jak funkcje biblioteczne:
#numpy.sin(x), numpy.cos(x), numpy.exp(x) i numpy.tan(x).
#We wlasnych funkcjach wykorzystaj rozwiniecie w szereg Taylora (https://en.wikipedia.org/wiki/Taylor_series).
#W celu poprawnego rozwiazania zadania nalezy dodatkowo napisac funkcje realizujaca n! (silnia).

import numpy as np

def tbernoulli(n):
    if n<0 and n>20:
        return 0
    else:
        temp=[1, 1/2, 1/6, 0, -1/30, 0, 1/42, 0, -1/30, 0, 5/66, 0, -691/2730, 0, 7/6, 0, -3617/510, 0, 43867/798, 0, -174611/330]
        return temp[n]

def silnia(x):
    sil=1
    while x>0:
        sil=sil*x
        x =x-1
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

x=np.pi/3

print('sin(%.2f)=%.12f' % (x,tsin(x)))
print('cos(%.2f)=%.12f' % (x,tcos(x)))
print('exp(%.2f)=%.12f' % (x,texp(x)))
print('tan(%.2f)=%.12f' % (x,ttan(x)))