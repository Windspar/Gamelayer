from pygame import Rect, Vector2
from .camera_keys import TileCameraKeys

class TileCamera:
    def __init__(self, tile, start_position, speed=80/1000, camera_keys=None, allow_sliding=True):
        self.tile = tile
        self.speed = speed
        self.speed_boost = 1
        self.position = start_position
        self.allow_sliding = allow_sliding

        if camera_keys:
            self.keys = camera_keys
        else:
            self.keys = TileCameraKeys(self.move)

    def collision(self, position):
        player_map_position = lambda pos: Vector2(self.tile.player.rect.center) + pos
        old_position = player_map_position(self.position)
        new_position = player_map_position(position)

        for point in self.get_collision_locations(position):
            layer = self.tile.map[point]
            if layer.is_collidable:
                x, y = Vector2(point) * self.tile.size
                rect = Rect(x, y, self.tile.size, self.tile.size)
                npd = new_position.distance_to(rect.center)
                opd = old_position.distance_to(rect.center)

                if(rect.collidepoint(new_position)):
                    return True

        self.position = position
        return False

    def get_collision_locations(self, position):
        rect = self.tile.player.rect
        points = rect.topleft, rect.topright, rect.bottomleft, rect.bottomright
        return set([tuple(map(int, (position + point) / self.tile.size)) for point in points])

    def get_tile_position(self):
        return self.position // self.tile.size

    def get_offset(self):
        position = self.get_tile_position() * self.tile.size
        return self.position - position

    def move(self, direction, delta):
        position = self.move_position(direction, delta)
        if self.collision(position):
            if self.allow_sliding:
                self.slide(direction, delta)

        # Turn player
        direction.x, direction.y = direction.y, direction.x
        angle = direction.as_polar()[1] - 90
        self.tile.player.rotate(angle)

    def move_position(self, direction, delta):
        return self.position + direction * self.speed * delta * self.speed_boost

    def slide(self, direction, delta):
        dir = Vector2(direction)
        if direction.x != 0 and direction.y != 0:
            dir.x = 0
            position = self.move_position(dir, delta)
            if self.collision(position):
                dir.y = 0
                dir.x = direction.x
                position = self.move_position(dir, delta)
                self.collision(position)
        else:
            self.slide_sideways(direction, delta)

    def slide_sideways(self, direction, delta):
        half_size = self.tile.size / 2
        if direction.x == 0:
            value = (self.position.x + half_size) % self.tile.size
            direction.y = 0
            if value < half_size:
                direction.x = -1
            else:
                direction.x = 1

            position = self.move_position(direction, delta)
            self.collision(position)
        elif direction.y == 0:
            direction.x = 0
            # Unkown why I have to adjust position
            value = (self.position.y + half_size - 4) % self.tile.size
            if value < half_size:
                direction.y = -1
            else:
                direction.y = 1

            position = self.move_position(direction, delta)
            self.collision(position)

    def update(self, delta, keys_pressed):
        self.keys.update(delta, keys_pressed)
