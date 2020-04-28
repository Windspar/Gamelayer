import os
import pygame

class DisplayEngine:
    @staticmethod
    def center_screen():
        os.environ['SDL_VIDEO_CENTERED'] = '1'

    @staticmethod
    def screen_position(x, y):
        os.environ['SDL_VIDEO_WINDOW_POS'] = '{}, {}'.format(x, y)

    def __init__(self, caption, width, height, flags=0, fps=60):
        pygame.display.set_caption(caption)
        self.surface = pygame.display.set_mode((width, height), flags)
        self.rect = self.surface.get_rect()
        self.clock = pygame.time.Clock()
        self.running = False
        self.delta = 0
        self.fps = fps

    def mainloop(self, state):
        self.state = state
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state.on_quit()
                else:
                    self.state.on_event(event)

            self.state.on_update(self.delta)
            self.state.on_draw(self.surface)
            pygame.display.flip()
            self.delta = self.clock.tick(self.fps)

    def quit(self):
        self.running = False

class DisplayState:
    def __init__(self, display_engine):
        self.display_engine = display_engine

    def on_draw(self, surface): pass
    def on_event(self, event): pass
    def on_update(self, delta): pass

    def on_quit(self):
        self.display_engine.quit()
