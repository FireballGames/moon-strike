# import os

__BLOCK = 8

WIDTH = 32 * __BLOCK
HEIGHT = 24 * __BLOCK
TITLE = "Moon Strike"
FPS = 30

BACKGROUND_COLOR = (0, 0, 0)
PATH = 'res'  # os.path.join('res')

FIELD_BACKGROUND_COLOR = (255, 255, 255)
FIELD_LEFT = 1 * __BLOCK
FIELD_TOP = 0
FIELD_WIDTH = 16 * __BLOCK
FIELD_HEIGHT = 22 * __BLOCK
FIELD_OFFSET_X = 1 * __BLOCK
FIELD_OFFSET_Y = 1 * __BLOCK

PLAYER_WIDTH = 4 * __BLOCK
PLAYER_HEIGHT = 2 * __BLOCK
PLAYER_LEFT = FIELD_OFFSET_X + 6 * __BLOCK
PLAYER_TOP = FIELD_OFFSET_Y + 18 * __BLOCK

PLAYER_SCOPE_LEFT = FIELD_OFFSET_X
PLAYER_SCOPE_TOP = FIELD_OFFSET_Y + 6 * __BLOCK
PLAYER_SCOPE_WIDTH = FIELD_WIDTH
PLAYER_SCOPE_HEIGHT = FIELD_HEIGHT
