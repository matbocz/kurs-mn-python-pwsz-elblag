#Napisz program obliczajacy n! (silnia) dla z gory ustalonego n.

N=5
wynik=1

for i in range(1,N+1):
    wynik=wynik*i
print("Wynik to: %d" % (wynik))