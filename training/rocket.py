import sys, pygame

class Rocket:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("rocket in map")
        self.screen = pygame.display.set_mode((1000,578))
        self.bg_color = (0,22,111)
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load("character/favicon-32x32.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.location()

    # разметка границы
    def location(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 1
        elif self.moving_left and self.rect.left > 0:
            self.rect.x -= 1
        elif self.moving_up and self.rect.top > 0:
            self.rect.y -= 1
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 1
       
    # нажатие клавиши     
    def _check_keydown(self, event):
        if event.key == pygame.K_RIGHT:
            self.moving_right= True
        elif event.key == pygame.K_LEFT:
            self.moving_left= True
        elif event.key == pygame.K_UP:
            self.moving_up= True
        elif event.key == pygame.K_DOWN:
            self.moving_down= True

    # отпуск для зажатия
    def _check_keyup(self, event):
        if event.key == pygame.K_RIGHT:
            self.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.moving_left= False
        elif event.key == pygame.K_UP:
            self.moving_up= False
        elif event.key == pygame.K_DOWN:
            self.moving_down= False

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup(event)
                    

            self.location()
            self.screen.fill(self.bg_color)
            self.screen.blit(self.image, self.rect)
            pygame.display.flip()

if __name__ == "__main__":
    ch = Rocket()
    ch.run()
