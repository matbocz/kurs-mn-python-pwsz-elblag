#Napisz program drukujacy N kolejnych liczb parzystych.
#Wykorzystaj petle 'for'.

N=10
x=0

for i in range(0,N*2):
    if i%2==0:
        print("%d. %d" % (x,i))
        x=x+1