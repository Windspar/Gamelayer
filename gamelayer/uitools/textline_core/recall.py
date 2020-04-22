class Recall:
    def __init__(self, max_count=10):
        self.max_count = max_count
        self.position = 0
        self.buffer = []

    def move_up(self):
        if self.position < len(self.buffer) - 1:
            self.position += 1
            return self.buffer[self.position]

    def move_down(self):
        if self.position > 0:
            self.position -= 1
            return self.buffer[self.position]
        else:
            self.position = -1

    def append(self, text):
        self.position = -1
        if text not in self.buffer:
            if len(self.buffer) >= self.max_count:
                self.buffer = [text] + self.buffer[:self.max_count - 1]
            else:
                self.buffer.insert(0, text)
        elif self.buffer[0] != text:
            self.buffer.remove(text)
            self.buffer.insert(0, text)
