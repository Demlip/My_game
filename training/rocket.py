import sys, pygame

class Rocket:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("rocket in map")
        self.screen = pygame.display.set_mode((1000,578))
        self.bg_color = (0,22,111)
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load("character/cucumber.jpeg")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def location(self):
        if self.moving_right and self.rect.right < self.screen.right:
            self.rect.x += 1

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            
            self.screen.fill(self.bg_color)
            self.screen.blit(self.image, self.rect)
            pygame.display.flip()

    
    def keydown(self, event):
        if event.key == pygame.K_RIGHT:
            self.moving_right = True
        if event.key == pygame.K_LEFT:
            self.moving_left = True
        if event.key == pygame.K_UP:
            self.moving_up = True
        if event.key == pygame.K_DOWN:
            self.moving_down = True


if __name__ == "__main__":
    ch = Rocket()
    ch.run()
