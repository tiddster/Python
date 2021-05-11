import pygame.font

from pygame.sprite import Group

from ship import Ship

class Scoreboard:

    def __init__(self,ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)

        self.prep_score()
        self.prep_high_score()

        self.prep_and_show()
    
    def prep_score(self):
        score_str = "Current: " + str(self.stats.score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right= self.screen_rect.right - 20
        self.score_rect.top = 50
    
    def prep_high_score(self):
        high_score = "Highest: " + str(self.stats.high_score)
        self.high_score_image = self.font.render(high_score,True,self.text_color,self.settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right= self.screen_rect.right - 20
        self.high_score_rect.top = 10
    
    def prep_level(self):
        level = "Level: " + str(self.stats.level)
        self.level_image = self.font.render(level,True,self.text_color,self.settings.bg_color)
        
        self.level_rect = self.level_image.get_rect()
        self.level_rect.center = self.screen_rect.center
        self.level_rect.top = 20

    def prep_lives(self):
        self.ships = Group()

        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number*ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
    
    def show_high_score(self):
        self.screen.blit(self.high_score_image,self.high_score_rect)
    
    def show_level(self):
        self.screen.blit(self.level_image,self.level_rect)

    def show_lives(self):
        self.ships.draw(self.screen)

    def checK_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_and_show(self):
        self.prep_score()
        self.show_score()

        self.prep_high_score()
        self.show_high_score()

        self.prep_level()
        self.show_level()

        self.prep_lives()
        self.show_lives()