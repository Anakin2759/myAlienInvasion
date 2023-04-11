import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """获取按下键事件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets )
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event,ship):
    """获取松开键事件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, aliens, bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    screen.fill(ai_settings.bg_color)
    #在飞船和外星人后绘制子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    #打印屏幕
    pygame.display.flip()
    
def update_bullets(aliens,bullets):
    """更新子弹位置，删除无用子弹"""
    #更新子弹位置
    bullets.update()
    #删除子弹
    for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
    collosions = pygame.sprite.groupcollide(bullets,aliens,True,True)

def fire_bullet(ai_settings,screen,ship ,bullets):
    """如果没受限就发射"""
    #创建新子弹
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)


def get_number_rows(ai_settings,ship_height, alien_height):
    """计算屏幕上最多几排怪"""
    alien_yspace = (ai_settings.screen_height -
                     3*alien_height-ship_height)
    
    number_rows = int(alien_yspace/(2*alien_height))
    return number_rows

def get_number_aliens_x(ai_settings, alien_width):
    alien_xspace=ai_settings.screen_width - 2 * alien_width
    alien_maxNum=int(alien_xspace/(2 * alien_width ))
    return alien_maxNum

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    
    #创建一个怪在某一行
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width *alien_number
    alien.rect.x=alien.x
    alien.rect.y=alien.rect.height + 2*alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """怪群"""
    #创建一个怪，计算一行最多几个怪
    alien = Alien(ai_settings,screen)
    alien_maxNum = get_number_aliens_x(ai_settings, alien.rect.width)
    alien_rowNum = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    alien.rect.x = alien.x
    aliens.add(alien)

    #创建怪群
    for row_number in range(alien_rowNum):
        for alien_number in range(alien_maxNum):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """将整群下移"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, aliens):
    """更新所有怪位置"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()


    
