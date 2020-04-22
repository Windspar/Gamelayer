import os
import pygame
import gamelayer as game

class MainScene(game.Scene):
    def __init__(self, manager):
        game.Scene.__init__(self, manager)
        self.load_images()

        position = self.state.manager.rect.centerx, 100
        self.alien = game.Sprite(self.images["shipBlue_manned"], position, "midtop")
        self.alien.add_movement("direction", 100)
        self.alien.add_movement_keys()

    def load_images(self):
        spritesheet = os.path.join("resources", "spritesheet_spaceships.png")
        xml = os.path.join("resources", "spritesheet_spaceships.xml")
        self.images = game.XmlSpriteSheet(spritesheet, True, xml)

    def on_draw(self, surface):
        surface.fill(game.color.black)
        self.alien.draw(surface)

    def on_update(self, delta):
        keys_pressed = pygame.key.get_pressed()
        self.alien.update(delta, keys_pressed)

def main():
    pygame.init()
    game.Manager.center_screen()
    manager = game.Manager("Basic", 800, 600)
    manager.flip(MainScene(manager))
    manager.mainloop()

main()
