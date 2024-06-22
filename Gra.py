from Gracz import *
from Pole import *
from Karta import *
from karty import *
from Talia import *
from Tura import *
from Akcja import *
from Oferta import *
import random 


class Gra:
    def __init__(self, gracze):
        self.gracze = gracze
        self.talia = Talia(karty)
        self.current_index = None

    def addPlayer(self, new_player: Gracz):
        self.gracze.append(new_player)

    def startGame(self):
        def rozdajKarty (talia):
            for j in range(5):
                for i in range (len(self.gracze)): 
                    self.gracze[i].karty_na_rece.append(talia.get_card())
            return talia
        
        self.talia = Talia(karty)
        self.talia.potasuj()
        self.talia = rozdajKarty(self.talia)

        self.current_index = 0

        return True
    
    def endGame(self):
        for i, gracz in enumerate(self.gracze):
            self.gracze[i].monety = gracz.pola[0].monety + gracz.pola[1].monety
        winner = max(self.gracze, key=lambda x: x.monety, default=None)
        return winner
    
    def nextTurn(self):
        self.current_index = (self.current_index + 1) % len(self.gracze)
    
    '''
    def getCurrentPlayer(self):
        return self.players[self.current_index].id
    '''
    def play(self, player: Gracz):
        if len(self.talia.karty) < 2:
            self.endGame()
        
        print ()
        print("Tura gracza:  ", player.nick)

        #tura użytkownika
        if self.current_index == 0:   

            #sadzenie 1 lub 2 fasoli z kart z ręki

            print ("Jaka akcje chcesz wykonac? (z = zasadz):   ", end='')
            
            akcja = input()
            if akcja == "z":    #zasadz
                akcja = SadzFasoleZReki(player)
                akcja.wykonaj()

            print ("Jaka akcje chcesz wykonac? (z = zasadz, s = skip):   ", end='')

            akcja = input()
            if akcja == "z":    #zasadz
                akcja = SadzFasoleZReki(player)
                akcja.wykonaj()

            #print("len(talia):  ", self.talia)

            #wyciągnięcie 2 kart przeznaczonych do handlu
            dobrane_karty = [self.talia.karty.pop(), self.talia.karty.pop()]
            print("dobrane karty do handlu:  ", dobrane_karty[0], dobrane_karty[1])

            #składanie oferty
            do_posadzenia = [[] for _ in range (len(self.gracze))]
            do_posadzenia[self.current_index].append(dobrane_karty[0])
            do_posadzenia[self.current_index].append(dobrane_karty[1])
            
            print("Czy chcesz handlowac? (y/n)")
            akcja = input()
            if akcja == "y":
                print("Co chcesz? :  ", end='')
                co_chce = str_to_Karta[input()]
                print("Co oferujesz? :  ", end='')
                co_oferuje = str_to_Karta[input()]
                oferta = Oferta(player, co_chce, co_oferuje)

                #tymczasowo
                player2 = self.gracze[1]

                if oferta.akceptuj_oferte(player2):

                    def find_first_card(cards_on_hand, card):
                        try:
                            for i in range (len(cards_on_hand)):
                                if cards_on_hand[i] == card:
                                    del cards_on_hand[i]
                                    return cards_on_hand
                        except card not in cards_on_hand:
                            print("Error! Gracz nie ma tej karty na rece wiec nie moze jej oddac!\n")         
                            #
                    

                    oferujacy = oferta.oferujacy    
                    co_chce = oferta.co_chce
                    co_oferuje = oferta.co_oddaje 
                    
                    '''
                    print("\n\n testuje ifa: ")
                    print(oferujacy)
                    print(player)
                    print(co_oferuje)
                    print(dobrane_karty[0], dobrane_karty[1])
                    '''

                    if oferujacy == player and co_oferuje in dobrane_karty:
                        dobrane_karty.remove(co_oferuje)
                        do_posadzenia[oferujacy.id].remove(co_oferuje)
                        do_posadzenia[player2.id].append(co_oferuje)
                        do_posadzenia[oferujacy.id].append(co_chce)
                        player2.karty_na_rece = find_first_card(player2.karty_na_rece, co_chce)

                        
                        print("\n\nkarty na rece i karty do sadzenia po wymianie handlowej :\n")
                        print (oferujacy)
                        for karta in do_posadzenia[oferujacy.id]:
                            print(karta)
                        print("\n", player2)
                        for karta in do_posadzenia[player2.id]:
                            print(karta)

                    else:
                        print("not implemented")
                            
                    
                            
                    



            '''    
                kolejnosc = [0,1]
                if (random.randint(0, 2) == 0):
                    kolejnosc = [1, 0]
                for index in kolejnosc:
                    return 
                    #if Bot[index].akceptuj_oferte(oferta):
                        #next
                    #if Bot[index].odrzuc_oferte(oferta):
                        #next

            else:   #akcja == "n", nie handluję, od razu przechodzę do sadzenia 2 dobranych fasol
                return
            '''

            

            #dobranie karty po ukończeniu swojej tury
            player.karty_na_rece.append(self.talia.karty.pop())

            print("len(talia):  ", self.talia)
            print("karty na rece gracza:  ", player)



            

        #tura bota
        else:
            return
            
        #obsluzyc konczenie gry w sensie podliczanie hajsu itd 
        
        #musi byc tak ze najpierw TRZEBA zasadzic chociaz jedna
        #if action == "zasadz": 
            #karta = gracz.karty_na_rece[0] 
            #if not wybrane_pole rodzaj = karta.rodzaj:
                #zbierz_zbiory_wybrane_pole
                #trzeba obsluzyc monety
            #zasadz 
         #2x powyzszy fragment
        
        #2 wylosowane karty 
        #wyswietl na srodku
        #opcje: zasadz/ handluj
        # zloz oferte co chcesz w zamian za co (takze nic)
          #losuj gracza ktory 1szy rozpatrzy oferte
            # jesli zaakceptuje
              # implementacja dojscia do skutku transakcji i jej efektow
          # 2 graczy sklada lub nie oferty
          # jesli zaakceptuję
            # implementacja dojscia do skutku transakcji i jej efektow
          # jesli nie -> 
            #sadzenie fasoli ktorą muszę
          # sadzenie przehandlowanych fasoli + wyliczenie hajsu
          # nextTurn()
 

        return
    '''
    def Game(self):
        while (True):
            player = self.gracze[self.current_index]
            play(player)
            #Tura(player)
            #nextTurn()
    '''

#test
if __name__ == "__main__":

    
    gracz0 = Gracz(0, "Gracz 0")
    gracz1 = Gracz(1, "Gracz 1")
    gracz2 = Gracz(2, "Gracz 2")
    g = Gra([])
    g.addPlayer(gracz0)
    g.addPlayer(gracz1)
    g.addPlayer(gracz2)

    g.startGame()
    print(g.talia)

    for p in g.gracze:
        print (p)
        print()
    #g.nextTurn()
    print()



    #g.Game()
    print("len(talia):  ", g.talia)

    while (True):
        player = g.gracze[g.current_index]
        g.play(player)
        #Tura(player)
        g.nextTurn()
        if len(g.talia.karty) < 70:
            winner = g.endGame()
            print("WYGRAL GRACZ: ")
            print(winner)
            exit(0)

