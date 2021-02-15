import pygame
import config
from game_utils.image_sprite import ImageSprite
from moon_strike.game_data.levels.level1 import land_map, land_objects


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
    SPRITE_WIDTH = 8
    SPRITE_HEIGHT = 8
    # SKIP_START = True
    SKIP_START = False

    def __init__(self, *groups):
        super().__init__(*groups)

        self.rect = pygame.Rect(0, 0, config.FIELD_WIDTH, 256 * self.SPRITE_HEIGHT)
        self.rect.left = config.FIELD_OFFSET_X
        # self.rect.bottom = config.FIELD_HEIGHT + config.FIELD_OFFSET_Y
        self.image = pygame.Surface(self.rect.size)
        self.image.fill((255, 0, 0))

        self.start = StartLand()
        self.sprites = None

    @classmethod
    def get_sprite_id(cls, x, y):
        if y < len(land_map):
            row = land_map[y]
            if x < len(row):
                return row[x]
        return 0

    def fill(self):
        rects = []
        for y in range(8):
            for x in range(32):
                rect = pygame.Rect(x * self.SPRITE_WIDTH, y * self.SPRITE_HEIGHT, self.SPRITE_WIDTH, self.SPRITE_HEIGHT)
                rects.append(rect)

        bunker = pygame.Rect(
            1 * self.SPRITE_WIDTH,
            4 * self.SPRITE_HEIGHT,
            4 * self.SPRITE_WIDTH,
            4 * self.SPRITE_HEIGHT,
        )
        smile = pygame.Rect(
            5 * self.SPRITE_WIDTH,
            4 * self.SPRITE_HEIGHT,
            4 * self.SPRITE_WIDTH,
            4 * self.SPRITE_HEIGHT,
        )
        doorbell = pygame.Rect(
            9 * self.SPRITE_WIDTH,
            4 * self.SPRITE_HEIGHT,
            4 * self.SPRITE_WIDTH,
            4 * self.SPRITE_HEIGHT,
        )
        flower = pygame.Rect(
            13 * self.SPRITE_WIDTH,
            4 * self.SPRITE_HEIGHT,
            4 * self.SPRITE_WIDTH,
            4 * self.SPRITE_HEIGHT,
        )
        fort = pygame.Rect(
            0,
            8 * self.SPRITE_HEIGHT,
            8 * self.SPRITE_WIDTH,
            8 * self.SPRITE_HEIGHT,
        )

        current = pygame.Rect(0, 0, self.SPRITE_WIDTH, self.SPRITE_HEIGHT)
        current.top = self.SPRITE_HEIGHT * 256
        for y in range(256):
            for x in range(16):
                rect = rects[self.get_sprite_id(x, y)]
                self.image.blit(
                    self.sprites,
                    current,
                    rect,
                )
                current = current.move(self.SPRITE_WIDTH, 0)
            current = current.move(0, -self.SPRITE_HEIGHT)
            current.left = 0

        for o in land_objects:
            if o.SPRITE_ID == 1:
                area = bunker
            elif o.SPRITE_ID == 2:
                area = smile
            elif o.SPRITE_ID == 3:
                area = doorbell
            elif o.SPRITE_ID == 4:
                area = flower
            elif o.SPRITE_ID == 5:
                area = fort
            else:
                continue
            self.image.blit(
                self.sprites,
                pygame.Rect(o.x, self.rect.height - o.y + 8, o.WIDTH, o.HEIGHT),
                area,
            )

    def load(self, resource):
        self.sprites = resource.sprites
        self.fill()

        if self.SKIP_START:
            return

        self.start.load(resource)
        self.start.rect.left = 0
        self.start.rect.bottom = self.rect.bottom - 32
        self.image.blit(
            self.start.image,
            self.start.rect,
        )

