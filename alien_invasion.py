import sys
import pygame

def run_game():
    # launch game and create 'screen' object
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
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
        screen.fill(bg_color)

        # display last modified screen
        pygame.display.flip()

run_game()
