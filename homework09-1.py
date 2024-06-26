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