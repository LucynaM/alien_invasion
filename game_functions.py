import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


# bullet functionalities
def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet, if limit not reached yet."""
    # Create a new bullet, add to bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

# alien functionalities
def get_number_rows(ai_settings, ship_height, alien_height):
    """Find max alien rows"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def get_number_aliens(ai_settings, alien_width):
    # find max aliens number in a row
    # distance between 2 aliens equals one alien width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + (2 * alien.rect.height * row_number)
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """Create alien fleet"""
    #create an alien and find max aliens number in a row
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # first alien row
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """React when finding screen edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Move fleet down and change direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


# start game options
def start_game(ai_settings, screen, stats, sb, ship, aliens, bullets):
    #reset game settings
    ai_settings.initialize_dynamic_settings()

    #hide mouse cursor
    pygame.mouse.set_visible(False)

    # Reset game statistics
    stats.reset_stats()
    stats.game_active = True

    # Reset scoreboard information
    sb.prep_images()

    #remove content of aliens and bullets groups
    aliens.empty()
    bullets.empty()

    #create new fleet and center ship position
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()


# play_button functionalities
def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """launch new game after clicking 'play' button"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        start_game(ai_settings, screen, stats, sb, ship, aliens, bullets)


#event functionalites
def check_keydown_events(event, ai_settings, screen, sb, ship, bullets, stats, aliens):
    """Respond to keydown presses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        stats.high_score_write()
        sys.exit()
    elif event.key == pygame.K_p:
        start_game(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    # listen for key or mouse events
    for event in pygame.event.get():
        # exit
        if event.type == pygame.QUIT:
            stats.high_score_write()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)
        # keydown event
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, sb, ship, bullets, stats, aliens)
        # keyup event
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_high_score(stats, sb):
    """Check to see if there's a new high score"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def start_new_level(ai_settings, stats, sb, screen, ship, aliens):
    """If the entire fleet is destroyed, start a new level"""
    #  increase speed
    ai_settings.increase_speed()
    #  start a new level
    stats.level += 1
    sb.prep_level()
    # create new alien fleet
    create_fleet(ai_settings, screen, ship, aliens)


# collision functions - start

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Respond to bullet-alien collisions"""
    # Remove any bullets and aliens that have collided.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # If the entire fleet is destroyed, get rid of existing bullets
        bullets.empty()
        start_new_level(ai_settings, stats, sb, screen, ship, aliens)


def ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets):
    """Respond to ship being hit by alien."""
    if stats.ships_left > 0:
        # decrease value kept in ships_left
        stats.ships_left -= 1

        # update scoreboard
        sb.prep_ships()

        # remove content of aliens and bullets groups
        aliens.empty()
        bullets.empty()

        # Create new fleet and center ship position
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Pause
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets):
    """Check if any alien reached bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)
            break

# collision functions - stop


# update functionalites - start

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Update bullets position and remove the out of screen ones"""

    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)


def update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets):
    """Check screen edges and update aliens position"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Detect collision between alien and ship
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)

    # Detect aliens that reach screen bottom
    check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets)


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """Update screen state and display new screen"""
    # refresh screen while looping
    screen.fill(ai_settings.bg_color)

    # redisplay all bullets above ship and alien layers
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    #disply fleet of aliens
    aliens.draw(screen)
    #display scoring information
    sb.show_score()

    #display button only if game is inactive
    if not stats.game_active:
        play_button.draw_button()


    #display new screen
    pygame.display.flip()

# update functionalites - stop