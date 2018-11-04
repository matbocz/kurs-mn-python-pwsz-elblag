#ZADANIE 1C
#Napisz funkcje realizujaca interpolacje liniowa dla zbioru danych wejsciowych.
#Przyjmij, ze zbior ten jest dwuwymiarowy.
#Pokaz testbench implementacji dla zbiorow danych pierwotnych wygenerowanych wg funkcji:
#cos(1/x), exp(sin(x)).
#Zbiory danych wejsciowych generuj z krokiem 0.1.
#Wartosci 'x' dla danych interpolowanych generuj 'gesto', np. z krokiem 0.08.
#Przedstaw graficzne interpretacje.

#Przyklad exp(sin(x)).

import numpy as np

import matplotlib.pyplot as pylab

def interplin2p(x,xi,yi,xil,yil):
    return yi+(yil-yi)*(x-xi)/(xil-xi)

def interplinvect(x,xyvect):
    xinterp=[]
    yinterp=[]
    for xk in x:
        N=len(xyvect[0])
        for i in range(0,N-1):
            if(xk>=xyvect[0][i] and xk<xyvect[0][i+1]):
                xinterp.append(xk)
                yinterp.append(interplin2p(xk,xyvect[0][i],xyvect[1][i],xyvect[0][i+1],xyvect[1][i+1]))
            i=i+1
    return [xinterp,yinterp]

xyv=[]
xyv.append([i for i in np.arange(0,3.3,0.1)])
xyv.append([np.exp(np.sin(i)) for i in np.arange(0,3.3,0.1)])

print(xyv)
print(len(xyv[0]))

pylab.plot(xyv[0],xyv[1],'.',xyv[0],xyv[1],'-')
pylab.show()

xin=[i for i in np.arange(0,3.3,0.08)]
xyinterp=interplinvect(xin,xyv)

print(xyinterp)

pylab.plot(xyinterp[0],xyinterp[1],'.',xyv[0],xyv[1],'^r')
pylab.show()

print(len(xyinterp[0]))
print(len(xyinterp[1]))
print(len(xin))