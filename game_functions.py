import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """React keydown event"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
    # create new bullet and add it to bullets group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def get_number_aliens(ai_settings, alien_width):
    # find max aliens number in a row
    # distance between 2 aliens equals one alien width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)


def create_fleet(ai_settings, screen, aliens):
    """Create alien fleet"""
    #create an alien and find max aliens number in a row
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens(ai_settings, alien.rect.width)

    # first alien row
    for alien_number in range(number_aliens_x):
        create_alien(ai_settings, screen, aliens, alien_number)


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


def update_bullets(bullets):
    """Update bullets position and remove the out of screen ones"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Update screen state and display new screen"""
    # refresh screen while looping
    screen.fill(ai_settings.bg_color)

    # redisplay all bullets under ship and alien layers
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)
    # display new screen
    pygame.display.flip()
