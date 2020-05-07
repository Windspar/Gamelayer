from pygame.font import Font, SysFont
from pygame import Surface
from .util import blend_surfaces
from .gradient import Gradient


class Pen:
    @classmethod
    def system_font(cls, fontname, size, foreground, background=None, bold=False, italic=False):
        font = SysFont(fontname, size, bold, italic)
        return cls(font, foreground, background)

    @classmethod
    def font(cls, fontname, size, foreground, background=None):
        font = Font(fontname, size)
        return cls(font, foreground, background)

    def __init__(self, font, foreground, background=None):
        self.foreground = foreground
        self.background = background
        self.font = font

    def __call__(self, text, position, anchor):
        return self._render(text, self.foreground, self.background, position, anchor)

    def _render(self, text, foreground, background, position, anchor):
        if isinstance(foreground, Gradient):
            surface = self.font.render(text, 1, (255, 255, 255))
            surface = foreground.apply_surface_blend(surface)
        elif isinstance(foreground, Surface):
            surface = self.font.render(text, 1, (255, 255, 255))
            surface = blend_surfaces(foreground, surface)
        elif background:
            if isinstance(background, Gradient):
                fg_surface = self.font.render(text, 1, foreground)
                surface = background.get_surface(fg_surface.get_size())
                surface.blit(fg_surface, (0, 0))
            else:
                surface = self.font.render(text, 1, foreground, background)
        else:
            surface = self.font.render(text, 1, foreground)

        rect = surface.get_rect(**{anchor: position})
        return surface, rect

    def write(self, text, foreground, background, position, anchor):
        return self._render(text, foreground, background, position, anchor)
