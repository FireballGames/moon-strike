import pygame
import config
from game_utils.image_sprite import ImageSprite


class StartLand(ImageSprite):
    def get_image(self, resource):
        return resource.start

    def load(self, resource):
        super().load(resource)
        self.rect.left = config.FIELD_OFFSET_X
        self.rect.bottom = config.FIELD_HEIGHT


class LandSprite(ImageSprite):
    def get_image(self, resource):
        return resource.sprites


class Land(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.rect = pygame.Rect(0, 0, config.FIELD_WIDTH, 8 * 128)
        self.rect.left = config.FIELD_OFFSET_X
        # self.rect.bottom = config.FIELD_HEIGHT + config.FIELD_OFFSET_Y
        self.image = pygame.Surface(self.rect.size)
        self.image.fill((255, 0, 0))

        self.start = StartLand()
        self.sprites = None

    def fill(self):
        rect_1 = pygame.Rect(0, 0, 32, 32)

        current = pygame.Rect(0, 0, 32, 32)
        for y in range(32):
            current.left = 0
            current.top = y * 32
            for x in range(4):
                rect = rect_1
                self.image.blit(
                    self.sprites,
                    current,
                    rect,
                )
                current = current.move(32, 0)

    def load(self, resource):
        self.sprites = resource.sprites
        self.fill()

        self.start.load(resource)
        self.start.rect.left = 0
        self.start.rect.bottom = self.rect.bottom
        self.image.blit(
            self.start.image,
            self.start.rect,
        )

