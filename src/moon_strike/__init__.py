import pygame
from game_utils.game import Game
from .resource import Resource
from .sprites.background import Background
from .sprites.spaceship import Spaceship
from .sprites.main_field import MainField


class MoonStrike(Game):
    def __init__(self, size=(800, 600), title="Game"):
        super().__init__(size=size, title=title)

        self.resource = None
        self.background = Background()
        self.main_field = MainField()

        self.spaceship = self.main_field.spaceship

        self.load()

    def load(self):
        self.resource = Resource()
        self.background.load(self.resource)
        self.main_field.load(self.resource)

    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.quit()
            if event.key == pygame.K_LEFT:
                self.spaceship.move(-1, None)
            if event.key == pygame.K_RIGHT:
                self.spaceship.move(1, None)
            if event.key == pygame.K_UP:
                self.spaceship.move(None, -1)
            if event.key == pygame.K_DOWN:
                self.spaceship.move(None, 1)
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                self.spaceship.move(0, None)
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                self.spaceship.move(None, 0)
        super().process_event(event)

    def update(self):
        self.background.update()
        self.main_field.update()

    def draw(self):
        self.background.draw(self.window)
        self.main_field.draw(self.window)
        super().draw()
