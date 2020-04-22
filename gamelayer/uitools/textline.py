import string
from pygame import KMOD_CTRL, Rect, KEYDOWN, MOUSEMOTION, MOUSEBUTTONDOWN
from .label import Label
from .uisprite import UISprite
from .textline_core import *

class TextLine(UISprite):
    def __init__(self, font, color, callback, rect, allowed_keys=None, *groups):
        UISprite.__init__(self, rect, (0, 0), "topleft", *groups)
        self.callback = callback
        self._left = 0
        self._right = 0
        self._offset = 2

        if allowed_keys is None:
            self.allowed_keys = string.digits + string.ascii_letters + string.punctuation + " "

        self.recall = Recall()
        position = self.rect.x + self._offset, self.rect.centery
        self.carrot = Carrot("|", font, color, position)
        self.carrot.set_callback(self.build_image)
        self.buffer = Buffer(self.carrot, self.recall, callback)
        self.label = Label("", font, color, position, "midleft")
        self.label.set_apply_image(self.build_image)

    def bind(self, events):
        events.bind(KEYDOWN, self.on_keydown)
        events.bind(MOUSEMOTION, self.on_mousemotion)
        events.bind(MOUSEBUTTONDOWN, self.on_mousebuttondown)

    def build_image(self, tool=None):
        self.image = self.build_surface()
        self.label.blit(self.image, self.rect)
        self.carrot.blit(self.image, self.rect)
        self.apply_image()

    def draw(self, surface):
        self.label.draw(surface)
        self.carrot.draw(surface)

    def on_keydown(self, event):
        if self._toggle:
            self.carrot.show(True)
            ctrl = event.mod & KMOD_CTRL

            if ctrl == 0 and event.unicode in self.allowed_keys and event.unicode != "":
                self.buffer.insert(self.carrot.position, event.unicode)
                self.carrot.position += 1
                self.update_text()
            elif ctrl == 0:
                if event.key in self.buffer.key_events.keys():
                    self.buffer.key_events[event.key]()
                    self.update_text()

    def on_mousebuttondown(self, event):
        self._toggle = False
        if event.button == 1:
            if self._hover:
                self._toggle = True
                if not self.carrot._enable:
                    self.carrot.enable(True)

        if not self._toggle:
            self.carrot.enable(False)

        self.apply_image()

    def update(self, delta):
        self.carrot.update(delta)

    def update_text(self):
        if not self.buffer.empty():
            text = self.buffer.text
            font = self.label._font
            width = self.rect.width - self._offset * 3
            self.label.set_text(text)

            if self.carrot.position > self._right:
                self._right = self.carrot.position
            elif self.carrot.position < self._left:
                self._left = self.carrot.position

            # Looking for clipping text best fit. Base on carrot position
            # Move left position to the left.
            while font.size(text[self._left:self._right])[0] < width and self._left > 0:
                self._left -= 1

            # Move left position to the right.
            while font.size(text[self._left:self._right])[0] > width and self._left < self.carrot.position:
                self._left += 1

            # Move right position to right.
            while font.size(text[self._left:self._right])[0] < width and self._right < len(self.buffer):
                self._right += 1

            # Move right position to left.
            while font.size(text[self._left:self._right])[0] > width:
                self._right -= 1

            label_x = self.label.rect.x - 1
            x = font.size(text[0: self._left])[0]
            w = min(width, self.label.rect.width - x)
            # Smooth scrolling effect
            if w < width < self.label.rect.width:
                offset = width - (self.label.rect.width - x)
                x -= offset
                w += offset
                label_x += offset

            # Clip rect
            clip_rect = Rect(x, 0, w, self.label.rect.height)

            # Carrot position
            slice = text[self._left:self.carrot.position]
            self.carrot.rect.x = font.size(slice)[0] + label_x

            # Must set label clip rect. After setting carrot x position.
            # For image is update correctly.
            self.label.clip(clip_rect)

        else:
            self.carrot.rect.x = self.label.rect.x
            self.label.set_text("")
