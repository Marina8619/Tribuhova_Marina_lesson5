# Задание 5 (II) Реализуйте генератор, который будет генерировать числа Фибоначчи

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


g = fibonacci()
# for i in g:
#     print(i)

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
