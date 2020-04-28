from pygame import Vector2
from .movement import Movement


class DirectionMovement(Movement):
    def __init__(self, sprite, thrust=60, angle=True):
        Movement.__init__(self, sprite, thrust)
        self.angle = angle

    def allow_movement(self):
        if self.angle:
            return True

        if self.vector == Vector2():
            return True

    def up_action(self):
        if self.allow_movement():
            self.vector.y -= 1

    def down_action(self):
        if self.allow_movement():
            self.vector.y += 1

    def left_action(self):
        if self.allow_movement():
            self.vector.x -= 1

    def right_action(self):
        if self.allow_movement():
            self.vector.x += 1

    def move(self, delta):
        if self.vector != Vector2():
            if self.angle:
                self.vector = self.vector.normalize()

            self.sprite._center += self.vector * (self.thrust * delta)
            self.sprite.set_position(self.sprite._center, "center")
            self.vector = Vector2()
