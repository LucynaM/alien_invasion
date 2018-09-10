import sys
import pygame
from settings import Settings

def run_game():
    # launch game and create 'screen' object
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # define background screen color instead of default black one
    bg_color = (230, 230, 230)

    # start main loop of the game
    while True:

        # listen for key or mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # refresh screen while looping
        screen.fill(ai_settings.bg_color)

        # display last modified screen
        pygame.display.flip()

run_game()
