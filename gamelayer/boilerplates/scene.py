import os
import pygame
from ..util.timer import TimerSystem, Timer

class Extension:
    def __init__(self):
        self._logic = []
        self._extension = []

    def add(self, callback):
        self._extension.append(callback)

    def add_logic(self, callback):
        self._logic.append(callback)

    def process(self, manager):
        for extension in self._extension:
            extension(manager)

    def process_logic(self, manager):
        for extension in self._logic:
            extension(manager)

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

class Scene:
    live = {}

    def __init__(self, manager, keep=False, name=None):
        self.state = StateManager(self, manager)
        if keep:
            if name is None:
                name = self.__class__.__name__

            Scene.live[name] = self

    def on_quit(self):
        self.state.manager.quit()

    # Scene Interface
    def on_draw(self, surface): pass
    def on_drop(self, *args, **kwargs): pass
    def on_event(self, event): pass
    # When it gain focus
    def on_focus(self, *args, **kwargs): pass
    def on_new(self, *args, **kwargs): pass
    def on_update(self, delta, *args, **kwargs): pass

class StateManager:
    def __init__(self, scene, manager):
        self.scene = scene
        self.manager = manager
        self.timer = TimerSystem()
        self.previous_scene = None

    def draw(self, surface):
        self.scene.on_draw(surface)

    def drop(self):
        self.timer.pause()
        self.scene.on_drop()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.scene.on_quit()
            else:
                self.scene.on_event(event)

    def focus(self, *args, **kwargs):
        self.timer.unpause()
        self.scene.on_focus(*args, **kwargs)

    def new(self,*args, **kwargs):
        self.timer.reset()
        self.scene.on_new(*args, **kwargs)

    def update(self, delta):
        self.timer.update()
        self.scene.on_update(delta)

    def _flip(self, scene):
        if isinstance(scene, Scene):
            return scene
        else:
            return Scene.live[scene]

    def flip(self, scene, *args, **kwargs):
        new_scene = self._flip(scene)
        self.manager.flip(new_scene, *args, **kwargs)

    def flip_back(self, *args, **kwargs):
        if self.previous_scene:
            self.manager.flip_back(self.previous_scene, *args, **kwargs)

    def flip_new(self, scene, *args, **kwargs):
        new_scene, boolean_live = self._flip(scene)
        self.manager.flip_new(new_scene, *args, **kwargs)
