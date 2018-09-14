class GameStats():
    """Follow game statistics"""

    def __init__(self, ai_settings):
        """Initialize statistics """
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start game in an active state.
        self.game_active = False


    def reset_stats(self):
        """Initialize statistics which may change during the game"""
        self.ships_left = self.ai_settings.ship_limit
