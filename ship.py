import pygame

class Ship():
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # загрузка изображения коробля
        self.image = pygame.image.load("images/ship.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

        # настройка управления кораблем
        self.moving_right = False
        self.moving_left = False


    def update(self):
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

# отмечает корабль в позиции
    def blitime(self):
        self.screen.blit(self.image, self.rect)

