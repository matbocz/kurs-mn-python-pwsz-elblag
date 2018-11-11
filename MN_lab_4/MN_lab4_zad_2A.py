#ZADANIE 2A
#Napisz funkcje realizujaca interpolacje wielomianowa dla zbioru danych wejsciowych.
#Przyjmij, ze zbior ten jest dwuwymiarowy.
#Pokaz testbench implementacji dla zbiorow danych pierwotnych wygenerowanych wg funkcji:
#sin(1/x), exp(cos(x)).
#Zbiory danych wejsciowych generuj z krokiem 0.1 w zakresie -pi do pi.
#Wartosci 'x' dla danych interpolowanych generuj 'gesto', np. z krokiem 0.08.
#Przedstaw graficzne interpretacje.

#Przyklad z wykladu.

import numpy as np

import matplotlib.pyplot as pylab

def interpolacja_lagrange(x,y,xval):
    products=0
    yval=0
    for i in range(len(x)):
        products=y[i]
        for j in range(len(x)):
            if i!=j:
                products=products*(xval-x[j])/(x[i]-x[j])
        yval=yval+products
    return yval

x=[i for i in np.arange(0,3.3,0.4)]
y=[np.sin(i**2) for i in np.arange(0,3.3,0.4)]

print("x = ",x)
print("y = ",y)

print("interpolowane: xval = %.2f, yval = %.2f" % (1,interpolacja_lagrange(x,y,1)))
print("wartosci dokladne: xval = %.2f, yval = %.2f" % (1,np.sin(1**2)))

pylab.plot(x,y,'o-',label="ounkty danych")
pylab.show()

xval = [i for i in np.arange(0,3.1,0.01)]
yval = []
for xv in xval:
    yval.append(interpolacja_lagrange(x,y,xv))
pylab.plot(xval,yval,"-",label="punkty danych")
pylab.show()