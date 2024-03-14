class Settings():
    """Класс для хранения всех настроек игры"""
    def __init__(self):
        """Инициализирует постоянные настройки"""
        """Параметры экрана"""
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (255, 255, 255)
        """Sip`s settings"""
        self.ship_limit = 2
        """Параметры пули"""
        self.bullet_width = 3000
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3
        """Alien`s settings"""
        self.fleet_drop_speed = 10
        #Темп ускорения игры
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1  # fleet_direction = 1 it`s meaning right moving, -1 -- left
        #Подсчет очков
        self.alien_points = 50

    def increase_speed(self):
        """Upp game`s speed """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
