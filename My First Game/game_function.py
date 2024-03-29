import sys
import pygame
from time import sleep

from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, stats, ship, aliens, bullets):
    """Реагирует на нажатие клавиш"""
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE or event.key == pygame.K_w or event.key == pygame.K_UP:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_p:
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        stats.game_active = True


def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = False


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """Обрабатывает нажатия клавиши события мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, ship, aliens, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """It starts new game if Play is pushed"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        """Сброс игровых настроек"""
        ai_settings.initialize_dynamic_settings()
        """Указатель мыши скрывается"""
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True
        """Сброс изображения счетов и уровня"""
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """Обновляет изображения на экране и отображает новый"""
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()
    """"Отображение последнего прорисованного экрана"""
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Обновляет позиции пуль и уничтожает старые"""
    bullets.update()
    """Удаление пуль, вышедших за пределы экрана"""
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Проверка попаданий в пришельцев
        при обнаружении попадания удлить пулю и пришельца"""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
            check_high_score(stats, sb)
    if len(aliens) == 0:
        """Уничтожение существующих пуль и создание нового флота"""
        bullets.empty()
        ai_settings.increase_speed()
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, ship, aliens)


def get_number_aliens_x(ai_settings, alien_width):
    """Calculate count of alien in line"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x/(2 * alien_width))
    return number_alien_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """Calculate count of row placing on screen"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    numbers_rows = int(available_space_y / (2 * alien_height))
    return numbers_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create alien and place it in his line"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """Creating alien`s fleet
       Creating alien and calculating one`s number
       Interval between neighbour aliens is 1 width of alien
    """
    alien = Alien(ai_settings, screen)
    number_alien_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    """Creating new line of alien"""
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            """Creating alien and placement in line"""
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """Реагирует на достижение пришельцем края экрана"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Опускает флот вниз и меняет направление его движения"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets):
    """Обрабатывает столкновение с кораблем"""
    if stats.ship_left > 0:
        stats.ship_left -= 1
        """Updating game`s information"""
        sb.prep_ships()
        """Cleaning list of aliens and bullets"""
        aliens.empty()
        bullets.empty()
        """Creating new fleet and placing new ship in centre"""
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        """Pause"""
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets):
    """Проверяет добрались ли пришельцы до края экрана"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            """Происходит то же, что и при столкновении с кораблем"""
            ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)
            break


def update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets):
    """Проверяет, достиг ли флот края экрана после чего
    Update position all aliens in fleet"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    """Проверка коллизий Пришелец-корабль"""
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)
    """Проверка пришельцев, добравшихся до края экрана"""
    check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets)


def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

