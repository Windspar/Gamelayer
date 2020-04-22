import pygame
import itertools
import gamelayer as game
from pygame.sprite import Group

class MainScene(game.Scene):
    def __init__(self, manager):
        game.Scene.__init__(self, manager)
        self.group_labels = Group()
        self.group_buttons = Group()
        self.ui_events = game.UIEvents()

        self.font = pygame.font.Font(None, 28)
        position = self.state.manager.rect.right - 20, 20
        self.label = game.Label("Press A Button", self.font, game.color.snow, position, "topright")

        y = itertools.count(20, 32)
        rect = pygame.Rect(20, 0, 150, 30)
        for letter in "ABC":
            name = "Button " + letter
            rect.y = next(y)
            self.create_button(name, rect.copy(), self.push_button, "You push " + name)

        x = 20
        y = itertools.count(200, 40)
        red_toggle = self.create_toggle_button("red", (x, next(y)), self.toggle_color)
        self.create_toggle_button("lawngreen", (x, next(y)), self.toggle_color)
        self.create_toggle_button("dodgerblue", (x, next(y)), self.toggle_color)
        red_toggle.set_toggle()

        self.toggle = red_toggle
        self.toggle_surface = pygame.Surface((400, 120))
        self.toggle_surface.fill(game.color.red)

    def create_button(self, text, rect, callback, user_data):
        button = game.Button(text, self.font, game.color.snow, rect, callback, user_data)
        renderer = game.Renderer(button, game.color.dodgerblue * 0.75, game.color.dodgerblue, game.color.dodgerblue * 0.5, self.group_buttons)
        self.ui_events.add(button)

    def create_toggle_button(self, text, position, callback):
        rect = pygame.Rect(0, 0, 30, 30)
        foreground = pygame.Surface(rect.size, pygame.SRCALPHA)
        foreground.fill((0, 0, 0, 0))

        hover = foreground.copy()
        toggle = foreground.copy()
        pygame.draw.rect(foreground, game.color.dodgerblue * 0.75, rect, 7)
        pygame.draw.rect(hover, game.color.dodgerblue, rect, 7)
        pygame.draw.rect(toggle, game.color.dodgerblue * 0.5, rect, 7)
        pygame.draw.rect(toggle, game.color.dodgerblue * 0.5, rect.inflate(-20, -20))

        b_rect = pygame.Rect(position, (30, 30))
        button = game.DraftButton(b_rect, callback, text, True)
        renderer = game.Renderer(button, foreground, hover, toggle, self.group_buttons)
        self.ui_events.add(button)
        position = b_rect.x + 36, b_rect.centery
        color = pygame.Color(text)
        label = game.Label(text.capitalize(), self.font, color, position, "midleft", self.group_labels)
        return button

    def on_draw(self, surface):
        surface.fill(game.color.black)
        surface.blit(self.toggle_surface, (200, 200))
        self.label.draw(surface)
        self.group_labels.draw(surface)
        self.group_buttons.draw(surface)

    def on_event(self, event):
        self.ui_events.process_event(event)

    def push_button(self, button):
        self.label.set_text(button.user_data)

    def toggle_color(self, button):
        self.toggle.set_toggle(False)
        self.toggle = button
        self.toggle_surface.fill(pygame.Color(button.user_data))

def main():
    pygame.init()
    game.Manager.center_screen()
    manager = game.Manager("Button Example", 800, 600)
    manager.flip(MainScene(manager))
    manager.mainloop()

main()
