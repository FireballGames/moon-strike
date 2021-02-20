import pygame


class TextSprite(pygame.sprite.Sprite):
    FONT_NAME = "comicsans"
    FONT_SIZE = 20

    def __init__(self, *groups):
        super().__init__(*groups)
        self.font = pygame.font.SysFont(self.FONT_NAME, self.FONT_SIZE)
        self.color = (0, 0, 0)

    def update(self, text='', *args, **kwargs):
        self.image = self.font.render(
            text,
            True,
            self.color,
        )
        self.rect = self.image.get_rect()


class LivesText(TextSprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.color = (255, 0, 0)

    def update(self, lives=0, *args, **kwargs):
        super().update(text="Lives: {lives}".format(lives=lives), *args, **kwargs)
        self.rect.topleft = (10, 10)


class LevelText(TextSprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.color = (0, 255, 0)

    def update(self, level=0, *args, **kwargs):
        super().update(text="Level: {level}".format(level=level), *args, **kwargs)
        self.rect.topleft = (10, 10)


class LostText(TextSprite):
    FONT_SIZE = 50

    def __init__(self, *groups):
        super().__init__(*groups)
        self.color = (0, 0, 255)

    def update(self, *args, **kwargs):
        super().update(text="You Lost!!!", *args, **kwargs)
        self.rect.topleft = (10, 50)
