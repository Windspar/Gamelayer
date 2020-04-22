from pygame import Vector2
from itertools import product

class CartesianMap:
    def __init__(self, tile, width, height):
        self.tile = tile
        self.size = Vector2(width, height)
        self.tilemap = [["None" for w in range(width)] for h in range(height)]

    def get_visable_tiles(self):
        tilesize = self.tile.size
        cpos = self.tile.camera.position
        display_size = self.tile.display_size
        location = cpos / tilesize
        xrange = create_range(cpos.x, display_size.x, self.size.x, tilesize, True)
        yrange = create_range(cpos.y, display_size.y, self.size.y, tilesize)
        for x, y in product(xrange, yrange):
            position = (Vector2(x, y) - location) * tilesize
            yield self.tilemap[y][x], position

    def __getitem__(self, key):
        if isinstance(key, (tuple, list)):
            x, y = key
            return self.tilemap[y][x]

        return self.tilemap[key]

    def __setitem__(self, key, value):
        if isinstance(key, (tuple, list)):
            x, y = key
            self.tilemap[y][x] = value
        else:
            self.tilemap[key] = value

def create_range(begin_pos, end_pos, max_pos, tilesize, reverse=False):
    begin = begin_pos / tilesize
    start_range = max(int(begin), 0)
    end_range = min(int(begin + end_pos), int(max_pos))
    if reverse:
        return range(end_range - 1, start_range - 1, -1)
    return range(start_range, end_range)
