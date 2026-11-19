import pygame, sys
from settings import Settings
from element import Element

class StarLight():

	def __init__(self):
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("Starlight")
		self.stars = pygame.sprite.Group()
		self._create_fleet()

	def start(self):
		while True:
			for event in pygame.event.get():
			    if event.type == pygame.QUIT:
			        sys.exit()

			    if event.type == pygame.KEYDOWN:
			        if event.key == pygame.K_q:
			            sys.exit()
			self._framerate()
			self._create_fleet()
			

	def _framerate(self):
		self.screen.fill(self.settings.bg_color)
		self.stars.draw(self.screen)
		pygame.display.flip()
		

	def _create_fleet(self):
		star = Element(self)
		star_width, star_height = star.rect.size
		# self.stars.add(star)
		star = Element(self)
		star_width = star.rect.width
		available_space_x = self.settings.screen_width - (star_width)
		number_stars_x = available_space_x // (2 * star_width)
		available_space_y = (self.settings.screen_height - 
			(star_height))
		number_rows = available_space_y // (2 * star_width)
		#^
		for row_number in range(number_rows):
			for stars_number in range(number_stars_x):
				self._create_star(stars_number, row_number)


	def _create_star(self, stars_number, row_number):
		star = Element(self)
		star_width, star_height = star.rect.size

		star_width = star.rect.width
		star.x = star_width + 2 * star_width * stars_number
		star.rect.x = star.x
		star.rect.y = star.rect.height + 2 * star.rect.height * row_number
		self.stars.add(star)


if __name__ == "__main__":
	s = StarLight()
	s.start()
