#ZADANIE 1
#Wygeneruj automatycznie nastepujace pary liczb:
#[(2, 11), (2, 17), (2, 5), (5, 11), (5, 17), (17, 11), (17, 5)]
#Zauwaz, ze wynikiem jest lista zawierajaca pary liczb zapisane w krotkach.
#Napisz kod zgodnie z wytycznymi z wykladu.

s1=[(x,y) for x in [2,5,17] for y in [11,17,5] if x!=y]
print(s1)