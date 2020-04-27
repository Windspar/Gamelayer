

class Panel:
    def show(self, state):
        state.panel = self

    def close(self, state):
        state.panel = None

    def on_draw(self, surface): pass
    def on_event(self, event): pass
    def on_update(self, delta): pass
