# Задание 2 (I). Реализуйте класс Number, используя functools определите функции сравнения
# разных объектов данного класса

from functools import total_ordering


#реализую __eq__ и один из оставшихся методов, а остальные будут автоматически созданы декоратором:
@total_ordering
class Number:
    def __init__(self, value):
        self.value = value

    def __ge__(self, other):
        return self.value >= other.value

    def __eq__(self, other):
        return self.value == other.value


print(Number(100) > Number(88))
print(Number(66) < Number(110))
print(Number(105) >= Number(101))
print(Number(99) <= Number(9))
