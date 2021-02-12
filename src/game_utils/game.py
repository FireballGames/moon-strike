import pygame
import sys


class Game:
    def __init__(self, size=(800, 600), title="Game"):
        pygame.init()

        self.window = pygame.display.set_mode(size)
        pygame.display.set_caption(title)

        self.clock = pygame.time.Clock()
        self.playing = True

    def quit(self):
        self.playing = False

        pygame.quit()
        sys.exit()

    def process_event(self, event):
        if event.type == pygame.QUIT:
            self.quit()

    def update(self):
        pass

    def draw(self):
        pygame.display.flip()

    def __call__(self, *args, **kwargs):
        while self.playing:
            for event in pygame.event.get():
                self.process_event(event)
            self.update()
            self.draw()
