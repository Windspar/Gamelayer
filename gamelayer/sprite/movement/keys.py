from pygame.locals import *

class MovementKeys:
    wasd = {"up": K_w, "down": K_s, "left": K_a, "right": K_d, "brake": K_LSHIFT}
    arrow = {"up": K_UP, "down": K_DOWN, "left": K_LEFT, "right": K_RIGHT, "brake": K_RSHIFT}
    keypad = {"up": K_KP8, "down": K_KP2, "left": K_KP4, "right": K_KP6, "brake": K_KP5}

    def __init__(self, movement, keys="wasd"):
        self.movement = movement
        if keys == "wasd":
            self.set_keys(**MovementKeys.wasd)
        elif keys == "arrow":
            self.set_keys(**MovementKeys.arrow)
        elif isinstance(keys, (list, tuple)):
            self.add_keys(*keys)

    def add_keys(self, up=None, down=None, left=None, right=None, brake=None):
        if up:
            self.up.append(up)

        if down:
            self.down.append(down)

        if left:
            self.left.append(left)

        if right:
            self.right.append(right)

        if brake:
            self.brake.append(brake)

    def set_keys(self, up, down, left, right, brake):
        self.up = [up]
        self.down = [down]
        self.left = [left]
        self.right = [right]
        self.brake = [brake]

    def update(self, delta, keys_pressed):
        if any([keys_pressed[key] for key in self.up]):
            self.movement.up_action()

        if any([keys_pressed[key] for key in self.down]):
            self.movement.down_action()

        if any([keys_pressed[key] for key in self.left]):
            self.movement.left_action()

        if any([keys_pressed[key] for key in self.right]):
            self.movement.right_action()

        if any([keys_pressed[key] for key in self.brake]):
            self.movement.brake_action()

        self.movement.move(delta)
