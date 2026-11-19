import sys, pygame

class Blue_Sky:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 500))
        self.bg_color = (0,0,230)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            pygame.display.flip()

if __name__ == "__main__":
    bl = Blue_Sky()
    bl.run()
