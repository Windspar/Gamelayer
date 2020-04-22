import pygame
import itertools
import gamelayer as game

class MainScene(game.Scene):
    def __init__(self, manager):
        game.Scene.__init__(self, manager)

        # Basic Label
        self.font = pygame.font.Font(None, 28)
        self.font50 = pygame.font.Font(None, 50)
        position = self.state.manager.rect.centerx, 10
        self.label = game.Label("Hello World", self.font50, game.color.white, position, "midtop")

        # Gradients
        self.create_gradients()

        # Gradient Label
        position = self.state.manager.rect.centerx, 60
        self.g_label = game.Label("Hello World", self.font50, self.blue_white, position, "midtop")

        # Action Labels
        y = itertools.count(200, 32)
        x = 60
        self.group_action_labels = pygame.sprite.Group(
            self.create_action_label("Gradient blue white blue", (x, next(y)), self.label_action, self.blue_white),
            self.create_action_label("Gradient red orange red", (x, next(y)), self.label_action, self.red_orange),
            self.create_action_label("Gradient green yellow green", (x, next(y)), self.label_action, self.green_yellow))

    def create_action_label(self, text, position, callback, user_data):
        color = game.color.dodgerblue * 0.7
        hover = game.color.dodgerblue
        foreground = game.Label(text, self.font, color, position)
        hover = game.Label(text, self.font, hover, position)
        return game.ActionLabel(foreground, hover, callback, user_data)

    def create_gradients(self):
        self.blue_white = game.Gradient()
        self.blue_white.blend(game.color.dodgerblue, game.color.white, game.color.dodgerblue)

        self.red_orange = game.Gradient()
        self.red_orange.blend(game.color.red, game.color.orange, game.color.red)

        self.green_yellow = game.Gradient()
        self.green_yellow.blend(game.color.green, game.color.yellow, game.color.green)

    def label_action(self, label):
        self.label.set_color(label.user_data)

    def on_draw(self, surface):
        surface.fill(game.color.black)
        self.label.draw(surface)
        self.g_label.draw(surface)
        self.group_action_labels.draw(surface)

    def on_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            for act in self.group_action_labels:
                act.on_mousemotion(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for act in self.group_action_labels:
                act.on_mousebuttondown(event)

def main():
    pygame.init()
    game.Manager.center_screen()
    manager = game.Manager("Label Example", 800, 600)
    manager.flip(MainScene(manager))
    manager.mainloop()

main()
