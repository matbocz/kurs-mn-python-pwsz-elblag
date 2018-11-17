#ZADANIE 3
#Uruchom przyklad z wykladu 5b (slajdy 11-15) dotyczacy interpolacji.

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QLabel, QGridLayout,
                             QLineEdit, QApplication)
from matplotlib.pyplot import plot, show
from scipy import interpolate
from numpy import arange, exp

class Program(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.lbl1 = QLabel('podaj: xp,xk,krok (oddziel przecinkiem)')#etykieta
        self.lbl2 = QLabel('Uruchom')#etykieta
        self.btn1 = QPushButton('GO')#przycisk
        self.text1 = QLineEdit()#pole tekstowe

        #siatka pomaga w rozmieszczeniu obiektow
        siatka = QGridLayout()
        siatka.setSpacing(10)

        siatka.addWidget(self.lbl1, 1, 0)#dodaj etykiete
        siatka.addWidget(self.text1, 1, 1)#dodaj pole tekstowe

        siatka.addWidget(self.lbl2, 2, 0)#dodaj etykiete
        siatka.addWidget(self.btn1, 2, 1)#dodaj przycisk

        self.setLayout(siatka)#wlacz siatke

        #zdarzenia
        #laczy zdarzenie przycisniecia przycisku z funkcja btn1Clicked()
        self.btn1.clicked.connect(self.btn1Clicked)
        
        self.setGeometry(300, 300, 450, 150)
        self.setWindowTitle('Przykład: pole/przycisk')
        self.show()

    def btn1Clicked(self):
        sender = self.sender()#kto wygenerowal zdarzenie?
        txt1 = self.text1.text()#pobierz tekst z pola
        txt1split = txt1.split(',');
        txt1final = 'xp='+txt1split[0]+' xk='+txt1split[1]+' krok='+txt1split[2]
        self.text1.clear()#wyczysc pole
        self.text1.insert(txt1final)#drukuj w polu
        xp=float(txt1split[0])
        xk=float(txt1split[1])
        k=float(txt1split[2])
        self.interpolacja(xp,xk,k)
        #plt.savefig('wykres.png')       
        print(float(txt1split[0]), float(txt1split[1]), float(txt1split[2]))
        print('Nacisnieto przycisk: ',sender.text())#drukuj w wierszu polecen
        print(txt1final)#drukuj w wierszu polecen

    def interpolacja(self,xp,xk,k):
        print('xp, xk, k:',xp, xk, k)
        x = arange(xp, xk,1)
        print('x=',x)
        y = exp(-x/3.0)
        print('y=',y)
        # uzycie funkcji interpolujacej `interp1d`
        f = interpolate.interp1d(x, y)
        xnew = arange(xp, x[-1], k)
        print('xnew=',xnew)
        ynew = f(xnew)#obliczenie interpolacji
        print('ynew=',ynew)
        plot(x, y, 'o', xnew, ynew, '-')
        show() 
      
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Program()
    sys.exit(app.exec_())