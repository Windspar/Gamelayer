from pygame import Vector2
from pygame.locals import *


class TileCameraKeys:
    def __init__(self, callback=None):
        self.callback = callback
        self.up = [K_w, K_UP]
        self.down = [K_s, K_DOWN]
        self.left = [K_a, K_LEFT]
        self.right = [K_d, K_RIGHT]

    def key_press(self, keys, keys_pressed):
        return any([keys_pressed[key] for key in keys])

    def update(self, delta, keys_pressed):
        direction = Vector2()
        if self.key_press(self.up, keys_pressed):
            direction.y -= 1

        if self.key_press(self.down, keys_pressed):
            direction.y += 1

        if self.key_press(self.left, keys_pressed):
            direction.x -= 1

        if self.key_press(self.right, keys_pressed):
            direction.x += 1

        if direction != Vector2():
            direction.normalize_ip()
            self.callback(direction, delta)
