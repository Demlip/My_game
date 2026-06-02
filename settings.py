#настройки экрана 

class Settings():
    def __init__(self):
        self.screen_width = 1100
        self.screen_height = 600
        self.bg_color = (230,230,230)
        # настройки корабля
        self.ship_speed = 1.5
        # добавление возможности стрельбы 
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3


