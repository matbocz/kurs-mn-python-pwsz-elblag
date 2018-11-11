#ZADANIE 4
#Napisz program obliczajacy i drukujacy rozwiazanie rownania kwadratowego.
#Wykonaj test programu dla uzyskania rozwiazan rzeczywistych i zespolonych.
#Porownaj dzialanie programu z www.wolframalpha.com.

import math

a=6
b=3
c=9

if a==0 and b==0 and c==0:
    print("Rownanie tozsame")
elif a==0 and b==0 and c!=0:
    print("Rownanie sprzeczne")
elif a==0:
    print("Rownanie liniowe")
    x1=-c/b
    print("x1 = %f" % x1)
elif a!=0:
    print("Rownanie kwadratowe")
    delta=(b*b)-(4*a*c)
    if delta==0:
        print("Delta rowna 0")
        x1=-b/(2*a)
        print("x1 = %f" % x1)
    if delta>0:
        print("Delta wieksza od 0")
        p=math.sqrt(delta)
        x1=(-b+p)/(2*a)
        x2=(-b-p)/(2*a)
        print("x1 = %f, x2 = %f" % (x1,x2))
    if delta<0:
        print("Delta mniejsza od 0")
        p=math.sqrt(-delta)
        re=-b/(2*a)
        im=p/(2*a)
        print("x1 = %.2lf+%.2lfi, x2 = %.2lf-%.2lfi" % (re,im,re,im));