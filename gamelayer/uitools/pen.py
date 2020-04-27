

class Pen:
    def __init__(self, font, color):
        self.font = font
        self.color = color

    def __call__(self, text):
        return self.font.render(text, 1, self.color)
