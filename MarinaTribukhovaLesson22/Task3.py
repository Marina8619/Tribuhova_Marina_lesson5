# Задание 3 (I). Реализуйте генератор, который будет бесконечно генерировать нечётные числа


def uneven_nums_generator(start):
    while True:
        if start % 2 != 0:
            yield start
        start += 1


g = uneven_nums_generator(5)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))