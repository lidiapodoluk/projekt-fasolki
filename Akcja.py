from Gracz import *
from Pole import *
from Karta import *
from Talia import *
from Tura import *
import random 
from abc import ABC, abstractmethod

class Akcja(ABC):
    def __init__(self, player):
        self.player = player

    @abstractmethod
    def wykonaj(self):
        pass


class SadzFasoleZReki(Akcja):
    '''
    def __init__(self, player, karta, pole_index):
        super().__init__(player)
        self.karta = karta
        self.pole_index = pole_index
    '''

    def __init__(self, player):
        super().__init__(player)

    def wykonaj(self):
        try:
            karta = self.player.karty_na_rece.pop(0)
            print ("Na ktorym polu? (0/1):   ", end='')
            wybrane_pole = int(input())
            pole = self.player.pola[wybrane_pole]
            if not pole.rodzaj_fasolki == karta:
                #akcja = ZbierzZbiory(player, pole, ilosc)
                #akcja.wykonaj()
                pole.zbierz_zbiory(pole.ilosc)
            pole.sadz_fasolki(karta)

            print("     przed")
            print("Pola gracza po zasadzeniu:  ", end='')
            for p in self.player.pola:
                print(p, end=', ')
            print()
            print("     przed")
        except not len(self.player.karty_na_rece):
            print("Error! Gracz nie ma kart na rece")  


