from pygame.sprite import Sprite
from pygame import Surface


class Carrot(Sprite):
    def __init__(self, text, font, color, position, anchor="midleft", sleep=500, awake=1000):
        Sprite.__init__(self)
        self.carrot_image = font.render(text, 1, color)
        self.invisiable = Surface((1, 1))
        self.invisiable.fill((0, 0, 0, 0))

        self.image = self.invisiable
        self.rect = self.carrot_image.get_rect(**{anchor: position})
        self.position = 0
        self.sleep = sleep
        self.awake = awake
        self.countdown = awake
        self._show = False
        self._enable = False
        self._callback = None

    def draw(self, surface):
        if self._show:
            surface.blit(self.image, self.rect)

    def draw_to(self, surface, rect):
        x = self.rect.x - rect.x
        y = self.rect.y - rect.y
        surface.blit(self.image, (x, y))

    def enable(self, boolean):
        self._enable = boolean
        self.show(boolean)

    def set_callback(self, callback):
        self._callback = callback

    def show(self, boolean):
        self._show = boolean
        if boolean:
            self.image = self.carrot_image
            self.countdown = self.awake
        else:
            self.image = self.invisiable
            self.countdown = self.sleep

        if self._callback:
            self._callback()

    def update(self, delta):
        if self._enable:
            self.countdown -= delta
            if self.countdown <= 0:
                self.show(not self._show)
