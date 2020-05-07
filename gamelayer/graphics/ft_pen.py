from pygame.freetype import Font, SysFont
from pygame import Surface
from .util import blend_surfaces
from .gradient import Gradient


class FT_Pen:
    @classmethod
    def system_font(cls, fontname, size, foreground, background=None, bold=False, italic=False):
        font = SysFont(fontname, size, bold, italic)
        return cls(font, foreground, background)

    @classmethod
    def font(cls, fontname, size, foreground, background=None, font_index=0, resolution=0, ucs4=False):
        font = Font(fontname, size, font_index, resolution, ucs4)
        return cls(font, foreground, background)

    def __init__(self, font, foreground, background=None):
        self.foreground = foreground
        self.background = background
        self.font = font

    def __call__(self, text, position, anchor):
        return self._render(text, self.foreground, self.background, position, anchor)

    def _render(self, text, foreground, background, position, anchor):
        if isinstance(foreground, Gradient):
            surface, rect = self.font.render(text, (255, 255, 255))
            surface = foreground.apply_surface_blend(surface)
        elif isinstance(foreground, Surface):
            surface, rect = self.font.render(text, (255, 255, 255))
            surface = blend_surfaces(foreground, surface)
        elif background:
            if isinstance(background, Gradient):
                fg_surface, rect = self.font.render(text, foreground)
                surface = background.get_surface(rect.size)
                surface.blit(fg_surface, (0, 0))
            else:
                surface, rect = self.font.render(text, foreground, background)
        else:
            surface, rect = self.font.render(text, foreground)

        setattr(rect, anchor, position)
        return surface, rect

    def write(self, text, foreground, background, position, anchor):
        return self._render(text, foreground, background, position, anchor)
