import operator
from pygame import Rect, Vector2

class Integer:
    def __init__(self, variable):
        self.variable = variable

    def __get__(self, instance, owner):
        return getattr(instance, self.variable)

    def __set__(self, instance, value):
        setattr(instance, self.variable, int(value))

class Point:
    x = Integer("_x")
    y = Integer("_y")

    def __init__(self, *args):
        self.assign(*args)

    def _operation_(self, op, rhs):
        if isinstance(rhs, (int, float)):
            return Point(op(self.x, rhs), op(self.y, rhs))
        elif isinstance(rhs, (Point, Rect, Vector2):
            return Point(op(self.x, rhs.x), op(self.y, rhs.y))
        elif isinstance(rhs, (tuple, list)):
            return Point(op(self.x, rhs[0]), op(self.y, rhs[1]))

    def __add__(self, rhs):
        return self._operation_(operator.add, rhs)

    def __sub__(self, rhs):
        return self._operation_(operator.sub, rhs)

    def __mul__(self, rhs):
        return self._operation_(operator.mul, rhs)

    def __div__(self, rhs):
        return self._operation_(operator.div, rhs)

    def __mod__(self, rhs):
        return self._operation_(operator.mod, rhs)

    def __hash__(self):
        return self._x + self._y

    def __iter__(self):
        yield self._x
        yield self._y

    def assign(self, *args):
        length = len(args)
        if length == 1:
            arg = args[0]
            if isinstance(arg, (Point, Rect, Vector2)):
                self.x = arg.x
                self.y = arg.y
            elif isinstance(arg, (list, tuple)):
                self.x, self.y = arg[:2]
            else:
                self.x, self.y = arg[0]
        elif length == 2:
            self.x, self.y = args[:2]

    def copy(self):
        return Point(self._x, self._y)

    def repr(self):
        return "Point({}, {})".format(self._x, self._y)

    def swap(self):
        self._x, self._y = self._y, self._x
