import sys
import pygame

def check_events():
    # listen for key or mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(screen, ai_settings, ship):
    """Update screen state and display new screen"""
    # refresh screen while looping
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # display new screen
    pygame.display.flip()
