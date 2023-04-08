
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建飞船
    ship = Ship(ai_settings,screen)

    #创建一个子弹编组
    bullets = Group()

    #开始游戏主循环
    while True:
        #获取键盘事件
        gf.check_events(ai_settings,screen,ship,bullets)
        #更新飞船状态
        ship.update()
        #更新子弹状态
        gf.update_bullets(bullets)
        #重新绘制画面
        gf.update_screen(ai_settings,screen,ship,bullets)
        

run_game()
