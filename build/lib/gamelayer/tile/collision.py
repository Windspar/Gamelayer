from pygame import Rect, Vector2

class TileCollision:
    def __init__(self, tile):
        self.tile = tile

    def collide(self, position, rect):
        new_position = position + rect.center

        for point in self.get_locations(position, rect):
            layer = self.tile.map[point]
            if layer.is_collidable:
                x, y = Vector2(point) * self.tile.size
                rect = Rect(x, y, self.tile.size, self.tile.size)
                if(rect.collidepoint(new_position)):
                    return True

        return False

    def get_locations(self, position, rect):
        points = rect.topleft, rect.topright, rect.bottomleft, rect.bottomright
        return set([tuple(map(int, (position + point) / self.tile.size)) for point in points])
