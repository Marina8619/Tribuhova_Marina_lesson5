#Задание 2 (I). Реализуйте класс-итератор EvenRange, который принимает начало и конец
# интервала в качестве аргументов __init__ и дает только чётные числа во время итерации. Если
# пользователь пытается итерироваться после того, как он дал все возможные числа, должно быть
# напечатано Out of numbers! Примечание: Не используйте функцию range()


class EvenRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.count = 0

    def __next__(self):
        if self.start <= self.end:
            if self.start % 2 == 0:
                print(f"{self.start}")
                self.start += 2
            else:
                self.start += 1
        else:
            raise StopIteration("Out of numbers!")

    def __iter__(self):
        return self


l = EvenRange(7, 17)
# for i in l:
#     i
next(l)
next(l)
next(l)
next(l)
next(l)
next(l)
next(l)



