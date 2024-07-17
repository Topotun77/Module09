# Домашнее задание по теме "Генераторные сборки"
#
# Цель задания:
# Научиться создавать функции динамически в зависимости от заданных условий и параметров,
# используя различные подходы, такие как фабрики функций, лямбда-функции и вызываемые объекты.
#
# Задание:
# Задача 1: Фабрика Функций
# Написать функцию, которая возвращает различные математические функции (например, деление,
# умножение) в зависимости от переданных аргументов.
#
# Задача 2: Лямбда-Функции
# Использовать лямбда-функцию для реализации простой операции и написать такую же функцию
# с использованием def. Например, возведение числа в квадрат
#
# Задача 3: Вызываемые Объекты
# Создать класс с Rect c полями a, b которые задаются в __init__ и методом __call__,
# который возвращает площадь прямоугольника, то есть a*b.

# ============== Задача 1: Фабрика Функций ===================
def create_operation(operation):
    if operation == "+":
        def oper(x, y):
            return x + y

        return oper
    elif operation == "-":
        def oper(x, y):
            return x - y

        return oper
    elif operation == "*":
        def oper(x, y):
            return x * y

        return oper
    elif operation == "/":
        def oper(x, y):
            try:
                return x / y
            except ZeroDivisionError:
                return '\033[91mError: Division by zero\033[0m'

        return oper


print('\033[93mЗадача 1: Фабрика функций\033[0m')
my_func = create_operation("+")
print(my_func(4, 2))

my_func = create_operation("*")
print(my_func(1, 2))

my_func = create_operation("/")
print(my_func(1, 0))

# ========== Задача 2: Лямбда-Функции ==============
print('\n\033[93mЗадача 2 лямбда\033[0m')
multiply = lambda x: x ** 2
print(multiply(4))


def multiply_def(x):
    return x ** 2


print(multiply_def(4))


# ============== Задача 3: Вызываемые Объекты ================
class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b

    def get_side(self):
        return self.a, self.b


print('\n\033[93mЗадача 3: Вызываемые объекты\033[0m')
rect_ = Rect(2, 4)
print(f'Стороны: {rect_.get_side()}', f'Площадь: {rect_()}', sep='\n')

# print(help(rect_))

# Задача новая:
# Дано 2 списка:
# first = ['Strings', 'Student', 'Computers']
# second = ['Строка', 'Урбан', 'Компьютер']
# Необходимо создать 2 генераторных сборки:
# 1. В переменную first_result запишите генераторную сборку, которая высчитывает разницу длин строк
# из списков first и second, если их длины не равны. Для перебора строк попарно из двух списков
# используйте функцию zip.
# 2. В переменную second_result запишите генераторную сборку, которая содержит результаты сравнения
# строк в одинаковых позициях из списков first и second. Составьте эту сборку НЕ используя функцию
# zip. Используйте функции range и len.

print('\nНовая версия задания')

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(i[0]) - len(i[1]) for i in zip(first, second) if len(i[0]) != len(i[1]))
print(list(first_result))

second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))
print(list(second_result))