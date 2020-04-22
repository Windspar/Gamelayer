from pygame.time import get_ticks as pygame_get_ticks

class Timer:
    ticks = 0
    default_interval = 30

    @classmethod
    def get_ticks(cls, *args):
        cls.ticks = pygame_get_ticks()

    def __init__(self, interval, callback, repeat=-1, user_data=None, system=None):
        self.interval = interval
        self.callback = callback
        self.user_data = user_data
        self.system = system
        self.identity = 0
        self.stop = False
        self.count = 0
        self.next_tick = Timer.ticks + self.get_interval()
        self.pause_ticks = 0
        self.repeat = repeat

    def get_interval(self):
        if self.interval < 0:
            return Timer.default_interval

        return self.interval

    def reset(self):
        self.next_tick = Timer.ticks + self.get_interval()

    def restart(self):
        self.stop = False
        self.reset()

    def pause(self):
        self.pause_ticks = Timer.ticks

    def pop(self):
        if self.system:
            self.system._remove_timers.append(self.identity)
            self.stop = True

    def unpause(self):
        ticks = Timer.ticks - self.pause_ticks
        self.next_tick += ticks
        self.pause_ticks = 0

    def unpause_system(self, ticks):
        self.next_tick += ticks

    def update(self):
        if not self.stop and self.pause_ticks == 0 and self.repeat != 0:
            self.count = 0
            if self.interval != 0:
                while Timer.ticks > self.next_tick:
                    self.count += 1
                    self.next_tick += self.get_interval()

            if self.count > 0 or self.interval == 0:
                if self.repeat > 0:
                    self.repeat -= 1

                self.callback(self)

class TimerSystem:
    def __init__(self):
        self._remove_timers = []
        self.pause_ticks = 0
        self.timers = {}
        self.identity = 1

    def __call__(self, interval, callback, repeat=-1, user_data=None):
        timer = Timer(interval, callback, repeat, user_data, self)
        timer.identity = self.identity
        self.identity += 1
        self.timers[timer.identity] = timer
        return timer

    def add(self, timer):
        timer.system = self
        timer.identity = self.identity
        self.identity += 1
        self.timers[timer.identity] = timer

    def pause(self):
        self.pause_ticks = Timer.ticks

    def pop(self, timer):
        del self.timers[timer.identity]

    def reset(self):
        for key in self.timers.keys():
            self.timers[key].reset()

    def unpause(self):
        ticks = Timer.ticks - self.pause_ticks
        self.pause_ticks = 0
        for key in self.timers.keys():
            self.timers[key].unpause_system(ticks)

    def update(self):
        if self.pause_ticks == 0:
            for identity in self._remove_timers:
                del self.timers[identity]

            self._remove_timers = []

            for key in self.timers.keys():
                self.timers[key].update()

    def update_manager(self, manager):
        self.update()
