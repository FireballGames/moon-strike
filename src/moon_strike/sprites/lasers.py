import pygame
from .sheet_sprite import SheetSprite


LASER_WIDTH = 16
LASER_HEIGHT = 16


class YellowLaser(SheetSprite):
    AREA = pygame.Rect(LASER_WIDTH * 0, LASER_HEIGHT, LASER_WIDTH, LASER_HEIGHT)
    POS = (64, 0)


class RedLaser(SheetSprite):
    AREA = pygame.Rect(LASER_WIDTH * 1, LASER_HEIGHT, LASER_WIDTH, LASER_HEIGHT)
    POS = (64, 32)


class GreenLaser(SheetSprite):
    AREA = pygame.Rect(LASER_WIDTH * 2, LASER_HEIGHT, LASER_WIDTH, LASER_HEIGHT)
    POS = (64, 64)


class BlueLaser(SheetSprite):
    AREA = pygame.Rect(LASER_WIDTH * 3, LASER_HEIGHT, LASER_WIDTH, LASER_HEIGHT)
    POS = (64, 96)
