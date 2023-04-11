import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """外星人"""
    def __init__(self, ai_settings, screen):
        """初始化外星飞船的起始位置"""
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        #加载外星飞船
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #外星人最初在左上
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image,self.rect) 
    
   
    
    def check_edges(self):
        """如果怪在边缘为真"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left<=0:
            return True

    def update(self):
        self.x += (self.ai_settings.alien_speed_factor  *
                     self.ai_settings.fleet_direction)
        self.rect.x =self.x

  