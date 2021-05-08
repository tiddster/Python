import sys
import pygame
from settings import Setting
from bullet import Bullet
from ship import Ship
from alien import Alien

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
        self.aliens = pygame.sprite.Group()
    
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._create_fleet()


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

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)       #每次循环时都会绘制屏幕

        self.ship.blitme()
        for bullet in self.bullets.sprites():         #绘制子弹
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            bullet.draw_bullet()
        
        for alien in self.aliens.sprites():           #绘制外星人
            if alien.rect.bottom >= self.screen.get_rect().height + 120:
                self.aliens.remove(alien)
            self.aliens.draw(self.screen)
            
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
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)

    def _create_fleet(self):                            #创建外星人
        if len(self.aliens) < self.settings.alien_allowed:
            alien = Alien(self)
            self.aliens.add(alien)
    
    def _update_aliens(self):                            #更新外星人状态
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            print("ship hit!!")
        
    def _check_fleet_edges(self):                            #检测是否在边缘
        for alien in self.aliens.sprites():
            if alien.check_edge():
                self.settings.fleet_direction *= -1
                break


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()