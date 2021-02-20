import pygame


def get_sprite(sprite, sheet, area):
    sprite.image = pygame.Surface(area.size, pygame.SRCALPHA)
    sprite.rect = sprite.image.get_rect()
    sprite.image.blit(sheet, sprite.rect, area)


class SheetSprite(pygame.sprite.Sprite):
    AREA = pygame.Rect(0, 0, 16, 16)
    POS = (0, 0)

    def load(self, sprite_sheet):
        self.image = pygame.Surface(self.AREA.size, pygame.SRCALPHA)
        self.rect = self.image.get_rect()

        self.image.blit(sprite_sheet, self.rect, self.AREA)
        self.rect.topleft = self.POS
