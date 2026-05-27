import sys, pygame

class Character:
    def __init__(self):
        pygame.init()
        pygame.display.set_cuption("Only character")
        self.screen = pygame.display.set_mode(1000,578)
        self.bg_color = (0,230,230)
        self.screen_rect = screen.get_rect()


    def run(self):
        while True:
            for event in pygame.event.get()

