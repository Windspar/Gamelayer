import pygame
import gamelayer as game

class MainScene(game.Scene):
    def __init__(self, manager):
        game.Scene.__init__(self, manager)

    def on_draw(self, surface):
        surface.fill(game.color.dodgerblue)

def main():
    pygame.init()
    game.Manager.center_screen()
    manager = game.Manager("Basic", 800, 600)
    manager.flip(MainScene(manager))
    manager.mainloop()

main()
