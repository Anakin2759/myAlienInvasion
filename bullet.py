import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """子弹类"""
    def __init__(self,ai_settings,screen,ship):
        """在飞船处创建子弹"""
        super(Bullet,self).__init__()
        self.screen = screen

        #在(0,0)处创建矩形，再设置位置
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #存储小数保存的子弹位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    
    def update(self):
        """向上移动子弹"""
        #更新子弹位置数值
        self.y -= self.speed_factor
        #更新表示子弹的rect的位置
        self.rect.y=self.y

    def draw_bullet(self):
        """绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)
