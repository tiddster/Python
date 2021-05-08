class Setting:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        self.bullet_speed = 2.0
        self.bullet_width = 5
        self.bullet_allowed = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)

        self.alien_allowed = 3
        self.alien_speed = 0.2
    
        self.fleet_direction = 1             #方向： -1左   1右

        self.ship_speed = 1.5
        self.ship_limit = 3
