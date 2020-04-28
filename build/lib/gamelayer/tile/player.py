from pygame.transform import rotate as pygame_rotate


class TilePlayer:
    def __init__(self, tile, image, position):
        self.tile = tile
        self.image = image
        self.original_image = image
        self.rect = self.image.get_rect(center=position)
        self.center = self.rect.center

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def rotate(self, angle):
        self.image = pygame_rotate(self.original_image, angle)
        self.rect = self.image.get_rect(center=self.center)
