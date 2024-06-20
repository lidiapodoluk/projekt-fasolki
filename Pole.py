from Karta import *
from karty import *

class Pole:
    def __init__(self):
        self.rodzaj_fasolki = None #typu Karta
        self.ilosc = 0
        self.monety = 0

    def sadz_fasolki(self, karta):
        if not self.ilosc:
            self.rodzaj_fasolki = karta
        self.ilosc += 1

    def zbierz_zbiory(self, ile):
        if self.rodzaj_fasolki:
            self.monety += next(((4 - ile_monet) for ile_monet, ile_min_fas in enumerate(reversed(self.rodzaj_fasolki.wartosc)) if ile >= ile_min_fas), 4)
        
        self.ilosc -= ile
        if not self.ilosc:
            self.rodzaj_fasolki = None

    def __str__(self):
        return f"Pole{{rodzaj_fasolki={[str(self.rodzaj_fasolki)]}, ilosc='{self.ilosc}', monety='{self.monety}'}}"


#test
'''
if __name__ == "__main__":
    pole = Pole()
    karta = Karta("Ogrodnik", [0, 1.5, 2, 3, inf], 6)
    pole.sadz_fasolki(karta)
    pole.sadz_fasolki(karta)
    pole.sadz_fasolki(karta)
    print(pole)
    print("Zbiory:", pole.zbierz_zbiory(3))
    print(pole)
'''