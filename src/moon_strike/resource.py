import os
import pygame
import config


class Resource:
    PATH = config.PATH
    RES_FILES = {
        'game-objects': 'game-objects.png',
    }
    FILES = {
        'main_field': os.path.join(config.PATH, 'main_field.png'),
        'moon_strike': os.path.join(config.PATH, 'MoonStrike.png'),
        'numbers': os.path.join(config.PATH, 'numbers.png'),
        'screen': os.path.join(config.PATH, 'screen.png'),
        'spaceship': os.path.join(config.PATH, 'spaceship.png'),
        'sprites': os.path.join(config.PATH, 'sprites.png'),
        'start': os.path.join(config.PATH, 'start.png'),
    }

    def __init__(self):
        # self.image = pygame.image.load(self.IMAGE_PATH).convert()
        self.main_field = pygame.image.load(self.FILES['main_field'])
        self.moon_strike = pygame.image.load(self.FILES['moon_strike'])
        self.numbers = pygame.image.load(self.FILES['numbers'])
        self.screen = pygame.image.load(self.FILES['screen'])
        self.spaceship = pygame.image.load(self.FILES['spaceship'])
        self.sprites = pygame.image.load(self.FILES['sprites'])
        self.start = pygame.image.load(self.FILES['start'])

        self.res_images = self.__load_resources()

    @classmethod
    def __load_resources(cls):
        return {
            k: pygame.image.load(os.path.join(cls.PATH, v))
            for k, v in cls.RES_FILES.items()
        }
