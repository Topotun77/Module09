# Домашнее задание по теме "Декораторы"
# Задание: Декораторы в Python
#
# Цель задания:
# Освоить механизмы создания декораторов Python.
# Практически применить знания, создав функцию декоратор и обернув ею другую функцию.
#
# Задание:
# Напишите 2 функции:
# Функция, которая складывает 3 числа (sum_three)
# Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой
# функции будет простым числом и "Составное" в противном случае.

class ArgumCount(Exception):
    def __init__(self, message='Неверное число аргументов', add_info=None):
        self.message = message
        self.add_info = add_info

    def __str__(self):
        return (f'{self.message}\n\tБыли переданы аргументы: {self.add_info}')


def sum_three(*args):
    if len(args) != 3:
        raise ArgumCount(f'Требуется 3 аргумента. В функцию было передано {len(args)}', tuple(args))
    return sum(args)


def func_dec(func):
    def is_prime(*args):
        from math import sqrt
        try:
            num_ = func(*args)
        except ValueError:
            raise
        for i in range(2, int(sqrt(num_))):
            if not num_ % i:
                return 'Составное', num_
        return 'Простое', num_

    return is_prime


sum_three = func_dec(sum_three)
list_ = [[2, 3, 6], [3, 3, 6], [2, 3, 6, 9]]

for l in list_:
    try:
        result = sum_three(*l)
    except ArgumCount as ex:
        print('\033[91m' + str(ex) + '\033[0m', end='\n\n')
    else:
        print(f'Результат суммы чисел {l}: ', *result, sep='\n', end='\n\n')
