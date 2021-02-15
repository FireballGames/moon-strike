BLOCK_SIZE = int(32 / 8)
SHEET_ROW = int(256 / 8)

L = 1
B = 2
T = 3
C = 4
V = 5
W = 6
P = 7

land_block = [
    [0, L, 0, L],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    # 1
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    # 2
    [L, B, L, B],
    [L, L, B, T],
    [0, 0, 0, 0],
    [L, 0, L, 0],
    # 3
    [C, L, 0, 0],
    [V, B, L, 0],
    [T, L, 0, V],
    [L, L, L, 0],
    # 4
    [C, L, 0, L],
    [B, 0, B, T],
    [0, L, 0, 0],
    [0, L, C, 0],
    # 5
    [0, 0, L, 0],
    [0, L, 0, 0],
    [L, 0, 0, 0],
    [B, L, 0, L],
    # 6
    [L, V, L, C],
    [V, C, 0, 0],
    [V, L, 0, L],
    [L, 0, L, C],
    # 7
    [C, 0, 0, V],
    [L, 0, 0, 0],
    [B, L, 0, L],
    [L, 0, 0, 0],
    # 8
    [B, 0, L, L],
    [W, W, W, W],
    [0, L, B, T],
    [W, P, P, P],
    # 9
    [L, C, L, B],
    [C, V, 0, L],
    [0, T, T, B],
    [L, L, B, 0],
    # 10
    [0, 0, 0, L],
    [B, 0, L, 0],
    [T, B, 0, B],
    [L, 0, L, L],
    # 11
    [0, 0, L, 0],
    [0, 0, 0, B],
    [0, 0, L, 0],
    [0, L, 0, L],
    # 12
    [B, T, L, 0],
    [L, 0, B, L],
    [B, 0, L, 0],
    [V, L, 0, L],
    # 13
    [T, B, L, 0],
    [B, 0, 0, V],
    [C, 0, 0, L],
    [L, 0, L, B],
    # 14
    [L, L, L, L],
    [L, L, L, L],
    [L, L, L, L],
    [L, L, L, L],
    # 15
    [L, L, L, L],
    [L, L, L, L],
    [L, L, L, L],
    [L, L, L, L],
    # 16
    [L, L, L, L],
    [L, L, L, L],
    [L, L, L, L],
    [4, 5, 6, 7],
]

land_map = []
for row in land_block:
    map_row = []
    for block_id in row:
        sprite_id = block_id * BLOCK_SIZE
        for offset in range(BLOCK_SIZE):
            map_row.append(sprite_id + offset)
    for block_row_id in range(BLOCK_SIZE, 0, -1):
        offset = (block_row_id - 1) * SHEET_ROW
        land_map.append([sprite_id + offset for sprite_id in map_row])

D = 128

SPECIAL = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

    *[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] * 16,
    # 1
    *[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] * 16,
    # 2
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] * 2,
    *[[D, D, D, D, D, D, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] * 8,
    *[[D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D]] * 4,
    *[[0, 0, 0, 0, 0, 0, 0, 0, 0, D, D, 0, 0, 0, 0, 0]] * 2,
    # 3
    *[[0, 0, 0, 0, 0, 0, 0, 0, 0, D, D, 0, 0, 0, 0, 0]] * 6,
    *[[0, 0, 0, 0, 0, 0, 0, 0, 0, D, D, D, D, D, D, D]] * 2,
    *[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] * 8,
    # 4
    *[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] * 8,
    *[[D, D, D, D, 0, 0, 0, 0, 0, 0, 0, 0, D, D, D, D]] * 8,
    # 5
    *[[D, D, D, D, 0, 0, 0, 0, 0, 0, 0, 0, D, D, D, D]] * 6,
    *[[D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D]] * 4,
    *[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, D, D, 0]] * 4,
    *[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, D, D, D, D, D, 0]] * 2,
    # 6
    *[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, D, D, 0, 0, 0, 0]] * 4,
    *[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] * 12,
    # 7
    *[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] * 16,
    # 8
    *[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] * 16,
    # *[[D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D]] * 4,
    # *[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] * 4,
    # *[[D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D]] * 4,
    # 9
    *[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] * 16,
    # 10
    *[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] * 16,
    # 11
    *[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] * 16,
    # 12
    *[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] * 16,
    # 13
    *[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] * 16,
    # 14
    *[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] * 16,
    # 15
    *[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] * 16,
    # 16
    *[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] * 16,
]


def fill_specials(land, specials):
    for y, land_row in enumerate(specials):
        for x, special_id in enumerate(land_row):
            if special_id > 0:
                land[y][x] = special_id


fill_specials(land_map, SPECIAL)


class LandObject:
    SPRITE_ID = 0

    def __init__(self, object_x, object_y):
        self.x = object_x * 8
        self.y = (object_y + 32) * 8


class Bunker(LandObject):
    SPRITE_ID = 1
    HEIGHT = 8 * 4
    WIDTH = 8 * 4


class Smile(LandObject):
    SPRITE_ID = 2
    HEIGHT = 8 * 4
    WIDTH = 8 * 4


class Doorbell(LandObject):
    SPRITE_ID = 3
    HEIGHT = 8 * 4
    WIDTH = 8 * 4


class Flower(LandObject):
    SPRITE_ID = 4
    HEIGHT = 8 * 4
    WIDTH = 8 * 4


class Fort(LandObject):
    SPRITE_ID = 5
    HEIGHT = 8 * 8
    WIDTH = 8 * 8


land_objects = [
    # 2 0
    Bunker(1, 8),
    Bunker(8, 12),
    Bunker(12, 12),
    # 3 16
    Smile(12, 20),
    Doorbell(1, 32),
    # 4 32
    Bunker(2, 44),
    Bunker(10, 44),
    # 5 48
    Bunker(2, 52),
    Bunker(10, 52),
    Bunker(4, 60),
    Bunker(8, 60),
    # 6 64
    Smile(9, 72),
    # 7 80
    Flower(7, 84),
    Flower(3, 88),
    Doorbell(7, 88),
    Flower(11, 88),
    Flower(7, 92),
    # 8 96
    Bunker(12, 104),
    Bunker(3, 112),
    # 9 112
    Bunker(0, 124),
    Bunker(2, 128),
    # 10 128
    Doorbell(4, 132),
    Doorbell(6, 136),
    Doorbell(8, 140),
    Bunker(10, 144),
    # 11 144
    Flower(0, 148),
    Bunker(12, 148),
    Flower(0, 152),
    Flower(4, 152),
    Flower(0, 156),
    Flower(4, 156),
    Flower(0, 160),
    # 12 160
    # 13 176
    Fort(4, 188),
    # 14 192
    # 15 208
    # 16 224
]
