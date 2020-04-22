from pygame import Color, Surface, Vector3, surfarray, SRCALPHA
from pygame.transform import scale as image_scale
import math


class Gradient:
    def __init__(self, vertical=False):
        self.vertical = vertical
        self.surface = None

    def apply_surface(self, surface):
        if self.surface is None:
            return

        size = surface.get_size()
        gradient_surface = self.get_surface(size)
        for x in range(size[0]):
            for y in range(size[1]):
                position = x, y
                color = gradient_surface.get_at(position)
                color.a = surface.get_at(position).a
                gradient_surface.set_at(position, color)

        return gradient_surface

    def blend(self, *colors):
        if len(colors) < 2:
            return False

        vectors = []
        for color in colors:
            vectors.append(Vector3(color[:3]))

        distance = self._create_gradient_steps(*vectors)
        self.surface = self._create_surface(distance)
        for gstep in self.gradient_steps:
            gstep.draw(self.surface, self.vertical)

        return True

    def _create_gradient_steps(self, *colors):
        current = Vector3(colors[0][:3])
        self.gradient_steps = []
        distance = 0

        for color in colors[1:]:
            vector = Vector3(color)
            gradient_step = GradientStep(current, vector, distance)
            self.gradient_steps.append(gradient_step)
            distance += gradient_step.distance
            current = Vector3(vector)

        return distance

    def _create_surface(self, distance):
        if self.vertical:
            surface = Surface((1, distance), SRCALPHA)
        else:
            surface = Surface((distance, 1), SRCALPHA)

        return surface

    def get_surface(self, size=None):
        if size is None:
            return self.surface.copy()
        return image_scale(self.surface, size)

class GradientStep:
    def __init__(self, current, color, distance):
        values = color - current
        self.distance = int(max(map(abs, values)))
        self.start_distance = distance
        self.step = values / self.distance
        self.color = Vector3(current)

    def draw(self, surface, vertical):
        vector = Vector3(self.color)
        step = self.start_distance
        for i in range(self.distance):
            if vertical:
                surface.set_at((0, i + step), Color(*map(int, vector)))
            else:
                surface.set_at((i + step, 0), Color(*map(int, vector)))

            vector += self.step
            self.minmax_color_vector(vector)

    def minmax_color_vector(self, vector):
        vector.x = max(min(vector.x, 255), 0)
        vector.y = max(min(vector.y, 255), 0)
        vector.z = max(min(vector.z, 255), 0)
