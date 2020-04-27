import os
import pygame
import random
import gamelayer as game

class MainScene(game.Scene):
    def __init__(self, manager):
        game.Scene.__init__(self, manager)
        self.load_images()
        rect = self.state.manager.rect
        player = self.characters["manBlue_stand"]
        self.tile = game.Tile(32, 100, 100, rect, player, (50, 50))
        self.build_world()

    def load_images(self):
        filename = os.path.join("resources", "spritesheet_characters.png")
        xmlname = os.path.join("resources", "spritesheet_characters.xml")
        self.characters = game.XmlSpriteSheet(filename, True, xmlname, 2)
        filename = os.path.join("resources", "tilesheet_ground.png")
        self.ground = game.SpriteSheet(filename, True, 32, 2)

    def build_world(self):
        ground_images = {"grass 1": self.ground[(0, 0)],
                         "grass 2": self.ground[(1, 0)],
                         "grass 3": self.ground[(2, 0)],
                         "grass 4": self.ground[(3, 0)],
                         "dirt 1": self.ground[(4, 0)],
                         "dirt 2": self.ground[(5, 0)],
                         "stone 1": self.ground[(6, 0)],
                         "stone 2": self.ground[(7, 0)]}

        object_images = {"bush": self.ground[(20, 6)],
                         "grass": self.ground[(20, 7)],
                         "leaves": self.ground[(23, 7)]}

        width, height = map(int, self.tile.map.size)
        for y in range(height):
            for x in range(width):
                object_image = None
                ground_key, ground_image = random.choice(list(ground_images.items()))
                if ground_key.startswith("grass"):
                    if random.randint(0, 15) == 1:
                        object_image = random.choice(list(object_images.values()))

                collidable = object_image == object_images['bush']
                layer = game.TileLayer((ground_image, object_image), collidable)
                self.tile.map[(x, y)] = layer

    def on_draw(self, surface):
        surface.fill(game.color.gray5)
        self.tile.draw(surface)

    def on_update(self, delta):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE]:
            self.tile.camera.speed_boost = 3
        else:
            self.tile.camera.speed_boost = 1

        self.tile.update(delta, keys_pressed)

def main():
    pygame.init()
    game.Manager.center_screen()
    manager = game.Manager("Basic", 800, 600)
    manager.flip(MainScene(manager))
    manager.mainloop()

main()
