class GameStates:
    def __init__(self,ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

        self.game_activity = True

        self.high_score = 0

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.killed_number = 0
        self.score = 0
        self.level = 1
        