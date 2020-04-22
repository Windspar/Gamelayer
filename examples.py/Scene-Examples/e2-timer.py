import pygame
import random
import gamelayer as game

# Scene has built-in timer system
class MainScene(game.Scene):
    def __init__(self, manager):
        game.Scene.__init__(self, manager)
        self.state.timer(2000, self.timer_color)
        self.background_color = game.color.black

    def on_draw(self, surface):
        surface.fill(self.background_color)

    def timer_color(self, timer):
        self.background_color = pygame.Color(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255))

def main():
    game.Manager.center_screen()
    manager = game.Manager("Basic", 800, 600)
    manager.flip(MainScene(manager))
    manager.mainloop()

main()
