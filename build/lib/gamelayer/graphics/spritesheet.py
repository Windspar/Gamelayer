from pygame.image import load as image_load
from pygame.transform import scale as image_scale
from ..geometry import Grid


class SpriteSheet:
    def __init__(self, sheet, alpha, tilesize, scale_by=1):
        self.sprite_sheet = image_load(sheet)
        self.tilesize = tilesize

        if alpha:
            self.sprite_sheet = self.sprite_sheet.convert_alpha()
        else:
            self.sprite_sheet = self.sprite_sheet.convert()

        self.scale(scale_by)

    def __getitem__(self, key):
        rect = self.grid.get_rect(key)
        return self.sprite_sheet.subsurface(rect)

    def blit_image(self, surface, key):
        rect = self.grid.get_rect(key)
        surface.blit(self.sprite_sheet, rect)

    def scale(self, scale_by):
        if scale_by != 1:
            size = self.sprite_sheet.get_size()
            size = int(size[0] // scale_by), int(size[1] // scale_by)
            self.sprite_sheet = image_scale(self.sprite_sheet, size)
            width = size[0] // self.tilesize
            height = size[1] // self.tilesize
            self.grid = Grid((0, 0), (width, height), (self.tilesize, self.tilesize))
