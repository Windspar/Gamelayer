from pygame.transform import scale as pygame_scale
from pygame import SRCALPHA, Surface
from ..graphics import Gradient

def surface_getter(color, size):
    if isinstance(color, Gradient):
        return color.get_surface(size)
    elif isinstance(color, Surface):
        return pygame_scale(color, size)

    surface = Surface(size, SRCALPHA)
    surface.fill(color)
    return surface

def background_creator(image, color, width, padding, anchor="center", offset=(0, 0)):
    image_rect = image.get_rect()
    rect = image_rect.copy()
    rect.w = width
    rect.h += padding

    position = getattr(rect, anchor)
    setattr(image_rect, anchor, position)
    image_rect.x += offset[0]
    image_rect.y += offset[1]

    surface = surface_getter(color, rect.size)
    surface.blit(image, image_rect)
    return surface
