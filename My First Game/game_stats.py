class GameStats():
    """Отслеживание статы игры"""
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        """Game starts in not active status"""
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        """Инициализирует стату, изменяющуюся во время игры"""
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
