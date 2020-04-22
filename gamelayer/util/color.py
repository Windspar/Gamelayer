import operator
from pygame import Color as PygameColor
from pygame.color import THECOLORS
from types import SimpleNamespace

class Color(PygameColor):
    minmax = lambda value: min(max(int(value), 0), 255)

    def _math(self, op, color):
        if isinstance(color, (int, float)):
            return Color(Color.minmax(op(self.r, color)),
                         Color.minmax(op(self.g, color)),
                         Color.minmax(op(self.b, color)),
                         self.a)
        elif isinstance(color, (Color, PygameColor)):
            return Color(Color.minmax(op(self.r, color.r)),
                         Color.minmax(op(self.g, color.g)),
                         Color.minmax(op(self.b, color.b)),
                         self.a)
        elif isinstance(color, (tuple, list)):
            return Color(Color.minmax(op(self.r, color[0])),
                         Color.minmax(op(self.g, color[1])),
                         Color.minmax(op(self.b, color[2])),
                         self.a)

    def __add__(self, color):
        return self._math(operator.add, color)

    def __sub__(self, color):
        return self._math(operator.sub, color)

    def __mul__(self, color):
        return self._math(operator.mul, color)

    def __truediv__(self, color):
        return self._math(operator.truediv, color)

def color_item(item):
    key, value = item
    return key, Color(*value)

color = SimpleNamespace(**dict(map(color_item, THECOLORS.items())))
