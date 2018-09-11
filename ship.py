import pygame

class Ship():
    def __init__(self, screen):
        """Set up spaceship and its start position"""
        self.screen = screen

        # load spaceship image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # every new ship appears at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Display the ship at its current position"""
        self.screen.blit(self.image, self.rect)