import pygame
import gamelayer as game

class MainScene(game.Scene):
    def __init__(self, manager):
        game.Scene.__init__(self, manager)
        self.ui_events = game.UI_Events()
        self.create_textbox()

    def on_draw(self, surface):
        surface.fill(game.color.dodgerblue)

    def create_textbox(self):
        font = pygame.font.Font(None, 28)
        rect = pygame.Rect(10, 10, 300, 34)
        rect.centerx = self.state.manager.rect.centerx
        self.textline = game.TextLine(font, game.color.snow, self.text_enter, rect)
        position = rect.centerx, rect.centery + 100
        self.label = game.Label("", font, game.color.dodgerblue, position, "midtop")
        foreground = game.Gradient(True)
        foreground.blend(game.color.dodgerblue * 0.75, game.color.blue * 0.75)
        hover = game.Gradient(True)
        hover.blend(game.color.dodgerblue, game.color.blue)
        toggle = game.Gradient(True)
        toggle.blend(game.color.blue, game.color.dodgerblue)

        self.textbox = game.Renderer(self.textline, foreground, hover, toggle)
        self.ui_events.add(self.textline)

    def on_draw(self, surface):
        surface.fill(game.color.black)
        self.label.draw(surface)
        self.textbox.draw(surface)

    def on_event(self, event):
        self.ui_events.process_event(event)

    def on_update(self, delta):
        self.textline.update(delta)

    def text_enter(self, text):
        self.label.set_text(text)

def main():
    pygame.init()
    game.Manager.center_screen()
    manager = game.Manager("Textline Example", 800, 600)
    manager.flip(MainScene(manager))
    manager.mainloop()

main()
