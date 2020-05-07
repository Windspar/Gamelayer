from pygame.sprite import Sprite as PygameSprite
from pygame.transform import rotate as pygame_rotate, scale as pygame_scale
from pygame import Vector2
from .core import *
from .movement import *

class Sprite(PygameSprite):
    def __init__(self, image=None, position=(0, 0), anchor="topleft"):
        PygameSprite.__init__(self)
        self._position = AnchorPosition(self, position, anchor)
        self._rotate = Rotate(self)
        self.movement = None
        self.keys = None

        self._original_image = None
        self._center = Vector2()
        self._angle = 0

        if image:
            self.set_image(image)

    def add_movement(self, type, *args, **kwargs):
        if type == "mouse":
            self.movement = MouseMovement(self, *args, **kwargs)
        elif type == "direction":
            self.movement = DirectionMovement(self, *args, **kwargs)
        elif type == "vector":
            self.movement = VectorMovement(self, *args, **kwargs)

        if self.keys:
            self.keys.movement = movement

    def add_movement_keys(self, *args, **kwargs):
        self.keys = MovementKeys(self.movement, *args, **kwargs)

    def apply(self):
        image = self._original_image.copy()
        image = self._rotate.apply(image)

        self.image = image

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def rotate(self, degrees):
        self._rotate.rotate(degrees)
        self.apply()

    def set_angle(self, angle):
        self.angle = angle % 360
        self.apply()

    def set_auto_rotate(self, boolean):
        self._rotate.auto = boolean

    def set_image(self, image):
        self._original_image = image
        self.image = image
        self._position.apply()
        self.apply()

    def set_rotation(self, value):
        self._rotate.set_rotation(value)

    def set_position(self, position, anchor=None):
        self._position.set_position(position, anchor)

    def scale(self, size, anchor=None):
        self.image = pygame_scale(self._original_image, size)
        if anchor:
            self.apply_anchor(anchor)
        else:
            self.apply()

    def update(self, delta, keys_pressed):
        if self.keys:
            self.keys.update(delta, keys_pressed)

        self._rotate.auto_update(delta)
