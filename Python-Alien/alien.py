import pygame
import random
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        #加载外星人图像设置rect值
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #外星人出现高度确定，但是左右位置不确定
        self.rect.x = random.randint(0 + self.rect.width,self.screen.get_rect().width - self.rect.width)
        self.rect.y = self.rect.height

        #储存每一个外星人精确的位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.alien_speed
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
        self.rect.y = self.y

    def check_edge(self):             #检查触碰边缘
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= screen_rect.left:
            return True