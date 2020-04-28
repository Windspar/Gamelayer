from pygame import K_BACKSPACE, K_RETURN, K_DELETE, K_RIGHT, K_LEFT, K_DOWN, K_HOME, K_END, K_UP


class Buffer:
    def __init__(self, carrot, recall, callback):
        self.carrot = carrot
        self.recall = recall
        self.callback = callback
        self.buffer = []

        self.key_events = {
            K_BACKSPACE: self.key_backspace,
            K_RETURN: self.key_return,
            K_DELETE: self.key_delete,
            K_RIGHT: self.key_right,
            K_LEFT: self.key_left,
            K_DOWN: self.key_down,
            K_HOME: self.key_home,
            K_END: self.key_end,
            K_UP: self.key_up
        }

    def __len__(self):
        return len(self.buffer)

    def empty(self):
        return len(self.buffer) == 0

    def insert(self, position, string):
        self.buffer.insert(position, string)

    def key_backspace(self):
        if self.carrot.position > 1:
            front = self.buffer[:self.carrot.position - 1]
            back = self.buffer[self.carrot.position:]
            self.buffer = front + back
            self.carrot.position -= 1
        else:
            self.key_delete()

    def key_delete(self):
        self.buffer = []
        self.carrot.position = 0

    def key_down(self):
        self.buffer = self.recall.move_down()
        if self.buffer:
            self.carrot.position = len(self.buffer)
        else:
            self.key_delete()

    def key_end(self):
        self.carrot.position = len(self.buffer)

    def key_home(self):
        self.carrot.position = 0

    def key_left(self):
        if self.carrot.position > 0:
            self.carrot.position -= 1

    def key_return(self):
        self.recall.append(self.buffer)
        self.callback(self.text)
        self.key_delete()

    def key_right(self):
        if self.carrot.position < len(self.buffer):
            self.carrot.position += 1

    def key_up(self):
        buffer = self.recall.move_up()
        if buffer:
            self.buffer = buffer
            self.carrot.position = len(self.buffer)

    @property
    def text(self):
        if self.empty():
            return ""
        return "".join(self.buffer)
