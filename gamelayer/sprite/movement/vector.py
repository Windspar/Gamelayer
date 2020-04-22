from pygame import Vector2
from .movement import Movement
from ...util import MaxValue

class VectorMovement(Movement):
    def __init__(self, sprite, thrust=10, friction=1, rotation=60, brake=6, max_velocity=150, angle=0):
        Movement.__init__(self, sprite, thrust)
        self.friction = friction * Movement.per_second ** 1.8
        self.rotation = rotation * Movement.per_second
        self.brake = brake * Movement.per_second ** 1.8
        self.sprite.set_angle(angle)
        self.velocity = MaxValue(max_velocity * Movement.per_second)
        self.vector = self.get_vector()
        self.current_friction = 0

        self._move = None
        self._rotate = None

    def apply_friction(self, delta, friction):
        self.current_friction = friction * delta
        self.velocity.decrease(self.current_friction)

    def get_vector(self):
        vector = Vector2()
        vector.from_polar((1, self.sprite.rotate.angle))
        vector.x, vector.y = vector.y, vector.x
        return vector

    def up_action(self):
        self._move = self.move_up

    def down_action(self):
        self._move = self.move_down

    def left_action(self):
        self._rotate = self.rotate_left

    def right_action(self):
        self._rotate = self.rotate_right

    def brake_action(self):
        self._move = self.move_brake

    def move(self, delta):
        if self._move:
            self._move(delta)
        else:
            self.apply_friction(delta, self.friction)

        if self._rotate:
            self._rotate(delta)

        center = self.vector.elementwise() * (self.velocity.value * delta)
        self.sprite._center -= center
        self.sprite.set_position(self.sprite._center, "center")

        self._move = None
        self._rotate = None

    def move_up(self, delta):
        self.velocity.value +=  self.thrust * delta * Movement.per_second

    def move_down(self, delta):
        self.velocity.value -=  self.thrust * delta * Movement.per_second

    def move_brake(self, delta):
        self.apply_friction(delta, self.brake)

    def rotate_left(self, delta):
        angle = self.sprite.rotate.angle
        self.sprite.set_angle(((angle + self.rotation * delta) % 360))
        self.vector = self.get_vector()

    def rotate_right(self, delta):
        angle = self.effects.rotate.angle
        self.effects.set_angle(((angle - self.rotation * delta) % 360))
        self.vector = self.get_vector()
