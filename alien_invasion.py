import pygame
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

    # main loop of the game
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(screen, ai_settings, ship)

run_game()
