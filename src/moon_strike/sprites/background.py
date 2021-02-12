import os
import config
from game_utils.image_sprite import ImageSprite


class Background(ImageSprite):
    COLOR = config.BACKGROUND_COLOR
    IMAGE_PATH = os.path.join(config.PATH, 'screen.png')

    def draw(self, surface):
        surface.fill(self.COLOR)
        super().draw(surface)
        surface.fill(self.COLOR)
