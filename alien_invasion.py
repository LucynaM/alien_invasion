import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
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
    # statistics of the game
    stats = GameStats(ai_settings)
    # play button
    play_button = Button(ai_settings, screen, "Play")


    # create alien fleet
    gf.create_fleet(ai_settings, screen, ship, aliens)


    # main loop of the game
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)

run_game()
