from pygame import QUIT
from pygame.event import get as event_get
from ...util import TimerSystem

class State:
    def __init__(self, scene, manager):
        self.panel = None
        self.scene = scene
        self.manager = manager
        self.timer = TimerSystem()
        self.previous_scene = None

    def draw(self, surface):
        self.scene.on_draw(surface)
        if self.panel:
            self.panel.on_draw(suface)

    def drop(self):
        self.timer.pause()
        self.scene.on_drop()
        self.panel = None

    def event(self):
        for event in event_get():
            if event.type == QUIT:
                self.scene.on_quit()
            elif self.panel:
                self.panel.on_event(event)
            else:
                self.scene.on_event(event)

    def focus(self, *args, **kwargs):
        self.timer.unpause()
        self.scene.on_focus(*args, **kwargs)

    def new(self,*args, **kwargs):
        self.timer.reset()
        self.scene.on_new(*args, **kwargs)

    @property
    def rect(self):
        return self.manager.rect

    def update(self, delta):
        self.timer.update()
        if self.panel:
            self.panel.on_update(delta)
        else:
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
