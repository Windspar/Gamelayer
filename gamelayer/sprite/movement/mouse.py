from pygame import Vector2, mouse
from .movement import Movement


class MouseMovement(Movement):
    def __init__(self, sprite, thrust=60, within=1, button=1, auto=False):
        Movement.__init__(self, sprite, thrust)
        self.mouse_position = Vector2(0, 0)
        self.within = within
        self.button = button
        self.auto = auto

    def get_vector(self, mouse_position):
        self.mouse_position = Vector2(mouse_position)
        return (Vector2(mouse_position) - self.sprite._center).normalize()

    def move(self, delta):
        button = mouse.get_pressed()[self.button - 1]
        if self.auto or button:
            pos = mouse.get_pos()
            if self.mouse_position != pos:
                self.vector = self.get_vector(pos)

            if self.mouse_position.distance_to(self.sprite._center) > self.within:
                self.sprite._center += self.vector * (delta * self.thrust)
                self.sprite.set_position(self.sprite._center, "center")
