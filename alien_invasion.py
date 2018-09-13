import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # launch game and create 'screen' object
    pygame.init()

    # screen settings
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # spaceship as an instance of Ship class
    ship = Ship(screen, ai_settings)
    # create group containing all bullets and all aliens as instances of sprite.Group
    bullets = Group()
    aliens = Group()


    # create alien fleet
    gf.create_fleet(ai_settings, screen, aliens)


    # main loop of the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
