import sys, pygame 
from settings import Settings
from ship import Ship
from bullet import Bullet


class Side_Ship():
	def __init__(self):
		pygame.init()
		pygame.display.set_caption("side rocket")
		self.settings = Settings()
		self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		self.ship = Ship(self)
		self.bullet = pygame.sprite.Group()

	def run(self):
		while True	:
			self.dvij()
			self.ship.update()
			self.bullet.update()
			self._update_bullets()
			self._update_screen()


	def dvij(self):
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				self._keydown(event)
			elif event.type == pygame.KEYUP:
				self._keyup(event)

	def _keydown(self, event):
		if event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_UP:
			self.ship.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_e:
			self._fire_bullet()

	def _keyup(self, event):
		if event.key == pygame.K_UP:
			self.ship.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False
		elif event.key == pygame.K_RIGHT:
			self.ship.moving_right = False

	def _fire_bullet(self):
		if len(self.bullet) < self.settings.bullet_allowed:
			new_bullet = Bullet(self)
			self.bullet.add(new_bullet)

	def _update_bullets(self):
		for bullet in self.bullet.copy():
			if bullet.rect.right >= self.ship.screen_rect.right:
				self.bullet.remove(bullet)

	def _update_screen(self):
		self.screen.fill(self.settings.bg_color)
		for bull in self.bullet.sprites():
			bull.draw_bullet()
		self.ship.blitime()
		pygame.display.flip()

if __name__ == "__main__":
	ss = Side_Ship()
	ss.run()