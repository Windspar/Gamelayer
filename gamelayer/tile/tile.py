from pygame import Rect, Vector2
from pygame.sprite import Group
from .cartesian_map import CartesianMap
from .collision import TileCollision
from .movement import TileMovement
from .camera import TileCamera
from .player import TilePlayer


class Tile:
    def __init__(self, tilesize, width, height, screen_rect, player_image, tile_position, slide_by=False):
        self.size = tilesize
        self.display_size = self.get_display_size(screen_rect)
        position = Vector2(tile_position) - self.display_size // 2
        self.camera = TileCamera(self, position * tilesize)
        self.map = CartesianMap(self, width, height)
        self.player = TilePlayer(self, player_image, screen_rect.center)
        self.collision = TileCollision(self)
        self.movement = TileMovement(self, slide_by)
        self.sprites = Group()

    def draw(self, surface):
        for layer, position in self.map.get_visable_tiles():
            if layer != "None":
                layer.draw(surface, position)

        self.sprites.draw(surface)
        self.player.draw(surface)

    def get_display_size(self, rect):
        size = Vector2(rect.size)
        return (size / self.size).elementwise() + 1

    def get_player_tile_position(self):
        return (self.camera.position + self.player.rect.center) / self.size

    def update(self, delta, keys_pressed):
        self.camera.update(delta, keys_pressed)
