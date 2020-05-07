import os
import pygame
import random
import itertools
import gamelayer as game

class MainScene(game.Scene):
    def __init__(self, manager):
        game.Scene.__init__(self, manager)
        self.text_list = []

        ypos = itertools.count(20, 30)

        create_text = False
        try:
            pen = game.FT_Pen.font(None, 24, game.color.dodgerblue)
            create_text = True
        except:
            print("Free type pen error.", pygame.get_error())

        if create_text:
            position = self.state.rect.centerx, next(ypos)
            self.text_list.append(pen("My First Pen", position, "midtop"))

        position = self.state.rect.centerx, next(ypos)
        pen = game.Pen.font(None, 24, game.color.dodgerblue)
        self.text_list.append(pen("My First Pen", position, "midtop"))

        gradient = game.Gradient(True)
        gradient.blend(game.color.blue, game.color.dodgerblue)
        position = self.state.rect.centerx, next(ypos)
        pen = game.Pen.font(None, 24, game.color.snow, gradient)
        self.text_list.append(pen("My First Pen", position, "midtop"))

        position = self.state.rect.centerx, next(ypos)
        pen = game.Pen.font(None, 24, gradient)
        self.text_list.append(pen("My First Pen", position, "midtop"))

        colorful_surface = pygame.Surface((100, 40), pygame.SRCALPHA)
        colorful_surface.fill(game.color.navy)

        random.seed(101)
        x = y = 0
        while True:
            size = random.randint(10, 22), 20
            rect = pygame.Rect((x, y), size)
            color = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            colorful_surface.fill(color, rect)
            x += size[0]
            if x > 100:
                if y != 0:
                    break

                x = 0
                y += 20

        position = self.state.rect.centerx, next(ypos)
        pen = game.Pen.font(None, 24, colorful_surface)
        self.text_list.append(pen("My First Pen", position, "midtop"))

    def on_draw(self, surface):
        surface.fill(game.color.black)
        for text in self.text_list:
            surface.blit(*text)

def main():
    pygame.init()
    game.Manager.center_screen()
    manager = game.Manager("Basic", 800, 600)
    manager.flip(MainScene(manager))
    manager.mainloop()

main()
