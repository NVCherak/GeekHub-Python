class Figure():
    count = 0

    def __init__(self):
        Figure.count += 1


class Thing():
    pass


example = Thing()
print(type(example), type(Thing()))


class Thing2():
    letters = 'abc'

example2 = Thing2()
print(example2.letters)


class Thing3():
    pass


example3 = Thing3()
example3.letters = 'xyz'
print(example3.letters)


class DefaultClass():
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        self._symbo = value

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value


print(DefaultClass.__dict__.keys())


class DefaultClass1():
    def __init__(self, dict_):
        self._name = dict_['name']
        self._l_name = dict_['l_name']
        self._age = dict_['age']

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def l_name(self):
        return self._l_name

    @l_name.setter
    def l_name(self, value):
        self._l_name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    def print_info(self):
        print('Name:', self._name + ';', 'Surname:', self._l_name + ';',
            'Age:', str(self._age) + '.')


Vasya = {'name': 'Vasya', 'l_name': 'Pupkin', 'age': 20}
employee = DefaultClass1(Vasya)
print(employee.name, employee.l_name, employee.age)
employee.print_info()


class First():
    def __init__(self, a, b):
        self._a = a
        self._b = b


class Second(First):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self._c = c


class Third(Second):
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c)
        self._d = d
