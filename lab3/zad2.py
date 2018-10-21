#Oblicz blad wzgledny i bezwzgledny,
#wyciagnij poprawne wnioski nt. Implementacji funkcji z zadania 1.
#Zestaw bledy dla nastepujacych wariantow:
#a) miedzy tsin(x) a numpy.sin(x) dla x w zakresach: [-3pi,0], [0,pi/4], [-3pi,3pi]
#b) miedzy tcos(x) a numpy.cos(x) dla x w zakresach: [-3pi,0], [0,pi/4], [-3pi,3pi]
#c) miedzy texp(x) a numpy.exp(x) dla x w zakresach: [0,20], [0,1]
#d) miedzy ttan(x) a numpy.tan(x) dla x w zakresach: [-pi/2,0], [0,pi/2], [-pi/2,pi/2]

import numpy as np

def tbernoulli(n):
    if n<0 and n>20:
        return 0
    else:
        temp=[1, 1/2, 1/6, 0, -1/30, 0, 1/42, 0, -1/30, 0, 5/66, 0, -691/2730, 0, 7/6, 0, -3617/510, 0, 43867/798, 0, -174611/330]
        return temp[n]

def silnia(x):
    sil = 1
    while x > 0:
        sil = sil * x
        x = x - 1
    return sil
    
def tsin(x):
    sum_sin=0
    for i in range(0,6):
        sum_sin=sum_sin+((-1)**i)*(x**(2*i+1))/float(silnia(2*i+1))
    return sum_sin

def tcos(x):
    sum_cos=0
    for i in range(0,6):
        sum_cos=sum_cos+((-1)**i)*(x**(2*i))/float(silnia(2*i))
    return sum_cos

def texp(x):
    sum_exp=0
    for i in range(0,6):
        sum_exp=sum_exp+(x**i)/float(silnia(i))
    return sum_exp

def ttan(x):
    sum_tan=0
    for i in range(0,6):
        sum_tan=sum_tan+tbernoulli(2*i)*((-4)**i)*(1-(4**i))*(x**(2*i-1))/float(silnia(2*i))
    return sum_tan

x=(-3)*np.pi
while x<=0:
    Bbw=np.abs(tsin(x)-np.sin(x))
    Bw=(Bbw/x)*100
    print('sin(%.2f)=%.12f, tsin(%.2f)=%.12f, Bbw=%.17f, Bw=%.17f' % (x,np.sin(x),x,tsin(x),Bbw,Bw))
    x=x+0.1
    
x=0.1
while x<=np.pi/4:
    Bbw=np.abs(tsin(x)-np.sin(x))
    Bw=(Bbw/x)*100
    print('sin(%.2f)=%.12f, tsin(%.2f)=%.12f, Bbw=%.17f, Bw=%.17f' % (x,np.sin(x),x,tsin(x),Bbw,Bw))
    x=x+0.1
    
x=(-3)*np.pi
while x<=3*np.pi:
    Bbw=np.abs(tsin(x)-np.sin(x))
    Bw=(Bbw/x)*100
    print('sin(%.2f)=%.12f, tsin(%.2f)=%.12f, Bbw=%.17f, Bw=%.17f' % (x,np.sin(x),x,tsin(x),Bbw,Bw))
    x=x+0.1
    
x=(-3)*np.pi
while x<=0:
    Bbw=np.abs(tcos(x)-np.cos(x))
    Bw=(Bbw/x)*100
    print('cos(%.2f)=%.12f, tcos(%.2f)=%.12f, Bbw=%.17f, Bw=%.17f' % (x,np.cos(x),x,tcos(x),Bbw,Bw))
    x=x+0.1
    
x=0.1
while x<=np.pi/4:
    Bbw=np.abs(tcos(x)-np.cos(x))
    Bw=(Bbw/x)*100
    print('cos(%.2f)=%.12f, tcos(%.2f)=%.12f, Bbw=%.17f, Bw=%.17f' % (x,np.cos(x),x,tcos(x),Bbw,Bw))
    x=x+0.1
    
x=(-3)*np.pi
while x<=3*np.pi:
    Bbw=np.abs(tcos(x)-np.cos(x))
    Bw=(Bbw/x)*100
    print('cos(%.2f)=%.12f, tcos(%.2f)=%.12f, Bbw=%.17f, Bw=%.17f' % (x,np.cos(x),x,tcos(x),Bbw,Bw))
    x=x+0.1
    
x=1
while x<=20:
    Bbw=np.abs(texp(x)-np.exp(x))
    Bw=(Bbw/x)*100
    print('exp(%.2f)=%.12f, texp(%.2f)=%.12f, Bbw=%.17f, Bw=%.17f' % (x,np.exp(x),x,texp(x),Bbw,Bw))
    x=x+0.1

x=0.1
while x<=1:
    Bbw=np.abs(texp(x)-np.exp(x))
    Bw=(Bbw/x)*100
    print('exp(%.2f)=%.12f, texp(%.2f)=%.12f, Bbw=%.17f, Bw=%.17f' % (x,np.exp(x),x,texp(x),Bbw,Bw))
    x=x+0.1
    
x=-np.pi
while x<=2:
    Bbw=np.abs(texp(x)-np.exp(x))
    Bw=(Bbw/x)*100
    print('tan(%.2f)=%.12f, ttan(%.2f)=%.12f, Bbw=%.17f, Bw=%.17f' % (x,np.tan(x),x,ttan(x),Bbw,Bw))
    x=x+0.1
    
x=0.1
while x<=np.pi/2:
    Bbw=np.abs(texp(x)-np.exp(x))
    Bw=(Bbw/x)*100
    print('tan(%.2f)=%.12f, ttan(%.2f)=%.12f, Bbw=%.17f, Bw=%.17f' % (x,np.tan(x),x,ttan(x),Bbw,Bw))
    x=x+0.1
    
x=-np.pi/2
while x<=np.pi/2:
    Bbw=np.abs(texp(x)-np.exp(x))
    Bw=(Bbw/x)*100
    print('tan(%.2f)=%.12f, ttan(%.2f)=%.12f, Bbw=%.17f, Bw=%.17f' % (x,np.tan(x),x,ttan(x),Bbw,Bw))
    x=x+0.1
    
#Jezeli zakres danych jest niewielki,
#to funkcje napisane samodzielnie i funkcje biblioteczne,
#zwracają podobne wyniki.
#Jezeli zakres danych jest duzy,
#to wyniki bardzo sie roznia.