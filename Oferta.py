from Gracz import *
from Karta import *


class Oferta:
    def __init__(self, oferujacy, co_chce, co_oddaje):
        self.oferujacy = oferujacy  #Instancja klasy Gracz
        self.co_chce = co_chce      #Instancja klasy Karta (moze bedzie tu lista)
        self.co_oddaje = co_oddaje  #Instancja klasy Karta (moze bedzie tu lista)
        
    def zloz_oferte(self):
        # Logika składania oferty
        pass

    def akceptuj_oferte(self, akceptujacy):
        # Logika akceptacji oferty
        return True
        pass

    def odrzuc_oferte(self):
        pass
