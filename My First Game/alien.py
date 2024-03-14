import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Класс представлюяющий одного пришельца"""
    def __init__(self, ai_settings, screen):
        """Инициализирует 1ого пришельца и задает его начальную позицию"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        """Загрузка изображения пришельца и назначение атрибута rect"""
        self.image = pygame.image.load('images/ship_2.bmp')
        self.rect = self.image.get_rect()
        """Каждый пришелец появляется в верхнем левом углу"""
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        """Сохранение точной позиции пришельца"""
        self.x = float(self.rect.x)

    def blitme(self):
        """Выводит пришельца в текущем положении"""
        self.screen.blit(self.image, self.rect)


    def check_edges(self):
        """Return True if alien have gone the end of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move alien left or right"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
