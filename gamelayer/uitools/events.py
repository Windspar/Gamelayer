

class UIEvents:
    def __init__(self):
        self.events = {}

    def add(self, *tools):
        for tool in tools:
            tool.bind(self)

    def bind(self, event_type, callback):
        if self.events.get(event_type, False):
            self.events[event_type].append(callback)
        else:
            self.events[event_type] = [callback]

    def process_event(self, event):
        if event.type in self.events.keys():
            for callback in self.events[event.type]:
                callback(event)
