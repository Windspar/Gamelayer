from pygame import Vector2

class Movement:
    per_second = 0.001

    def __init__(self, sprite, thrust):
        self.sprite = sprite
        self.thrust = thrust * Movement.per_second
        self.vector = Vector2()

    def get_vector(self, *args): pass
    def move(self, delta): pass

    def up_action(self): pass
    def down_action(self): pass
    def left_action(self): pass
    def right_action(self): pass
    def brake_action(self): pass
