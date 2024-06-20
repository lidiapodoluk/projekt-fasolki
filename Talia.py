from karty import *
from Karta import *
import random

class Talia:
    def __init__(self, karty):
        self.karty = karty

    def potasuj(self):
        random.shuffle(self.karty)

    def get_card(self):
        return self.karty.pop() if self.karty else None

    def __str__(self):
        return f"Talia{{karty={len(self.karty)}}}"

rodzaje_kart = []
karty = []
for i in range (8):
    nazwa, wartosc, ilosc = Nazwa[i], Wartosc[i], Ilosc[i]
    karta = Karta(nazwa, wartosc, ilosc)
    #print(karta)
    rodzaje_kart.append(karta)
    karty.extend([karta] * ilosc)

#test
'''
if __name__ == "__main__":
    talia = Talia(karty)
    talia.potasuj()
    print(talia)
    print(talia.get_card())
    print(talia.get_card())
    print(talia.get_card())
'''