#ZADANIE 1
#Korzystajac z kodu zawartym w pliku lab7 approx polynomial wykonaj nastepujace eksperymenty:
#– wygeneruj dane zbioru aproksymowanego stosujac funkcje f(x) = ax6 + bx2 +cx + random();
#przyjmij nastepujace wartosci wspolczynnikow:
#a = liczba liter imienia, b = liczba liter nazwiska, c = numer domu adresu zamieszkania
#– wykonaj aproksymacje wielomianowa dla wielomianow stopnia m=3,5,7,10

import numpy as np
import math
import matplotlib.pyplot as plt

#rownania liniowe: eliminacja Gaussa
def swapRows(v,i,j):
    if len(v.shape) == 1:
        v[i],v[j] = v[j],v[i]
    else:
        v[[i,j],:] = v[[j,i],:]
        
def swapCols(v,i,j):
    v[:,[i,j]] = v[:,[j,i]]

def gaussPivot(a,b,tol=1.0e-12):
    n = len(b)

    # Set up scale factors
    s = np.zeros(n)
    for i in range(n):
        s[i] = max(np.abs(a[i,:]))   
        
    for k in range(0,n-1):
        # Row interchange, if needed
        p = np.argmax(np.abs(a[k:n,k])/s[k:n]) + k
        if abs(a[p,k]) < tol:
            print('Matrix is singular')
        if p != k:
            swapRows(b,k,p)
            swapRows(s,k,p)
            swapRows(a,k,p)
            
        # Elimination
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                lam = a[i,k]/a[k,k]
                a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                b[i] = b[i] - lam*b[k]

    if abs(a[n-1,n-1]) < tol:
        print('Matrix is singular')
    
    # Back substitution
    b[n-1] = b[n-1]/a[n-1,n-1]
    for k in range(n-2,-1,-1):
        b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    
    return b
        
#aproksymacja wielomianowa
def polyFit(xData,yData,m):
    a = np.zeros((m+1,m+1))
    b = np.zeros(m+1)
    s = np.zeros(2*m+1)
    
    for i in range(len(xData)):
        temp = yData[i]
        for j in range(m+1):
            b[j] = b[j] + temp
            temp = temp*xData[i]

        temp = 1.0
        for j in range(2*m+1):
            s[j] = s[j] + temp
            temp = temp*xData[i]

    for i in range(m+1):
        for j in range(m+1):
            a[i,j] = s[i+j]

    return gaussPivot(a,b)
        
def stdDev(c,xData,yData):
    
    def evalPoly(c,x):
        m = len(c) - 1
        p = c[m]
        for j in range(m):
            p = p*x + c[m-j-1]
        return p
    
    n = len(xData) - 1
    m = len(c) - 1
    sigma = 0.0
    for i in range(n+1):
        p = evalPoly(c,xData[i])
        sigma = sigma + (yData[i] - p)**2

    sigma = math.sqrt(sigma/(n - m))
    return sigma
            
def plotPoly(xData,yData,coeff,xlab='x',ylab='y'):
    m = len(coeff)
    x1 = min(xData)
    x2 = max(xData)
    dx = (x2 - x1)/20.0#wyliczenie kroku
    x = np.arange(x1,x2 + dx/10.0,dx)
    y = np.zeros((len(x)))*1.0
    for i in range(m):#obliczanie wielomianu
        y = y + coeff[i]*x**i
    plt.plot(xData,yData,'o',x,y,'-')
    plt.xlabel(xlab); plt.ylabel(ylab)
    plt.grid (True)
    plt.show()
        
def main():
    x = np.arange(0, 3.6, 0.4)
    y = 7 * x**6 + 9 * x**2 + 8 * x + np.random.normal(scale=200, size=len(x))
    
    print("\nWielomian stopnia 3")
    coeff = polyFit(x, y, 3)
    plotPoly(x, y, coeff)
    
    print("\nWielomian stopnia 5")
    coeff = polyFit(x, y, 5)
    plotPoly(x, y, coeff)
    
    print("\nWielomian stopnia 7")
    coeff = polyFit(x, y, 7)
    plotPoly(x, y, coeff)
    
    print("\nWielomian stopnia 10")
    coeff = polyFit(x, y, 10)
    plotPoly(x, y, coeff)

if __name__ == "__main__":
    main()
    
#Jako parametry do funkcji polyfit sa przekazywane
#zbiory aproksymowane oraz stopien wielomianu.
#W funkcji tworzone sa macierze A i b oraz wektor s,
#w ktorym skladowane sa obliczenia posrednie.
#W petlach obliczana jest zawartosc macierzy A oraz b.
#Funkcja rozwiazuje uklad rownan Aa = b.
#Funkcja zwraca wektor wspolczynnikow a.
#Do aproksymacji najlepiej nadaja sie wielomiany niskiego rzedu,
#poniewaz wysoki rzad wprowadza zaburzenie.