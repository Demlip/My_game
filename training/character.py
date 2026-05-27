import sys, pygame

class Character:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Only character")
        self.screen = pygame.display.set_mode((1000,578))
        self.bg_color = (0,230,230)
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load("character/cucumber.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            
            self.screen.fill(self.bg_color)
            self.screen.blit(self.image, self.rect)
            pygame.display.flip()

if __name__ == "__main__":
    ch = Character()
    ch.run()
