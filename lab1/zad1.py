#Uruchom ponizszy kod.
#Kod demonstruje uzycie kilku funkcji numerycznych pochodzacych z biblioteki.
#Podstawowa biblioteka funkcji numerycznych to NumPy.
#W rezultacie dzialania programu obliczono i wydrukowano wartosci 4 funkcji trygonometrycznych.

#import biblioteki NumPy do przestrzeni nazw np;
#funkcje dostepne sa z poziomu przestrzeni nazw 'np'
import numpy as np

#tworz zmienną x
x=np.pi/3

#oblicz wartosci f trygonometrycznych
print("sin(%f) = %f" % (x,np.sin(x)))
print("cos(%f) = %f" % (x,np.cos(x)))
print("tan(%f) = %f" % (x,np.tan(x)))
print("ctg(%f) = %f" % (x,1.0/np.sin(x)))