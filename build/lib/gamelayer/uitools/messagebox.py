from pygame import Rect, Surface, KEYDOWN, MOUSEBUTTONDOWN
from ..graphics.util import surface_getter, background_creator
from ..graphics import Gradient
from .panel import Panel

class MessageBoxObject:
    def __init__(self, pen, background):
        self.pen = pen
        self.background = background

    def create_image(self, text):
        self.image = self.pen(text)
        self.rect = self.image.get_rect()

    def create_render(self, width, padding, anchor):
        self.render = background_creator(self.image, self.background, width, padding, anchor)
        self.rect = self.render.get_rect()

    def draw(self, surface):
        surface.blit(self.render, self.rect)

class MessageBox(Panel):
    # @backgrounds (title, text, surface)
    def __init__(self, state, title_pen, text_pen, border, backgrounds, rect):
        self.title = MessageBoxObject(title_pen, backgrounds[0])
        self.text = MessageBoxObject(text_pen, backgrounds[1])
        self.background = backgrounds[2]
        self.center = rect.center
        self.border = border
        self.state = state

    def message(self, title, text, buttons):
        self.title.create_image(title)
        self.text.create_image(text)

        buttons_rect = Rect(0, 0, 0, 0)
        for button in buttons:
            buttons_rect = buttons_rect.union(button.rect)

        padding = 20
        size = (max(self.title.rect.w, self.text.rect.w + self.border + padding, buttons_rect.w),
                self.title.rect.h + 10 + self.text.rect.h + self.border + buttons_rect.h + padding)

        width = size[0]
        self.title.create_render(width, 10, "midleft")
        self.text.create_render(width - self.border, padding, "center")

        self.image = surface_getter(self.background, size)
        self.rect = self.image.get_rect()
        half_border = self.border // 2
        self.text.rect.y = self.title.rect.bottom + half_border
        self.text.rect.centerx = self.rect.centerx

        self.title.draw(self.image)
        self.text.draw(self.image)

        self.rect.center = self.center
        self.show(self.state)

    def on_draw(self, surface):
        surface.blit(self.image, self.rect)

    def on_event(self, event):
        if event.type == KEYDOWN:
            self.close(self.state)
        elif event.type == MOUSEBUTTONDOWN:
            self.close(self.state)
