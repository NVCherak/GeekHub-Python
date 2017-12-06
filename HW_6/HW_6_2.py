class Figure():
    _color = 'white'

    def __init__(self, value):
        self._color = value

    def change_color(self, value):
        self._color = value

    def get_info(self):
        print(self._color)

class Oval(Figure):
    def __init__(self, color, width, height):
        super().__init__(color)
        self._widh = width
        self._height = height

    def get_info(self):
        print(self._color, self._widh, self._height)

class Square(Figure):
    def __init__(self, color, side):
        super().__init__(color)
        self._side = side

    def get_info(self):
        print(self._color, self._side)


instance = Square('red', 50)
instance.get_info()

instance2 = Oval('yellow', 10, 15)
instance2.get_info()
