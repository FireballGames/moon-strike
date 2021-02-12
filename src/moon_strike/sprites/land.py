import config
from game_utils.image_sprite import ImageSprite


class Land(ImageSprite):
    def get_image(self, resource):
        return resource.start

    def load(self, resource):
        super().load(resource)
        self.rect.bottom = config.FIELD_HEIGHT