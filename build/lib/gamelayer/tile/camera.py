from .camera_keys import TileCameraKeys

class TileCamera:
    def __init__(self, tile, start_position, speed=80/1000, camera_keys=None):
        self.tile = tile
        self.speed = speed
        self.speed_boost = 1
        self.position = start_position

        if camera_keys:
            self.keys = camera_keys
        else:
            self.keys = TileCameraKeys(self.move)

    def get_tile_position(self):
        return self.position // self.tile.size

    def get_offset(self):
        position = self.get_tile_position() * self.tile.size
        return self.position - position

    def move(self, direction, delta):
        self.tile.movement.move(direction, delta, self.tile.player)

    def move_position(self, direction, delta):
        return self.position + direction * self.speed * delta * self.speed_boost

    def update(self, delta, keys_pressed):
        self.keys.update(delta, keys_pressed)
