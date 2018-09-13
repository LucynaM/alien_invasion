import sys
import pygame
from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #create new bullet and add it to bullets group
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    # listen for key or mouse events
    for event in pygame.event.get():
        # exit
        if event.type == pygame.QUIT:
            sys.exit()
        # keydown event
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        # keyup event
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)



def update_screen(ai_settings, screen, ship, bullets):
    """Update screen state and display new screen"""
    # refresh screen while looping
    screen.fill(ai_settings.bg_color)

    # redisplay all bullets under ship and alien layers
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    # display new screen
    pygame.display.flip()
