import config
from game_utils.image_sprite import ImageSprite


class Background(ImageSprite):
    COLOR = config.BACKGROUND_COLOR

    def get_image(self, resource):
        return resource.screen

    def draw(self, surface):
        surface.fill(self.COLOR)
        super().draw(surface)
