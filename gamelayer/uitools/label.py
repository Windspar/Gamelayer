from pygame import MOUSEMOTION, MOUSEBUTTONDOWN, Color
from .uisprite import UISprite
from ..graphics import Gradient

class Label(UISprite):
    def __init__(self, text, font, color, position, anchor="topleft", *groups):
        UISprite.__init__(self, (0, 0, 0, 0), position, anchor, *groups)
        self._font = font
        self._text = text
        self._color = color
        self._render()

    def _render(self):
        if isinstance(self._color, Gradient):
            self.image = self._font.render(self._text, 1, Color('white'))
            self.image = self._color.apply_surface(self.image)
        else:
            self.image = self._font.render(self._text, 1, self._color)

        self.rect = self.image.get_rect(**{self._anchor: self._position})
        self._original_image = self.image
        self.apply_image()

    def blit(self, surface, rect):
        x = self.rect.x - rect.x
        y = self.rect.y - rect.y
        surface.blit(self.image, (x, y))

    def clip(self, rect):
        self.image = self._original_image.subsurface(rect)
        self.rect = self.image.get_rect(**{self._anchor: self._position})
        self.apply_image()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def set_text(self, text):
        self._text = text
        self._render()

    def set_font(self, font):
        self._font = font
        self._render()

    def set_color(self, color):
        self._color = color
        self._render()

    def unclip(self):
        self.image = self._original_image
        self.rect = self.image.get_rect(**{self._anchor: self._position})
        self.apply_image()

class ActionLabel(UISprite):
    def __init__(self, normal_label, hover_label, callback, user_data=None, *groups):
        UISprite.__init__(self, (0, 0, 0, 0), (0, 0), "topleft", *groups)
        self.callback = callback
        self.toggle_label = None
        self.is_toggleable = False
        self.user_data = user_data
        self.normal_label = normal_label
        self.hover_label = hover_label

        self.set_image(self.normal_label)

    def bind(self, events):
        events.bind(MOUSEMOTION, self.on_mousemotion)
        events.bind(MOUSEBUTTONDOWN, self.on_mousebuttondown)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def make_toggleable(self, toggle_label, toggle=False):
        self.toggle_label = toggle_label
        self.is_toggleable = True
        self._toggle = toggle

    def on_mousemotion(self, event):
        self._hover = self.rect.collidepoint(event.pos)
        if not self._toggle:
            if self._hover and self.image != self.hover_label.image:
                self.set_image(self.hover_label)
            elif not self._hover and self.image != self.normal_label.image:
                self.set_image(self.normal_label)

    def on_mousebuttondown(self, event):
        if event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.toggle(True)
                self.callback(self)
            else:
                self.toggle(False)

    def set_image(self, sprite):
        self.image = sprite.image
        self.rect = sprite.rect

    def toggle(self, boolean):
        if self.is_toggleable:
            if self._toggle == boolean:
                return
            self._toggle = boolean
        else:
            return

        if self._toggle:
            self.set_image(self.toggle_label)
        elif self._hover:
            self.set_image(self.hover_label)
        else:
            self.set_image(self.normal_label)
