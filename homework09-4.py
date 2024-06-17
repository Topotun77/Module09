# Домашнее задание по теме "Генераторы"
# Цель работы
# Более глубоко понять особенности работы с функциями генераторами и оператором yield
# в Python.
#
# Задание
# Напишите функцию-генератор all_variants, которая будет возвращать все подпоследовательности
# переданной строки. В функцию передаётся только сама строка.

def all_variants(str_):
    str_ = str(str_)
    for i in range(len(str_)):
        for j in range(len(str_) - i):
            yield str_[j:j + i + 1]


def all_variants_2(str_: str):
    try:
        for i in range(len(str_)):
            for j in range(i + 1, len(str_) + 1):
                yield str_[i:j]
    except TypeError:
        print(f'Неверный тип аргумента {str_, type(str_)}, требуется str')


print("all_variants('abc')")
a = all_variants('abc')
for i in a:
    print(i)

print('\nall_variants(1234)')
a = all_variants(1234)
for i in a:
    print(i)

print('\nall_variants([1, 2])')
a = all_variants([1, 2])
for i in a:
    print(i)

print("\nall_variants_2('abc')")
a = all_variants_2('abc')
for i in a:
    print(i)

print('\nall_variants_2(123)')
a = all_variants_2(123)
for i in a:
    print(i)

print('\nall_variants_2([1, 2, 3])')
a = all_variants_2([1, 2, 3])
for i in a:
    print(i)
