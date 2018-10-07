#Uruchom ponizszy kod.
#Wyjasnij (opisz) jaki algorytm jest przez niego realizowany?

x=3.0
xn=0.1
blad=0.000001
x_old=0

while abs(x_old-xn)>blad:
    x_old=xn
    xn=(xn+x/xn)/2

print("x = %lf" % xn)

#Algorytm wykonuje pierwiastkowanie liczby x.
#Wykorzystuje petle while ktora wykonuje sie dopoki wartosc absolutna wyrazenia (x_old-xn) jest wieksza od zmiennej blad.
#Wartosci zmiennych x_old oraz xn sa zmieniane podczas wykonywania petli while.