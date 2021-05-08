class Setting:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        self.speed_up = 1

        self.bullet_width = 5
        self.bullet_allowed = 3
        self.bullet_height = 4
        self.bullet_color = (60,60,60)

        self.alien_allowed = 3
    
        self.fleet_direction = 1             #方向： -1左   1右

        self.ship_limit = 3

        self.difficulty(self.speed_up)

    def difficulty(self,speed_up):
        self.alien_speed = 0.2*speed_up
        self.bullet_speed = 2.0/speed_up
        self.ship_speed = 1.5/speed_up
        self.aim = 10*speed_up

