from pygame.sprite import Sprite
from pygame import SRCALPHA, Surface, Rect

class UISprite(Sprite):
    def __init__(self, rect, position, anchor, *groups):
        Sprite.__init__(self, *groups)
        self._apply_image = None
        self._position = position
        self._anchor = anchor
        self._toggle = False
        self._hover = False
        self.image = None
        self.rect = Rect(rect)

    def apply_image(self):
        if self._apply_image:
            self._apply_image(self)

    def bind(self, events):
        events.bind(MOUSEMOTION, self.on_mousemotion)

    def blit(self, surface, rect):
        if self.image:
            x = self.rect.x - rect.x
            y = self.rect.y - rect.y
            surface.blit(self.image, (x, y))

    def build_surface(self, rect=None):
        if rect is None:
            rect = self.rect

        surface = Surface(rect.size, SRCALPHA)
        surface.fill((0, 0, 0, 0))
        return surface

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def on_mousemotion(self, event):
        self._hover = self.rect.collidepoint(event.pos)
        self.apply_image()

    def set_apply_image(self, callback):
        self._apply_image = callback

    def set_position(self, position, anchor=None):
        self._position = position
        if anchor:
            self._anchor = anchor

        setattr(self.rect, self._anchor, self._position)

    def set_toggle(self, boolean=True):
        self._toggle = boolean
        self.apply_image()
