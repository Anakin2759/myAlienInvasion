import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image= pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #把新飞船放到屏幕中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #在飞船属性中心存储小数组
        self.center = float(self.rect.centerx)
        #移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整位置"""
        #更新飞船center值
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center +=self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left >0:
            self.center -=self.ai_settings.ship_speed_factor
        #根据self.centerx更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        """1"""
        self.screen.blit(self.image,self.rect)
    
   
 