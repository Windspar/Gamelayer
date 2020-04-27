from pygame.sprite import Sprite
from pygame import SRCALPHA, Surface, Rect

class UI_Base(Sprite):
    def __init__(self, rect, position, anchor, *groups):
        Sprite.__init__(self, *groups)
        self.image = None
        self.rect = Rect(rect)
        # Internal
        self._apply_image = None
        self._position = position
        self._anchor = anchor
        self._toggle = False
        self._hover = False

    def apply_image(self):
        if self._apply_image:
            self._apply_image(self)

    def bind(self, events):
        events.bind(MOUSEMOTION, self.on_mousemotion)

    def build_surface(self, rect=None):
        if rect is None:
            rect = self.rect

        surface = Surface(rect.size, SRCALPHA)
        surface.fill((0, 0, 0, 0))
        return surface

    def draw(self, surface):
        if self.image:
            surface.blit(self.image, self.rect)

    def draw_to(self, surface, rect):
        if self.image:
            x = self.rect.x - rect.x
            y = self.rect.y - rect.y
            surface.blit(self.image, (x, y))

    def get_position_from_rect(self, rect=None):
        if rect:
            self._position = getattr(rect, self._anchor)
        else:
            self._position = getattr(self.rect, self._anchor)

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
