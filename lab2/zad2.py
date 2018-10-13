#Zadanie 2
#Podaj procentowe roznice miedzy liczbami:
#[0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1. ] (efekt instrukcji print(np.arange(0,1.1,0.1)))
#a liczbami rzeczywistymi (float32) generowanymi na biezaco poprzez iteracyjne sumowanie x=x+0.1 (w pierwszym kroku x=0).

import numpy as np

x=np.float32(0.0)

for i in np.arange(0,1.1,0.1):
    print("i = %.20f" % i)
    print("x = %.20f" % x)
    print("Roznica = %.20f" % abs(x-i))
    x=x+0.1