from pygame import Vector2

class MaxVector(Vector2):
    def __init__(self, maximum, x=0, y=0):
        Vector2.__init__(self, x, y)
        self.maximum = maximum
        self.minmax()

    def __hash__(self):
        return self.x + self.y

    def wrap(self, vector):
        return MaxVector(self.maximum, vector.x, vector.y)

    def minmax(self):
        self.x = min(max(self.x, -self.maximum), self.maximum)
        self.y = min(max(self.y, -self.maximum), self.maximum)

    def increase(self, vector):
        self.x = self._increase(self.x, vector.x)
        self.y = self._increase(self.y, vector.y)
        self.minmax()

    def decrease(self, vector):
        self.x = self._decrease(self.x, vector.x)
        self.y = self._decrease(self.y, vector.y)
        self.minmax()

    def _increase(self, value, speed):
        if value >= 0:
            return max(value + speed, 0)
        return min(value - speed, 0)

    def _decrease(self, value, speed):
        if self.x >= 0:
            return max(value - speed, 0)
        return min(value + speed, 0)

class MinMaxVector(MaxVector):
    def __init__(self, minimum, maximum, x=0, y=0):
        MaxVector.__init__(self, maximum, x, y)
        self.minimum = minimum

    def wrap(self, vector):
        return MinMaxVector(self.minimum, self.maximum, vector.x, vector.y)

    def minmax(self):
        self.x = min(max(self.x, self.minimum), self.maximum)
        self.y = min(max(self.y, self.minimum), self.maximum)

class MaxValue:
    def __init__(self, maximum, value=0):
        self.maximum = maximum
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = min(max(value, -self.maximum), self.maximum)

    def __add__(self, value):
        self.value = self._value + value

    def __sub__(self, value):
        self.value = self._value - value

    def __mul__(self, value):
        self.value = self._value * value

    def __truediv__(self, value):
        self.value = self._value / value

    def __floordiv__(self, value):
        self.value = self._value // value

    def increase(self, value):
        if self._value >= 0:
            self.value = max(self._value + value, 0)
        else:
            self.value = min(self._value - value, 0)

    def decrease(self, value):
        if self._value >= 0:
            self._value = max(self._value - value, 0)
        else:
            self._value = min(self._value + value, 0)

class MinMaxValue(MaxValue):
    def __init__(self, minimum, maximum, value=0):
        MaxValue.__init__(self, maximum, value)
        self.minimum = minimum

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = min(max(value, self.minimum), self.maximum)
