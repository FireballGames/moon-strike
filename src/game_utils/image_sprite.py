import os
import pygame
import config


class ImageSprite(pygame.sprite.Sprite):
    IMAGE_PATH = os.path.join(config.PATH, '../../res/screen.png')

    def load(self):
        # self.image = pygame.image.load(self.IMAGE_PATH).convert()
        self.image = pygame.image.load(self.IMAGE_PATH)
        self.rect = self.image.get_rect()

    def draw(self, surface):
        surface.blit(self.image, self.rect)
