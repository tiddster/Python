import pygame

class Ship:
    def __init__(self,ai_game):
        '''初始化飞船并设置其初始位置'''
        self.screen = ai_game.screen        
        self.settings = ai_game.settings

        self.screen_rect = ai_game.screen.get_rect()                 #访问屏幕属性

        #加载飞船都图像，并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')        #加载飞船图像，返回一个surface
        self.rect = self.image.get_rect()                        #获取相应surface

        #对于每一艘飞船，都将其放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom

        #在飞船的属性x中储存小数值  
        self.x = float(self.rect.x)

        #移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)