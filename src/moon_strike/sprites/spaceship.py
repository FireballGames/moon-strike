import os
import config
from game_utils.image_sprite import ImageSprite


class Spaceship(ImageSprite):
    def __init__(self, pos, *groups):
        super().__init__(*groups)
        self.bounce = 0
        self.moving_x = 0
        self.moving_y = 0
        self.pos = pos

    def get_image(self, resource):
        return resource.spaceship

    def load(self, resource):
        super().load(resource)
        self.rect.topleft = self.pos

    def move(self, x=None, y=None):
        if x is not None:
            self.moving_x = x
        if y is not None:
            self.moving_y = y

    def get_new_rect(self):
        return self.rect.move(self.moving_x, self.moving_y)
