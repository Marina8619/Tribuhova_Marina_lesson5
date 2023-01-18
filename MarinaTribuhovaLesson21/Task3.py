# Задание 3 (I). Пусть есть 3 функции которые вызываются в следующей последовательности
# bzz -> bar -> foo. В функции foo() возникают исключения ZeroDivisionError и IndexError.
# Перехватите исключение ZeroDivisionError в функции bar, а IndexError в функции bzz.
# def foo(a):
# b = [1, 2, 3]
# x = 5 / a
# y = b[a]
# print(x, a, y)
# def bar(a):
# foo(a)
# def bzz(a):
# bar(a)


def foo(a):
    b = [1, 2, 3]
    x = 5 / a
    y = b[a]
    print(x, a, y)


def bar(a):
    try:
        foo(a)
    except ZeroDivisionError as exp:
        print(f"Division by zero is prohibited!!! The error is {exp}!")


def bzz(a):
    try:
        bar(a)
    except IndexError as exp:
        print(f"The index does not match the list!!! The error is {exp}!")


bzz(3)
bar(0)
foo(2)