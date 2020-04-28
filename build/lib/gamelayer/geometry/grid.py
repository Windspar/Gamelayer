from pygame import Rect

class Grid:
    @classmethod
    def init(cls):
        return cls((0, 0), (1, 1), (1, 1))

    def __init__(self, position, size, slice, gap=(0, 0)):
        self.slice = slice
        self.size = size
        self.gap = gap
        self.position = position
        self.update()

    def calculate_cut(self):
        x = self.slice[0] + self.gap[0]
        y = self.slice[1] + self.gap[1]
        return x, y

    def calculate_rect(self, position):
        width = self.size[0] * self.cut[0]
        height = self.size[1] * self.cut[1]
        return Rect(position, (width, height))

    def get_rect(self, location):
        return Rect(
            location[0] * self.cut[0] + self.rect.x,
            location[1] * self.cut[1] + self.rect.y,
            self.slice[0],
            self.slice[1])

    def get_location(self, mouse_position):
        mx, my = mouse_position
        x = int((mx - self.rect.x) / self.cut[0])
        y = int((my - self.rect.y) / self.cut[1])

        if not self.location_within(x, y):
            return

        if self.get_rect((x, y)).collidepoint(mx, my):
            return x, y

        return

    def location_within(self, x, y):
        sx, sy = self.size
        if 0 <= x < sx:
            if 0 <= y < sy:
                return True
        return False

    def update(self):
        self.cut = self.calculate_cut()
        self.rect = self.calculate_rect(self.position)
