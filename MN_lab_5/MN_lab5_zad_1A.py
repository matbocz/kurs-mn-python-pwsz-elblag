#ZADANIE 1A
#Napisz program realizujacy interpolacje za pomoca funkcji scipy.interpolaste.interp1d dla zbioru danych wejsciowych.
#Przyjmij, ze zbior ten jest dwuwymiarowy.
#Pokaz testbench implementacji dla zbiorow danych pierwotnych wygenerowanych wg funkcji:
#sin(1/x), exp(cos(x)).
#Zbiory danych wejsciowych generuj z krokiem 0.4 w zakresie -pi do pi.
#Wartosci 'x' dla danych interpolowanych generuj „gesto”, np. z krokiem 0.08.
#Przedstaw graficzne interpretacje typu: 'linear’, ‘nearest’, ‘zero’, ‘slinear’, ‘quadratic, ‘cubic’.

#Funkcja sin(1/x).

from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt

x = [i for i in np.arange(-np.pi, np.pi, 0.4)]
y = [np.sin(1/i) for i in np.arange(-np.pi, np.pi, 0.4)]

xinterp = np.arange(-np.pi, 2.8, 0.08)

opcje = ('linear', 'nearest', 'zero', 'slinear', 'quadratic', 'cubic')
for o in opcje:
    finterp = interp1d(x, y, kind=o)
    plt.plot(xinterp, finterp(xinterp), label=o)
    
plt.plot(x, y, 'or')
plt.legend()
plt.schow()