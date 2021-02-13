import config
from moon_strike import MoonStrike


def main():
    __game = MoonStrike(
        size=(config.WIDTH, config.HEIGHT),
        title=config.TITLE,
        fps=config.FPS,
    )
    __game()


if __name__ == '__main__':
    main()
