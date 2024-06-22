from Karta import *

inf = 100

Nazwa = {
    0   :   "Ogrodnik",
    1   :   "Golas",
    2   :   "Bokser",
    3   :   "Hipis",
    4   :   "Pijak",
    5   :   "Grubas",
    6   :   "Piroman",
    7   :   "Kowboj"
}

Wartosc = {
    0   :   [0, 1.5, 2, 3, inf],
    1   :   [0, 2, 3, 4, 5],
    2   :   [0, 2, 4, 5, 6],
    3   :   [0, 2, 4, 6, 7],
    4   :   [0, 3, 5, 6, 7],
    5   :   [0, 3, 5, 7, 8],
    6   :   [0, 3, 6, 8, 9],
    7   :   [0, 4, 6, 8, 10],
}

Ilosc = {
    0   :   6,
    1   :   8,
    2   :   10,
    3   :   12,
    4   :   14,
    5   :   16,
    6   :   18,
    7   :   20
}

#if __name__ == "__main__":
rodzaje_kart = []
karty = []
str_to_Karta = {}
for i in range (8):
    nazwa, wartosc, ilosc = Nazwa[i], Wartosc[i], Ilosc[i]
    karta = Karta(nazwa, wartosc, ilosc)
    #print(karta)
    rodzaje_kart.append(karta)
    karty.extend([karta] * ilosc)
    str_to_Karta[nazwa] = karta


#test
'''
for karta in rodzaje_kart:
    print (karta)
for karta in karty:
    print(karta)
'''