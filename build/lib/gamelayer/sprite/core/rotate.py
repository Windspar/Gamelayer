from pygame.transform import rotate as pygame_rotate
from pygame import Vector2

class Rotate:
    def __init__(self, sprite, rotation=4, auto=False):
        self.auto = auto
        self.sprite = sprite
        self.rotation = rotation * 0.001

        # Sprite methods
        sprite.rotate = self.rotate
        sprite.rotation = self.rotation

    def apply(self, image):
        if self.sprite._angle != 0:
            return pygame_rotate(image, self.sprite._angle)

        return image

    def auto_update(self, delta):
        if self.auto:
            self.sprite._angle += self.rotation * delta
            self.sprite._angle %= 360

    def rotate(self, angle):
        self.sprite._angle += angle
        self.sprite._angle %= 360

    def set_rotation(self, value):
        self.rotation = value * 0.001
