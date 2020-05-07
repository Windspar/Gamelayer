from pygame.freetype import Font, SysFont


class FT_Pen:
    @classmethod
    def system_font(cls, fontname, size, color, bold=False, italic=False):
        self.font = SysFont(fontname, size, bold, italic)
        return cls(self.font, color)

    @classmethod
    def font(cls, fontname, size, color, font_index=0, resolution-0, ucs4=False):
        self.font = Font(fontname, size, font_index, resolution, ucs4)
        return cls(self.font, color)

    def __init__(self, font, color):
        self.color = color
        self.font = font

    def __call__(self, text):
        return self.font.render(text, 1, self.color)

    def write(self, text, color):
        return self.font.render(text, 1, color)
