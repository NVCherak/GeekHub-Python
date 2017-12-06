class Calc:

    def add(self, a, b):
    # method addition two operands
        self._last_result = a + b # remember result
        return a + b

    def subtract(self, a, b):
    # method substraction two operands
        self._last_result = a - b
        return a - b

    def multiply(self, a, b):
    # method multiplication two operands
        self._last_result = a * b
        return a * b

    def divide(self, a, b):
    # method division two operands
        self._last_result = a / b
        return a / b


class Person():
    def __init__(self, *args):
    # method getting two positional arguments: first - name, second - age
        self._name = args[0]
        self._age = args[1]

    def show_age(self):
        print(self._age)

    def print_name(self):
        print(self._name)

    def show_all_information(self):
        print(self._name, self._age)


instance1 = Person('Kevin', 8)
instance2 = Person('Garry', 37)
instance1.profession = 'schoolboy'
instance2.profession = 'bandit'
