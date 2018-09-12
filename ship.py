import pygame

class Ship():
    def __init__(self, screen, ai_settings):
        """Set up spaceship and its start position"""
        self.screen = screen
        self.ai_settings = ai_settings

        # load spaceship image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # set up the default position of the ship - at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # center point of the ship as a float number
        self.center = float(self.rect.centerx)

        # constant movement of the ship
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the position of the ship according to movement parameter value"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Update rect object according to self.center value
        self.rect.centerx = self.center

    def blitme(self):
        """Display the ship at its current position"""
        self.screen.blit(self.image, self.rect)