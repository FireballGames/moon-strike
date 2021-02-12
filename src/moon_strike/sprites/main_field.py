import os
import pygame
import config
from game_utils.image_sprite import ImageSprite
from .spaceship import Spaceship


class Border(ImageSprite):
    IMAGE_PATH = os.path.join(config.PATH, 'main_field.png')


class MainField(pygame.sprite.Sprite):
    TOP = config.FIELD_TOP
    LEFT = config.FIELD_LEFT
    WIDTH = config.FIELD_WIDTH + 2 * config.FIELD_OFFSET_X
    HEIGHT = config.FIELD_HEIGHT + 2 * config.FIELD_OFFSET_Y
    COLOR = config.FIELD_BACKGROUND_COLOR
    OUTER = pygame.Rect(
        config.FIELD_LEFT,
        config.FIELD_TOP,
        config.FIELD_WIDTH + 2 * config.FIELD_OFFSET_X,
        config.FIELD_HEIGHT + 2 * config.FIELD_OFFSET_Y,
    )
    SCOPE = pygame.Rect(
        config.FIELD_OFFSET_X,
        config.FIELD_OFFSET_Y,
        config.FIELD_WIDTH,
        config.FIELD_HEIGHT,
    )

    def __init__(self, *groups):
        super().__init__(*groups)

        self.rect = pygame.Rect(self.OUTER)
        self.image = pygame.Surface(self.rect.size)

        self.group = pygame.sprite.Group()

        self.spaceship = Spaceship((config.PLAYER_LEFT, config.PLAYER_TOP), self.group)
        self.border = Border(self.group)

    def load(self):
        self.border.load()
        self.spaceship.load()

    def check_rect(self, new_rect, bounce):
        if new_rect.left <= self.SCOPE.left:
            new_rect.left = self.SCOPE.left + bounce
        if new_rect.right >= self.SCOPE.right:
            new_rect.right = self.SCOPE.right - bounce
        if new_rect.top <= self.SCOPE.top:
            new_rect.top = self.SCOPE.top + bounce
        if new_rect.bottom >= self.SCOPE.bottom:
            new_rect.bottom = self.SCOPE.bottom - bounce
        return new_rect

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)

        self.spaceship.rect = self.check_rect(
            self.spaceship.get_new_rect(),
            self.spaceship.bounce,
        )
        self.group.update(*args, **kwargs)

    def draw(self, surface):
        self.image.fill(self.COLOR)
        self.group.draw(self.image)
        surface.blit(self.image, self.rect)
