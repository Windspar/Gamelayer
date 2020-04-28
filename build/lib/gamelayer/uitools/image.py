from pygame.sprite import Sprite

class Image(Sprite):
    def __init__(self, image, position, anchor="topleft"):
        self.image = image
        self.rect = image.get_rect(**{anchor: position})

    def blit(self, surface, rect):
        x = self.rect.x - rect.x
        y = self.rect.y - rect.y
        surface.blit(self.image, (x, y))

    def draw(self, surface):
        surface.blit(self.image, self.rect)
