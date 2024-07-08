# Домашнее задание по теме "Создание функций на лету"
# Цель: освоить на практике замыкание, объекты-функторы и lambda-функции.
#
# Задача "Функциональное разнообразие":
# Lambda-функция:
# Даны 2 строки:
# first = 'Мама мыла раму'
# second = 'Рамена мало было'
# Необходимо составить lambda-функцию для следующего выражения - list(map(?, first, second)).
# Здесь ? - место написания lambda-функции.

print('\nЗадание №1')
first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x, y: x == y, first, second)))

# Напишите функцию get_advanced_writer(file_name), принимающую название файла для
# записи.
# Внутри этой функции, напишите ещё одну - write_everything(*data_set),
# где *data_set - параметр принимающий неограниченное количество данных любого типа.
# Логика write_everything заключается в добавлении в файл file_name всех данных
# из data_set в том же виде.
# Функция get_advanced_writer возвращает функцию write_everything.

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as fs:
            for ln in data_set:
                fs.write(str(ln)+'\n')

    return write_everything


print('\nЗадание №2')
file_ = 'example.txt'
write_fn = get_advanced_writer(file_)
write_fn('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
print(f'Создан файл {file_}')

with open(file_, 'r', encoding='utf-8') as fs:
    print(fs.read())

# Метод __call__:
# Создайте класс MysticBall, объекты которого обладают атрибутом words хранящий
# коллекцию строк.
# В этом классе также определите метод __call__ который будет случайным образом
# выбирать слово из words и возвращать его. Для случайного выбора с одинаковой
# вероятностью для каждого данного в коллекции можете использовать функцию choice
# из модуля random.

from random import choice

class MysticBall():
    def __init__(self, *words):
        self.words = tuple(words)

    def __call__(self, *args, **kwargs):
        return choice(self.words)


# Ваш класс здесь
print('\nЗадание №3')
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())