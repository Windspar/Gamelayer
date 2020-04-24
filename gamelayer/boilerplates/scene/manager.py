import os
import pygame
from .scene import Scene
from .extension import Extension
from ...util import Timer


class Manager:
    @staticmethod
    def center_screen():
        os.environ['SDL_VIDEO_CENTERED'] = '1'

    def __init__(self, caption, width, height, flags=0):
        # Basic pygame setup
        pygame.display.set_caption(caption)
        self.surface = pygame.display.set_mode((width, height), flags)
        self.rect = self.surface.get_rect()
        self.clock = pygame.time.Clock()
        self.running = False
        self.delta = 0
        self.fps = 60

        # Extension
        self.extension = Extension()

        # Current Scene
        self._scene = Scene(self)

    def flip(self, state, *args, **kwargs):
        self._scene.state.drop()
        self._scene = state
        self._scene.state.focus(*args, **kwargs)

    def flip_back(self, state, *args, **kwargs):
        self._scene.state.drop()
        self._scene = state
        self._scene.state.focus(*args, **kwargs)

    def flip_new(self, state, *args, **kwargs):
        self._scene.state.drop()
        self._scene = state
        self._scene.state.new(*args, **kwargs)

    def mainloop(self):
        self.running = True
        while self.running:
            self._scene.state.event()
            self.extension.process_logic(self)
            Timer.get_ticks()
            self._scene.state.update(self.delta)
            self._scene.state.draw(self.surface)
            self.extension.process(self)

            pygame.display.flip()
            self.delta = self.clock.tick(self.fps)

    def quit(self):
        self.running = False
