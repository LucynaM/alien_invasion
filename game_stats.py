class GameStats():
    """Follow game statistics"""

    def __init__(self, ai_settings):
        """Initialize statistics """
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start game in an active state
        self.game_active = False

        # High score should never be reset
        self.high_score = self.high_score_read()



    def reset_stats(self):
        """Initialize statistics which may change during the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1


    def high_score_read(self):
        try:
            with open('best_score_ever.txt') as file_object:
                return int(file_object.read())
        except FileNotFoundError:
            return 0


    def high_score_write(self):
        with open('best_score_ever.txt', 'w') as file_object:
            file_object.write(str(self.high_score))


