import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """manage bullets shot by ship"""

    def __init__(self, ai_settings, screen, ship):
        """Create bullet object at the current ship position"""
        super().__init__()
        self.screen = screen

        # create rect of bullet, firstly at point (0,0), than at the ship position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Bullet position as float number
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move bullet on the screen"""
        #update of bullet position
        self.y -= self.speed_factor
        #update of bullet rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Display bullet"""
        pygame.draw.rect(self.screen, self.color, self.rect)

