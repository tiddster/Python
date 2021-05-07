import pygame
class Ship:
    def __init__(self,ai_game):
        '''初始化飞船并设置其初始位置'''
        self.screen = ai_game.screen                        
        self.screen_rect = ai_game.screen.get_rect()                 #访问屏幕属性

        #加载飞船都图像，并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')        #加载飞船图像，返回一个surface
        self.rect = self.image.get_rect()                        #获取相应surface

        #对于每一艘飞船，都将其放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)