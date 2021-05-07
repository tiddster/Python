import sys
import pygame
from settings import Setting
from bullet import Bullet
from ship import Ship

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Setting()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
    
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self._updata_screen()
            self.ship.update()
            self.bullets.update()


    def _check_events(self):
        '''键盘、鼠标响应事件'''
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()                           #退出程序

                #飞船移动事件
                elif event.type == pygame.KEYDOWN:           #键盘摁下的时候
                    self._check_keydown_events(event)

                elif event.type == pygame.KEYUP:              #键盘初始状态的时候
                   self._check_keyup_events(event)


    def _updata_screen(self):
        self.screen.fill(self.settings.bg_color)       #每次循环时都会绘制屏幕
        self.ship.blitme()
        for bullet in self.bullets.sprites():         #绘制子弹
            bullet.draw_bullet()
        pygame.display.flip()          #让最近绘制的屏幕可见
    
    def _check_keyup_events(self,event):             #键盘初始状态的时候
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _check_keydown_events(self,event):            #键盘摁下的时候
        if event.key == pygame.K_RIGHT:               #摁左箭头向右走
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:              #摁左箭头向左走
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE:                 #按esc退出
            sys.exit()
        elif event.key == pygame.K_SPACE:              #摁空格发射子弹
            self._fire_bullet()


    def _fire_bullet(self):                             #创建子弹
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

