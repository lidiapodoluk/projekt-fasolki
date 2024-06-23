import pygame
from scene_manager import *

class MenuScene(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.left_image = pygame.image.load('/home/lidia/Pulpit/projekt/projekt-fasolki/img/menu.jpg')
        self.left_image = pygame.transform.scale(self.left_image, (SCREEN_HEIGHT, SCREEN_HEIGHT))
        self.button_width = 200
        self.button_height = 60
        self.start_button_rect = pygame.Rect(
            (SCREEN_WIDTH - (SCREEN_WIDTH - SCREEN_HEIGHT) // 2) - self.button_width // 2,
            SCREEN_HEIGHT // 2,
            self.button_width,
            self.button_height
        )

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if self.start_button_rect.collidepoint(mouse_x, mouse_y):
                    return "game"
        return None

    def update(self):
        pass

    def draw(self):
        self.screen.fill(WHITE)
        self.screen.blit(self.left_image, (0, 0))

        # Rysowanie napisu "Fasolki"
        font = pygame.font.SysFont(None, 100)
        title_surf = font.render("Fasolki", True, RED)
        title_rect = title_surf.get_rect(center=(SCREEN_WIDTH - (SCREEN_WIDTH - SCREEN_HEIGHT) // 2, SCREEN_HEIGHT // 3))
        self.screen.blit(title_surf, title_rect)

        # Rysowanie przycisku "START"
        self.draw_button("START", self.start_button_rect.x, self.start_button_rect.y, self.start_button_rect.width, self.start_button_rect.height)

    def draw_button(self, text, x, y, width, height):
        pygame.draw.rect(self.screen, LIGHT_BLUE, (x, y, width, height), border_radius=10)
        pygame.draw.rect(self.screen, BLACK, (x, y, width, height), 2, border_radius=10)

        font = pygame.font.SysFont(None, 40)
        text_surf = font.render(text, True, RED)
        text_rect = text_surf.get_rect(center=(x + width // 2, y + height // 2))
        self.screen.blit(text_surf, text_rect)
