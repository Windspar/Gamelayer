import pygame
import gamelayer as game

class MainState(game.DisplayState):
    def __init__(self, display_engine):
        game.DisplayState.__init__(self, display_engine)

    def on_draw(self, surface):
        surface.fill(game.color.dodgerblue)

def main():
    pygame.init()
    game.DisplayEngine.center_screen()
    display_engine = game.DisplayEngine("Basic Screen", 800, 600)
    display_engine.mainloop(MainState(display_engine))

main()
