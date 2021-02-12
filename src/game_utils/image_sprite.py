import os
import pygame
import config


class ImageSprite(pygame.sprite.Sprite):
    def get_image(self, resource):
        raise NotImplementedError()

    def load(self, resource):
        self.image = self.get_image(resource)
        self.rect = self.image.get_rect()

    def draw(self, surface):
        surface.blit(self.image, self.rect)
