# Задание 2 (I). Написать функцию, которая возвращает среднее геометрическое для чисел a и b (не
#использовать модуль math). Выполните обработку исключений при помощи try-except.


from math import sqrt


def geometric_mean(a, b):
    try:
        mult = a * b
        res = sqrt(mult)
        return f"The geometric mean of the numbers is {res}"
    except ValueError as exc:
        return f"Multiplication of the numbers under the square root must be positive! The error is {exc}"


print(geometric_mean(-2, 8))

