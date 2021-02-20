import pygame
from .sheet_sprite import get_sprite
from .lasers import YellowLaser, RedLaser, GreenLaser, BlueLaser


class Spaceship(pygame.sprite.Sprite):
    WIDTH = 32
    HEIGHT = 16

    def __init__(self, pos, *groups, max_health=100):
        super().__init__(*groups)
        self.pos = pos
        self.new_rect = None
        self.speed = 1

        self.max_health = max_health
        self.health = self.max_health

        self.laser_image = None
        self.lasers = []
        self.cool_down_counter = 0

        self.mask = None

    @property
    def area(self):
        raise NotImplementedError()

    @property
    def laser_class(self):
        raise NotImplementedError()

    def load(self, resource):
        sheet = resource.res_images.get('game-objects')
        get_sprite(self, sheet, self.area)

        self.laser_image = self.laser_class()
        if self.laser_image is not None:
            self.laser_image.load(sheet)

        self.rect.topleft = self.pos
        self.new_rect = self.rect.copy()

        self.mask = pygame.mask.from_surface(self.image)

    def update(self, *args, **kwargs):
        self.rect = self.new_rect.copy()

    def move(self, x=0, y=0):
        self.new_rect.move_ip(
            x * self.speed,
            y * self.speed,
        )


class PlayerSpaceship(Spaceship):
    __AREA = pygame.Rect(Spaceship.WIDTH * 0, 0, Spaceship.WIDTH, Spaceship.HEIGHT)

    def __init__(self, pos, *groups, max_health=100):
        super().__init__(pos, *groups, max_health=max_health)
        self.base_speed = 1
        self.lives = 3
        self.lost = False
        self.lost_count = 0

    @property
    def area(self):
        return self.__AREA

    @property
    def laser_class(self):
        return YellowLaser

    def die(self):
        self.lives -= 1
        if self.lives <= 0 or self.health <= 0:
            self.lost = True
            self.lost_count += 1


class EnemySpaceship(Spaceship):
    RED = 1
    GREEN = 2
    BLUE = 3
    AREAS = {
        RED: pygame.Rect(Spaceship.WIDTH * 1, 0, Spaceship.WIDTH, Spaceship.HEIGHT),
        GREEN: pygame.Rect(Spaceship.WIDTH * 2, 0, Spaceship.WIDTH, Spaceship.HEIGHT),
        BLUE: pygame.Rect(Spaceship.WIDTH * 3, 0, Spaceship.WIDTH, Spaceship.HEIGHT),
    }
    LASERS = {
        RED: RedLaser,
        GREEN: GreenLaser,
        BLUE: BlueLaser,
    }

    def __init__(self, pos, color, *groups, max_health=100):
        super().__init__(pos, *groups, max_health=max_health)
        self.color = color
        # self.base_speed = 1
        # self.lives = 3

    @property
    def area(self):
        return self.AREAS.get(self.color)

    @property
    def laser_class(self):
        return self.LASERS.get(self.color)

    def update(self, *args, **kwargs):
        self.move(0, 1)
        super().update(*args, **kwargs)


class RedSpaceship(EnemySpaceship):
    def __init__(self, pos, *groups, max_health=100):
        super().__init__(pos, self.RED, *groups, max_health=max_health)


class GreenSpaceship(EnemySpaceship):
    def __init__(self, pos, *groups, max_health=100):
        super().__init__(pos, self.GREEN, *groups, max_health=max_health)


class BlueSpaceship(EnemySpaceship):
    def __init__(self, pos, *groups, max_health=100):
        super().__init__(pos, self.BLUE, *groups, max_health=max_health)
