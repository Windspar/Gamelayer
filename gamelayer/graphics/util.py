from pygame.transform import scale as pygame_scale
from pygame import BLEND_RGBA_MULT, SRCALPHA, Surface
from ..graphics import Gradient

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

def blend_surfaces(surface_source, surface, special_flags=BLEND_RGBA_MULT):
    size = surface.get_size()
    surface_apply =  pygame_scale(surface_source, size)
    surface_apply.blit(surface, (0, 0), special_flags=special_flags)
    return surface_apply

def surface_getter(color, size):
    if isinstance(color, Gradient):
        return color.get_surface(size)
    elif isinstance(color, Surface):
        return pygame_scale(color, size)

    surface = Surface(size, SRCALPHA)
    surface.fill(color)
    return surface
