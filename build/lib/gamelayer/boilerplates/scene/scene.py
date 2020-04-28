from .state import State


class Scene:
    live = {}

    def __init__(self, manager, keep=False, name=None):
        self.state = State(self, manager)
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
