# Домашнее задание по теме "Списковые, словарные сборки"
# Задание
# Дан список целых чисел, примените функции map и filter так, чтобы в конечном списке оставить нечётные
# квадраты чисел

# Примечание
# Не забывайте, что встроенные функции map и filter возвращают генератор, сами операции преобразования
# не выполняются.

def sqr_(x):
    try:
        return x ** 2
    except TypeError:
        return f'Неверный тип аргумента функции ({type(x), x})'


def not_odd(x):
    try:
        return x % 2
    except TypeError:
        return 1


list_ = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
# list_ = [1, 2, 5, 7, [1, 2], 11, 35, 4, 89, 10]
# list_ = [1, 2, 5, 7, '12', 11, 35, 4, 89, 10]

res_1 = list(map(sqr_, filter(not_odd, list_)))
res_2 = list(filter(not_odd, map(sqr_, list_)))
print(res_1, res_2, sep='\n')

try:
    res_3 = list(filter(lambda x: x % 2, map(lambda x: x ** 2, list_)))
    l_sqr = lambda x: x ** 2
    res_4 = [l_sqr(x) for x in list_ if x % 2]
    print(res_3, res_4, sep='\n')
except TypeError as ex:
    print(f'Неверный тип данных, ожидался список из переменных типа int или float\n'
          f'{list_}\n{ex.args}')


# Новая версия задания
# 1. В переменную first_result запишите список созданный при помощи сборки состоящий из длин
# строк списка first_strings, при условии, что длина строк не менее 5 символов.
# 2. В переменную second_result запишите список созданный при помощи сборки состоящий из пар
# слов(кортежей) одинаковой длины. Каждое слово из списка first_strings должно сравниваться с
# каждым из second_strings. (два цикла)
# 3. В переменную third_result запишите словарь созданный при помощи сборки, где парой
# ключ-значение будет строка-длина строки. Значения строк будут перебираться из объединённых
# вместе списков first_strings и second_strings. Условие записи пары в словарь - чётная длина
# строки.

print('\nНовая версия задания')

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = list(map(lambda x: len(x), first_strings))
first_result2 = [len(x) for x in first_strings]

second_result = [(i, j) for i in first_strings for j in second_strings if len(i) == len(j)]

third_result = dict([(i, len(i)) for i in first_strings+second_strings if not (len(i) % 2)])

print(first_result, first_result2)
print(second_result)
print(third_result)
