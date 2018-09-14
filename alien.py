import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """single alien of the fleet"""
    def __init__(self, ai_settings, screen):
        """Initialize an alien and define its default position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Load alien image and define its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #place an alien near upper left screen corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #alien position as float number
        self.x = float(self.rect.x)


    def check_edges(self):
        """Return True when alien gets the edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True


    def update(self):
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """Display an alien in its current position"""
        self.screen.blit(self.image, self.rect)
