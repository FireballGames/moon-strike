import pygame
from game_utils.game import Game
from .resource import Resource
from .sprites import lasers
from .sprites.background import Background
from .sprites.main_field import MainField
from .sprites.texts import LevelText, LivesText, LostText


class MoonStrike(Game):
    KEY_LEFT = pygame.K_LEFT
    KEY_RIGHT = pygame.K_RIGHT
    KEY_UP = pygame.K_UP
    KEY_DOWN = pygame.K_DOWN

    KEY_EXIT = pygame.K_ESCAPE
    KEY_FIRE = pygame.K_SPACE

    def __init__(self, size=(800, 600), title="Game", fps=60):
        super().__init__(size=size, title=title, fps=fps)

        self.resource = None
        self.background = Background()
        self.main_field = MainField()

        self.spaceship = self.main_field.spaceship

        self.level_label = LevelText()
        self.lives_label = LivesText()
        self.lost_label = LostText()

        self.load()
        self.draw_bg()

        self.__lost_count = 0

    def load(self):
        self.resource = Resource()
        self.background.load(self.resource)
        self.main_field.load(self.resource)

    def draw_bg(self):
        self.background.draw(self.window)
        pygame.display.flip()

    @property
    def movement_keys(self):
        yield self.KEY_LEFT
        yield self.KEY_RIGHT
        yield self.KEY_UP
        yield self.KEY_DOWN

    def on_exit(self):
        self.quit()

    def on_move(self, direction):
        if direction == self.KEY_LEFT:
            self.spaceship.move(-1, 0)
        if direction == self.KEY_RIGHT:
            self.spaceship.move(1, 0)
        if direction == self.KEY_UP:
            self.spaceship.move(0, -1)
        if direction == self.KEY_DOWN:
            self.spaceship.move(0, 1)

    def on_fire(self):
        pass

    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == self.KEY_EXIT:
                self.on_exit()
            if event.key == self.KEY_FIRE:
                self.on_fire()

        super().process_event(event)

    def update(self):
        keys = pygame.key.get_pressed()

        for k in self.movement_keys:
            if keys[k]:
                self.on_move(k)

        if keys[self.KEY_FIRE]:
            self.on_fire()

        self.background.update()
        self.main_field.update()

        self.lives_label.update(self.spaceship.lives)
        self.level_label.update(self.main_field.level)
        self.lost_label.update()

        self.level_label.rect.topright = (self.window.get_width() - 10, 10)
        self.lost_label.rect.centerx = int(self.window.get_width() / 2)

    def draw(self):
        self.main_field.draw(self.window)
        pygame.display.update(self.main_field.rect)

        self.window.blit(self.lives_label.image, self.lives_label.rect)
        pygame.display.update(self.lives_label.rect)

        self.window.blit(self.level_label.image, self.level_label.rect)
        pygame.display.update(self.level_label.rect)

        if self.spaceship.lost:
            self.__lost_count += 1
            self.window.blit(self.lost_label.image, self.lost_label.rect)
            pygame.display.update(self.lost_label.rect)

            if self.__lost_count > self.fps * 3:
                self.playing = False
