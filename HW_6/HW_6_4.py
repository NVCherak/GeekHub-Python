class Point():
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value


class ChangeTool():
    def change(self, Point, x, y):
        Point.x = x
        Point.y = y


a = Point(1, 1)
tool = ChangeTool()

print(a.x, a.y)
tool.change(a, 2, 2)

print(a.x, a.y)
