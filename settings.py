class Settings():
    """Manage all game settings"""
    def __init__(self):
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_limit = 3

        # bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # speed of movement down after getting to right or left edge
        self.fleet_drop_speed = 10


        # change of game speed
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Initilize settings which may change during the game"""

        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # fleet_direction param 1 means right, -1 means left
        self.fleet_direction = 1

    def increase_speed(self):
        """Change speed settings"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

