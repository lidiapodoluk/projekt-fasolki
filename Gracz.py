from Karta import *
from Talia import *
from Pole import *
from karty import *


class Gracz:
    def __init__(self, id, nick: str):
        self.id = id
        self.nick = nick
        self.karty_na_rece = []             #list Karta
        self.monety = 0
        self.pola = [Pole(), Pole()]

    def dodaj_karte(self, karta):
        self.karty_na_rece.append(karta)

    def usun_karte(self):
        self.karty_na_rece.pop(0)

    def dodaj_monety(self, liczba):
        self.monety += liczba

    def __str__(self):
        return f"Gracz{{id='{self.id}', nick='{self.nick}', monety={self.monety}, reka={[str(karta) for karta in self.karty_na_rece]}, pola={self.pola}}}"

#test
'''
if __name__ == "__main__":
    gracz = Gracz(0, "Gracz 0")
    karta = Karta("Ogrodnik", [0, 1.5, 2, 3, inf], 6)
    gracz.dodaj_karte(karta)
    gracz.dodaj_karte(karta)
    gracz.usun_karte()
    print(gracz)
'''