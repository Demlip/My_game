import pygame 

class Ship():
	def __init__(self, xyelet):
		self.screen = xyelet.screen
		self.screen_rect = xyelet.screen.get_rect()
		self.settings = xyelet.settings

		self.image = pygame.image.load("maket/persona.png")
		self.rect = self.image.get_rect()
		self.rect.midbottom = self.screen_rect.midbottom
		
		# настройк направлений объекта
		self.moving_up = False
		self.moving_down = False
		self.moving_right = False
		self.moving_left = False


# ПРОВЕРИТЬ МОЖНО ЛИ ИСПОЛЬЗОВАТЬ ГРАНИЦЫ А НЕ 0
	def update(self):
	    if self.moving_right and self.rect.right < self.screen_rect.right:
	        self.rect.x += 1
	    elif self.moving_left and self.rect.left > 0:
	        self.rect.x -= 1
	    elif self.moving_up and self.rect.top > 0:
	        self.rect.y -= 1
	    elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
	        self.rect.y += 1

	def blitime(self):
		self.screen.blit(self.image, self.rect)

