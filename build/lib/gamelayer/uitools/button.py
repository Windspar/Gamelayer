from pygame import MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP
from .label import Label
from .image import Image
from .ui_base import UI_Base

class DraftButton(UI_Base):
    def __init__(self, rect, callback, user_data=None, togglebutton=False, *groups):
        UI_Base.__init__(self, rect, (0, 0), "topleft")
        self.callback = callback
        self.user_data = user_data
        self.image = self.build_surface()
        self._togglebutton = togglebutton

    def bind(self, events):
        events.bind(MOUSEMOTION, self.on_mousemotion)
        events.bind(MOUSEBUTTONDOWN, self.on_mousebuttondown)
        if not self._togglebutton:
            events.bind(MOUSEBUTTONUP, self.on_mousebuttonup)

    def on_mousebuttondown(self, event):
        if event.button == 1 and self._hover:
            if self._togglebutton:
                self._toggle = not self._toggle
                self.callback(self)
            else:
                self._toggle = True
        elif not self._togglebutton:
            self._toggle = False

        self.apply_image()

    def on_mousebuttonup(self, event):
        if event.button == 1:
            self._toggle = False
            if self._hover:
                self.callback(self)

            self.apply_image()

class Button(DraftButton):
    def __init__(self, text, font, color, rect, callback, user_data=None, anchor="center", togglebutton=False, *groups):
        DraftButton.__init__(self, rect, callback, user_data, togglebutton)
        self.label = Label(text, font, color, self.rect.center, anchor)
        self.label.set_apply_image(self.build_image)
        self.build_image()

    def build_image(self):
        surface = self.build_surface()
        self.label.draw_to(surface, self.rect)
        self.image = surface

    def draw(self, surface):
        self.label.draw(surface)

class ImageButton(DraftButton):
    def __init__(self, image, rect, callback, user_data=None, anchor="center", togglebutton=False):
        DraftButton.__init__(self, rect, callback, user_data, anchor, togglebutton)
        self.image_data = Image(self, image, self.rect.center, anchor)
        self.build_image()

    def build_image(self):
        surface = self.build_surface()
        self.image_data.draw(surface)
        self.image = surface

    def draw(self, surface):
        self.image.draw(surface)
