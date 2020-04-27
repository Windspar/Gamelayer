from pygame import Surface
from pygame.sprite import Sprite
from ..graphics import Gradient

class Renderer(Sprite):
    def __init__(self, tool, normal, hover, toggle, *groups):
        Sprite.__init__(self, *groups)
        self.tool = tool
        self.tool.set_apply_image(self.update_image)
        self._apply_image = None
        self.normal_image = self.process_image(normal)
        self.hover_image = self.process_image(hover)
        self.toggle_image = self.process_image(toggle)
        self.build_image(self.normal_image)

    def apply_image(self):
        if self._apply_image:
            self._apply_image(self)

    def build_image(self, base):
        self.image = base.copy()
        self.tool.draw_to(self.image, self.tool.rect)
        self.rect = self.tool.rect
        self.apply_image()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def process_image(self, image):
        if isinstance(image, Gradient):
            return image.get_surface(self.tool.rect.size)
        elif isinstance(image, Surface):
            return image

        surface = Surface(self.tool.rect.size)
        surface.fill(image)
        return surface

    def update_image(self, tool):
        if tool._toggle:
            self.build_image(self.toggle_image)
        elif tool._hover:
            self.build_image(self.hover_image)
        else:
            self.build_image(self.normal_image)

    def set_apply_image(self, callback):
        self._apply_image = callback
