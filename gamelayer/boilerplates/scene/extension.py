

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
