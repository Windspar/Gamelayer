from pygame import Vector2

class TileSprite:
    def __init__(self, image, position, camera_position, anchor="topleft"):
        self.image = image
        self.original_image = image
        self.rect = image.get_rect(**{anchor: position})
        self.tile_position = Vector2(self.rect.center)
        self.map_position = self.tile_position - camera_position

    def move(self, position, camera_position):
        self.tile_position += position
        self.update(camera_position)

    def rotate(self, angle):
        self.image = pygame_rotate(self.original_image, angle)
        self.rect = self.image.get_rect(center=self.center)

    def update(self, camera_position):
        self.map_position = self.tile_position - camera_position
        self.rect.center = self.map_position
