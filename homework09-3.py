# Домашнее задание по теме "Итераторы"
#
# Цель работы
# Применить dunder методы iter, next в своём классе
#
# Задание
# Напишите класс-итератор EvenNumbers для перебора чётных чисел в определённом числовом
# диапазоне. При создании и инициализации объекта этого класса создаются атрибуты:
# start – начальное значение (если значение не передано, то 0)
# end – конечное значение (если значение не передано, то 1)

class EvenNumbers:
    def __init__(self, start=0, end=1):
        if start > end:
            raise ValueError('Неверно переданные данные start > end')
        self.start, self.end = start, end

    def __iter__(self):
        self.i = self.start - 1
        return self

    def __next__(self):
        if self.i % 2:
            self.i += 1
        else:
            self.i += 2
        if self.i >= self.end:
            raise StopIteration
        return self.i


try:
    en = EvenNumbers(10, 25)
    for i in en:
        print(i)
except ValueError as ex:
    print(ex)
