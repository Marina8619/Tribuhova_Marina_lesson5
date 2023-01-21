# Задание 4 (I). Реализуйте генератор show_letters(some_str: str), выводящий все символы
# строки на печать, но только в том случае, если они являются буквами (остальные игнорируются).


def str_generator(str_):
    for char in str_:
        if char.isalpha():
            yield char


g = str_generator("Hello 3232, I am 4563!!!Marina")
for i in g:
    print(i, end="")
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

