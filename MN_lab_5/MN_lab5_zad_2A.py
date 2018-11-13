#Zadanie 2
#Napisz program realizujacy interpolacje za pomoca funkcji numpy.polyfit i numpy.polyval dla zbioru danych wejsciowych.
#Przyjmij, że zbior ten jest dwuwymiarowy.
#Pokaż testbench implementacji dla zbiorow danych pierwotnych wygenerowanych wg funkcji:
#sin(1/x), exp(cos(x)).
#Zbiory danych wejsciowych generuj z krokiem 0.4 w zakresie -pi do pi.
#Wartosci 'x' dla danych interpolowanych generuj „gesto”, np. z krokiem 0.08.
#Przedstaw graficzne interpretacje.

#Przyklad sin(1/x).

import numpy as np
import matplotlib.pyplot as plt

x = [i for i in np.arange(-np.pi, np.pi, 0.4)]
y = [np.sin(1/i) for i in np.arange(-np.pi, np.pi, 0.4)]

wielomian = np.polyfit(x, y, 6)

xinterp = np.arange(-np.pi, 2.8, 0.08)
yinterp = np.polyval(wielomian, xinterp)

plt.plot(x, y, 'or', xinterp, yinterp, '.b')
plt.show()