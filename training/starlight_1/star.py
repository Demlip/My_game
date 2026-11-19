import sys, pygame, random
from element import Element

class Star:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		self.bg_color = (230, 0, 230)
		self.screen_width = self.screen.get_rect().width
		self.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("Random star")
		self.element = pygame.sprite.Group()
		self._element()


	def run(self):
		while True:
			self._check_events()
			self._screen_update()

	def _check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					sys.exit()
				elif event.key == pygame.K_q:
					sys.exit()
				elif event.key == pygame.K_r:
					pass

	def _screen_update(self):
		self.screen.fill(self.bg_color)
		self.element.draw(self.screen)
		pygame.display.flip()

	def _element(self):
		elmt = Element(self)
    	# elmt_width, elmt_height = elmt.rect.size
    	# alien.rect.x = alien.x 
    	# alien.rect.y = alien.y
		self.element.add()


if __name__ == "__main__":
	s = Star()
	s.run()