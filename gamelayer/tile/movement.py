from pygame import Vector2


class TileMovement:
    def __init__(self, tile, slide_by):
        self.tile = tile
        self.slide_by = slide_by

        self.move_position = self.tile.camera.move_position

    def move(self, direction, delta, entity):
        position = self.move_position(direction, delta)
        if self.tile.collision.collide(position, entity.rect):
            if self.slide_by:
                self.slide(direction, delta, entity)
        else:
            self.tile.camera.position = position

        # Turn entity
        direction.x, direction.y = direction.y, direction.x
        angle = direction.as_polar()[1] - 90
        entity.rotate(angle)

    def slide(self, direction, delta, entity):
        dir = Vector2(direction)
        if direction.x != 0 and direction.y != 0:
            dir.x = 0
            position = self.move_position(dir, delta)
            if self.tile.collision.collide(position, entity.rect):
                dir.y = 0
                dir.x = direction.x
                position = self.move_position(dir, delta)
                if not self.tile.collision.collide(position, entity.rect):
                    self.tile.camera.position = position
            else:
                self.tile.camera.position = position
        else:
            self.slide_sideways(direction, delta, entity)

    def slide_sideways(self, direction, delta, entity):
        half_size = self.tile.size / 2
        if direction.x == 0:
            value = (self.tile.camera.position.x + half_size) % self.tile.size
            direction.y = 0
            if value < half_size:
                direction.x = -1
            else:
                direction.x = 1

            position = self.move_position(direction, delta)
            if not self.tile.collision.collide(position, entity.rect):
                self.tile.camera.position = position
        elif direction.y == 0:
            direction.x = 0
            # Unkown why I have to adjust position by -4
            value = (self.tile.camera.position.y + half_size - 4) % self.tile.size
            if value < half_size:
                direction.y = -1
            else:
                direction.y = 1

            position = self.move_position(direction, delta)
            if not self.tile.collision.collide(position, entity.rect):
                self.tile.camera.position = position
