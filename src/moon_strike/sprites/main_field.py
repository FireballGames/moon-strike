import pygame
import random
import config
from game_utils.image_sprite import ImageSprite
from .land import Land
from .spaceship import PlayerSpaceship, EnemySpaceship, RedSpaceship


class Border(ImageSprite):
    def get_image(self, resource):
        return resource.main_field


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
        config.FIELD_OFFSET_Y + 6 * 8,
        config.FIELD_WIDTH,
        config.FIELD_HEIGHT - 8 * (6 + 1),
    )

    def __init__(self, *groups):
        super().__init__(*groups)

        self.rect = pygame.Rect(self.OUTER)
        self.image = pygame.Surface(self.rect.size)

        self.group = pygame.sprite.Group()

        self.land = Land(self.group)
        self.spaceship = PlayerSpaceship((config.PLAYER_LEFT, config.PLAYER_TOP), self.group)
        self.border = Border(self.group)

        self.level = 1

        self.wave_length = 5
        self.enemies = pygame.sprite.Group()

        self.resource = None

    def load(self, resource):
        self.resource = resource

        self.land.load(resource)
        self.land.rect.bottom = self.rect.bottom

        self.border.load(resource)
        self.spaceship.load(resource)

    def check_land_rect(self, new_rect):
        # if new_rect.top > config.FIELD_OFFSET_Y:
        #     new_rect.top = config.FIELD_OFFSET_Y
        return new_rect

    @classmethod
    def check_spaceship(cls, spaceship):
        if spaceship.new_rect.left <= cls.SCOPE.left:
            spaceship.move(1, 0)
        if spaceship.new_rect.right >= cls.SCOPE.right:
            spaceship.move(-1, 0)
        if spaceship.new_rect.top <= cls.SCOPE.top:
            spaceship.move(0, 1)
        if spaceship.new_rect.bottom >= cls.SCOPE.bottom:
            spaceship.move(0, -1)

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)

        if len(self.enemies) == 0:
            self.level += 1
            self.wave_length += 5
            for _ in range(self.wave_length):
                enemy = EnemySpaceship(
                    (
                        random.randrange(self.SCOPE.left, self.SCOPE.right - EnemySpaceship.WIDTH),
                        random.randrange(-150, -10),
                    ),
                    random.choice([
                        EnemySpaceship.RED,
                        EnemySpaceship.GREEN,
                        EnemySpaceship.BLUE,
                    ]),
                    self.enemies,
                )
                enemy.load(self.resource)

        self.check_spaceship(self.spaceship)
        self.land.rect = self.check_land_rect(
            self.land.rect.move(0, self.spaceship.base_speed),
        )

        for enemy in self.enemies:
            if enemy.rect.top > self.HEIGHT:
                self.spaceship.die()
                self.enemies.remove(enemy)

        self.enemies.update(*args, **kwargs)
        self.group.update(*args, **kwargs)

    def draw(self, surface):
        self.image.fill(self.COLOR)
        self.group.draw(self.image)
        self.enemies.draw(self.image)
        surface.blit(self.image, self.rect)
