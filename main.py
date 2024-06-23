import pygame
import sys
from Scenes import *
from scene_manager import *
from GameScene import *
from Menu import *
from Gracz import *
from Gra import *
from zmienne import *

# Inicjalizacja Pygame
pygame.init()


# Ustawienia ekranu
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fasolki")


# Inicjalizacja gry i graczy
gracz0 = Gracz(0, "Ty")
gracz1 = Gracz(1, "Gracz 1")
gracz2 = Gracz(2, "Gracz 2")
gra = Gra([gracz0, gracz1, gracz2])
gra.startGame()

# Inicjalizacja menedżera scen
scene_manager = SceneManager(screen)
scene_manager.add_scene("menu", MenuScene(screen))
scene_manager.add_scene("game", GameScene(screen, gra))
scene_manager.set_scene("menu")

# Główna pętla
running = True
while running:
    events = pygame.event.get()
    scene_manager.handle_events(events)
    scene_manager.update()
    scene_manager.draw()
    pygame.display.flip()
