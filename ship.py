import pygame

class Ship():
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # загрузка изображения коробля
        self.image = pygame.image.load("images/ship.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        # настройка управления кораблем
        self.moving_right = False

    def update(self):
        if self.moving_right:
            self.rect.x += 1

# отмечает корабль в позиции
    def blitime(self):
        self.screen.blit(self.image, self.rect)

