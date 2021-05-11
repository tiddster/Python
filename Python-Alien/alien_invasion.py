import sys
import pygame
from time import sleep

from settings import Setting
from bullet import Bullet
from ship import Ship
from GameState import GameStates
from alien import Alien
from button import Button

from ScoreBoard import Scoreboard


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

        #创建一个用于储存游戏统计信息的实例
        self.stats = GameStates(self)

        self.stats.game_activity = False

        self.play_button = Button(self,"Play")

        self.sb = Scoreboard(self)
    
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self._update_screen()
            
            if self.stats.game_activity:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                self._create_fleet()
            
            if self.stats.killed_number >= self.settings.aim:              #当达到目标的时候的事件
                sleep(1)
                self.settings.speed_up += 0.2                              #速度+0.2
                self.settings.difficulty(self.settings.speed_up)           #赋予新的难度

                self.stats.killed_number = 0                               #重置击杀次数
                self.stats.level += 1
                self.sb.prep_level()
                self.sb.show_level()

                self.aliens.empty()
                self.bullets.empty()
                self._create_fleet()

    def _check_events(self):
        '''键盘、鼠标响应事件'''
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()                           #退出程序

                elif event.type == pygame.MOUSEBUTTONDOWN:       #监听鼠标
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)

                #飞船移动事件
                elif event.type == pygame.KEYDOWN:           #键盘摁下的时候
                    self._check_keydown_events(event)

                elif event.type == pygame.KEYUP:              #键盘初始状态的时候
                   self._check_keyup_events(event)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)       #每次循环时都会绘制屏幕

        self.ship.blitme()

        self.sb.prep_and_show()

        for bullet in self.bullets.sprites():         #绘制子弹
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            bullet.draw_bullet()
        
        for alien in self.aliens.sprites():           #绘制外星人
            if alien.rect.bottom >= self.screen.get_rect().height + 120:              #外星人到屏幕外面时执行的事件
                self._ship_hit()
                self.aliens.remove(alien)
            self.aliens.draw(self.screen)

        if not self.stats.game_activity:                  #当游戏状态不活跃时，显示按钮
            self.play_button.draw_button()
            
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
        elif event.key == pygame.K_p:
            self.start_game()

    def _fire_bullet(self):                             #创建子弹
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):                          #子弹状态(包含子弹击中外星人事件)
        self.bullets.update()
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        if collisions:
            self.stats.killed_number += 1
            self.stats.score += 1
            self.sb.checK_high_score()

    def _create_fleet(self):                            #创建外星人
        if len(self.aliens) < self.settings.alien_allowed:
            alien = Alien(self)
            self.aliens.add(alien)
    
    def _update_aliens(self):                            #更新外星人状态
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
        
    def _check_fleet_edges(self):                            #检测是否在边缘
        for alien in self.aliens.sprites():
            if alien.check_edge():
                self.settings.fleet_direction *= -1
                break

    def _ship_hit(self):
        self.stats.ships_left -= 1
        self.sb.prep_lives()

        if self.stats.ships_left > 0:
            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.center_ship()
            sleep(1)
        else:
            self.stats.game_activity = False
            pygame.mouse.set_visible(True)                        #显示鼠标光标
            sleep(1)

    def _check_play_button(self,mouse_pos): 
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)            #判断鼠标是否点击play
        if button_clicked and not self.stats.game_activity:          #当鼠标点击按钮时，游戏便活跃
            self.start_game()

    def start_game(self):
        self.settings.speed_up = 1
        self.settings.difficulty(self.settings.speed_up)            #重置难度

        self.stats.game_activity = True                         #游戏活跃
        self.stats.reset_stats()

        self.aliens.empty()
        self.bullets.empty()

        self._create_fleet()
        self.ship.center_ship()

        pygame.mouse.set_visible(False)   

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()