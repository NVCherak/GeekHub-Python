"""№1. (таких ф-цій потрібно написати 3 -> різними варіантами) Написати функцію season,
приймаючу 1 аргумент — номер місяця (від 1 до 12), яка буде повертати пору року,
якій цей місяць належить (зима, весна, літо або осінь). """

def season_1(num):
    if num > 0:
        if num <= 2 or num == 12:
            return "Winter"
        elif num <= 5:
            return "Spring"
        elif num <= 8:
            return "Summer"
        elif num <= 11:
            return "Fall"
        else:
            return "This month don`t exist!"
    else:
        return "This month don`t exist!"

#season_1(9) -> Fall

def season_2(num):
    if num in range(1, 3) or num == 12:
        return "Winter"
    elif num in range(3, 6):
        return "Spring"
    elif num in range(6, 9):
        return "Summer"
    elif num in range(9, 12):
        return "Fall"
    else:
        return "This month don`t exist!"

#season_2(0) -> This month don`t exist!

def season_3(num):
    return {
        1: "Winter",
        2: "Winter",
        3: "Spring",
        4: "Spring",
        5: "Spring",
        6: "Summer",
        7: "Summer",
        8: "Summer",
        9: "Fall",
        10: "Fall",
        11: "Fall",
        12: "Winter"
    }.get(num, "This month don`t exist!")

#season_3(5) -> Spring

"""№2. Написати функцію, яка буде приймати декілька значень, одне з яких значення
за замовченням(повинна бути перевірка на наявність), і у випадку якщо воно є додати його
до іншого агрументу, якщо немає - придумайте логіку що робити программі."""

def func(first, second, third = None):
    if not third:
        return first + second
    else:
        return first + second + third

#func(5, 12) -> 17
#func(7, 3, 7) -> 17

"""№3. Створіть 3 різних функції(на ваш вибір), кожна з цих функцій повинна повертати якийсь результат.
Також створіть четверу ф-цію, яка в тілі викликає 3 попередніб обробляє повернутий ними результат
та також повертає результат. Таким чином ми будемо викликати 1 функцію, а вона в своєму тілі ще 3"""

from math import sqrt
#Імпортуємо функцію обрахунку кореня

def incomplit(a, b, c):
#Види неповних квадратних рівнянь та їх розв'язання
        if b == 0 and c == 0:
        #якщо b = 0, c = 0
            return 0
        if b != 0 and c == 0:
        # якщо b не= 0, c = 0
            return (0, -b / a)
        if b == 0 and c != 0:
        #якщо b = 0, c не= 0
            if (-c / a) > 0:
                return (sqtr(-c / a), -(sqrt(-c / a))) #x1, x2
            else:
                return "no root"

def D(a, b, c):
#Дискримінант
    d = b*b-4*a*c
    if d > 0:
        return ((-b+sqrt(d))/(2*a), (-b-sqrt(d))/(2*a)) #x1, x2
    elif d == 0:
        return -b/(2*a)
    else:
        return "no root"

def D2(a, b, c):
#Дискримінант із парним другим коефіцієнтом(b)
    d = pow((b/2), 2)-a*c
    if d >= 0:
        return ((-b/2+sqrt(d))/a, (-b/2-sqrt(d))/a) #x1, x2
    else:
        return "no root"

def quad_equation(a, b, c):
#Вирішення квадратного рівняння
    if b == 0 or c == 0:
        return incomplit(a, b, c)
    elif b%2 == 0:
        return D2(a, b, c)
    else:
        return D(a, b, c)

#quad_equation(1, -26, 120) -> (20.0, 6.0)
#quad_equation(1, 3, 10) -> no root
#quad_equation(9, -12, 4) -> (0.66, 0.66)

"""№4. Створіть 2 змінні x та y з довільними значеннями;
Створіть просту умовну конструкцію(звісно вона повинна бути в тілі ф-ції),
під час виконання якої буде перевірятися рівність змінних x та y.
Удоскональте конструкцію та додайте відповідні умови, які б при нерівності змінних
х та у відповідь повертали різницю чисел.
Повинні опрацювати такі умови:
x > y; відповідь - х більше ніж у на z
x < y; відповідь - у більше ніж х на z
x==y. відповідь - х дорівнює z"""

import random

x = random.randint(0, 10)
y = random.randint(0, 10)

def equality(x, y):
    if x > y:
        return str(x) + " більше ніж " + str(y) + " на " + str(x-y)
    elif x < y:
        return str(y) + " більше ніж " + str(x) + " на " + str(y-x)
    else:
        return str(x) + " дорівнює " + str(y)

#equality(10, 10) -> 10 дорівнює 10
#equality(9, 7) -> 9 більше ніж 7 на 2

"""№5. маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345"
-> просто потицяв по клаві
створюєте ф-цію яка буде отримувати рядки на зразок мого, яка працює в 4 випадках:
якщо довжина рядка в дфапазоні 30-50 -> прінтує довжину, кількість букв та цифр
якщо довжина менше 30 -> прінтує суму всіх чисел та окремо рядок без цифр лише з буквами
якщо довжина бульше 50 - > ваша фантазія
звiсно 4 все інше"""

def for_string(string):
    if len(string) in range(30, 50):
        #якщо довжина рядка в дiапазоні 30-50
        digits = 0
        letters = 0
        for i in string:
            if i.isalpha():
                letters += 1
            elif i.isnumeric():
                digits += 1
        print(len(string), digits, letters)
        #виводить довжину, кількість букв та цифр
    elif len(string) < 30:
        #якщо довжина менше 30
        sumDigits = 0
        str_letters = ""
        for i in string:
            if i.isnumeric():
                sumDigits += int(i)
            if i.isalpha():
                str_letters += i
        print(sumDigits, str_letters)
        #виводить суму всіх чисел та рядок без цифр лише з буквами
    elif len(string) > 50:
        #якщо довжина бiльше 50
        str_digits = ""
        for i in string:
            if i.isnumeric():
                str_digits += i
        print(len(str_digits), str_digits)
        #виводить довжину рядка, що складається тільки з цифр та сам рядок

#Не бачу смислу писати else так, як він ніколи не виконається

#for_string(" 7 nc s  s ")
#for_string("f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345")
#for_string("")

"""№6. придумайте 3 різних ф-ції(немає різниці які)"""

""" 1 Функція, яка отримує порядковий номер простого числа і виводе його"""
# наприклад 3-е просте число це 5

def get_simple_num(n = 1):
    lstSimple = [2, ]
    # Список простих чисел
    number = 3
    while len(lstSimple) < n:
    # цикл який працює доки не знайдено потрібне за рахунком число
        for i in lstSimple:
            # ділимо поточне число на всі прості числа
            if number % i:
                # якщо не ділиться націло
                if i != lstSimple[-1]:
                    # а дільник не є останнім простим числом списку - продовжуємо
                    continue
                else:
                    # і всі прості числа перечислено - добавляємо поточне число до списку простих
                    lstSimple.append(number)
            else:
                break
        number += 1

    return lstSimple[n-1]
    # повертаємо n-е просте число

#get_simple_num(4) -> 7
#get_simple_num() -> 2
#get_simple_num(15) -> 47
#get_simple_num(2) -> 3

""" 2 Функція розкладання числа на прості множники"""

def simple_decomposition(number):
    multipliers = [] # Список множників
    simpl = 1        # яке за рахунком просте число
    while number != 1:
        # доки число не дорівнює 1
        if number % get_simple_num(simpl):
            # якщо число не ділиться націло на дане просте - беремо наступне
            simpl += 1
        else:
            # якщо ділиться націло - додаємо в список множників
            multipliers.append(get_simple_num(simpl))
            number /= get_simple_num(simpl)
            # і ділимо число на "множник"

        if number == get_simple_num(simpl):
            # якщо число, що ми розкладаємо дорівнює простому - додаємо в список множників
            multipliers.append(get_simple_num(simpl))
            # і виходимо з циклу
            break

    return multipliers

#simple_decomposition(280) -> [2, 2, 2, 5, 7]
#simple_decomposition(2100) -> [2, 2, 3, 5, 5, 7]
#simple_decomposition(12) -> [2, 2, 3]

""" 3 Функція знаходження найбільшого спільного дільника (НСД) двох чисел"""
# НСД - англ. LCD - the largest common divider

""" не дороблена(
def LCD(a, b):
    aLst = simple_decomposition(a)
    bLst = simple_decomposition(b)
    intersectionLst = []
    i, j = 0, 0

    while i < len(aLst):
        while j < len(bLst):
            if aLst[i] == bLst[j]:
                intersectionLst.append(aLst[i])
                j += 1
                i += 1
                continue
            else:
                i += 1
                continue

    print(intersectionLst)

LCD(12, 18)"""


"""№7. ну і традиційно -> калькулятор, повинна бути 1 ф-ція яка б приймала 3 аргументи - один з яких операція яку зробити! """

def calc(a, b, operation):
    # a - перший операнд ,b - другий операнд, operation - операція яку потрібно виконати
    if operation == "+":
        return a+b
    elif operation == "*":
        return a*b
    elif operation == "-":
        return a-b
    else:
        return a/b

#calc(5, 7, "+") -> 12
#calc(21, 9, "*") -> 189
