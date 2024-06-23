import sys
import pygame
from scene_manager import Scene
from zmienne import *

class GameScene(Scene):
    def __init__(self, screen, game):
        super().__init__(screen)
        self.game = game
        self.player = self.game.gracze[0]
        self.card_images = {}
        self.pole_image = None
        self.rewers_image = None

        # Karty, pola i rewers
        for card in self.player.karty_na_rece:
            card_image = pygame.image.load(f'/home/lidia/Pulpit/projekt/projekt-fasolki/img/{card.rodzaj_fasolki}.jpg')
            card_image = pygame.transform.scale(card_image, CARD_SIZE)
            self.card_images[card.rodzaj_fasolki] = card_image
        
        self.pole_image = pygame.image.load(f'/home/lidia/Pulpit/projekt/projekt-fasolki/img/Pole.jpg')
        self.pole_image = pygame.transform.scale(self.pole_image, POLE_SIZE)

        self.rewers_image = pygame.image.load('/home/lidia/Pulpit/projekt/projekt-fasolki/img/rewers.jpg')
        self.rewers_image = pygame.transform.scale(self.rewers_image, CARD_SIZE)


    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        return None

    def update(self):
        pass

    def draw(self):
        self.screen.fill(LIGHT_BLUE)
        
        # Karty gracza
        card_width, card_height = CARD_SIZE
        spacing = 10
        num = len(self.player.karty_na_rece)
        start_x = [0, 0, 0]
        start_y = [0, 0, 0]
        start_x[0] = (SCREEN_WIDTH - (num * card_width + (num - 1) * spacing)) // 2
        start_y[0] = SCREEN_HEIGHT - card_height - 100
        
        # Rysowanie gracza 0 (użytkownika)
        for i, card in enumerate(self.player.karty_na_rece):
            card_x = start_x[0] + i * (card_width + spacing)
            card_y = start_y[0]
            self.screen.blit(self.card_images[card.rodzaj_fasolki], (card_x, card_y))
            
            # Rysowanie numeru karty
            font = pygame.font.SysFont(None, 40)
            text_surf = font.render(str(i + 1), True, BLACK)
            text_rect = text_surf.get_rect(center=(card_x + card_width // 2, card_y + card_height + 20))
            self.screen.blit(text_surf, text_rect)

        # Rysowanie pola
        pole_width, pole_height = POLE_SIZE
        pole_x = [0, 0, 0]
        pole_y = [0, 0, 0]
        pole_x[0] = start_x[0] - spacing - pole_width
        pole_y[0] = start_y[0]
        self.screen.blit(self.pole_image, (pole_x[0], pole_y[0]))

        start_x[1] = pole_x[0]
        start_y[1] = 80

        pole_x[1] = start_x[1]
        pole_y[1] = start_y[1]
        pole_x[2] = SCREEN_WIDTH - pole_x[1] - (pole_width + spacing + card_width)
        pole_y[2] = pole_y[1]
        
        # Rysowanie pól, kart i nicków pozostałych graczy
        for i in range(1, len(self.game.gracze)):
            self.screen.blit(self.pole_image, (pole_x[i], pole_y[i]))
            self.screen.blit(self.rewers_image, (pole_x[i] + pole_width + spacing, pole_y[i]))

            font = pygame.font.SysFont(None, 30)
            num = len(self.game.gracze[i].karty_na_rece)

            text_surf = font.render(f"Liczba kart: {num}", True, BLACK)
            text_rect = text_surf.get_rect(center=(pole_x[i] + pole_width + spacing + card_width // 2, pole_y[i] + card_height + 20))
            self.screen.blit(text_surf, text_rect)

            text_surf = font.render(self.game.gracze[i].nick, True, BLACK)
            text_rect = text_surf.get_rect(center=(pole_x[i] + (pole_width + spacing + card_width) // 2, pole_y[i] - 40))
            self.screen.blit(text_surf, text_rect)

       
