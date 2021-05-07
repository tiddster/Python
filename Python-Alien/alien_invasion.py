import sys
import pygame
from settings import Setting
from ship import Ship

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Setting()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
    
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self._updata_screen()


    def _check_events(self):
        '''键盘、鼠标响应事件'''
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _updata_screen(self):
        self.screen.fill(self.settings.bg_color)       #每次循环时都会绘制屏幕
        self.ship.blitme()
        pygame.display.flip()          #让最近绘制的屏幕可见


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

