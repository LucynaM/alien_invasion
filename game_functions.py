import sys
import pygame


def check_keydown_keyup_events(event, ship, bool_value):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = bool_value
    elif event.key == pygame.K_LEFT:
        ship.moving_left = bool_value


def check_events(ship):
    # listen for key or mouse events
    for event in pygame.event.get():
        # exit
        if event.type == pygame.QUIT:
            sys.exit()
        # keydown event
        elif event.type == pygame.KEYDOWN:
            check_keydown_keyup_events(event, ship, True)
        # keyup event
        elif event.type == pygame.KEYUP:
            check_keydown_keyup_events(event, ship, False)



def update_screen(screen, ai_settings, ship):
    """Update screen state and display new screen"""
    # refresh screen while looping
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # display new screen
    pygame.display.flip()
