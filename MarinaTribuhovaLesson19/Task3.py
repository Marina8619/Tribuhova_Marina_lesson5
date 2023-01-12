# Задание 3 (II). Реализуйте свой класс Complex для комплексных чисел (см. Определение),
# аналогично встроенной реализации complex. Добавьте инициализатор класса, реализуйте
# основные математические операции, реализуйте операцию модуля (abs). Оба класса должны
# давать осмысленный вывод как при print, так и просто при вызове в ячейке

# complex_number = a + b*j, здесь j — мнимое число (sqrt (-1))

from dataclasses import dataclass


@dataclass
class Complex:
    real: (int, float)
    i: (int, float) = 0

    def __repr__(self):
        return f'({self.real}{"-" if self.i < 0 else "+"}{abs(self.i)}*j)'

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.i + other.i)
        raise NotImplementedError

    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real - other.real, self.i - other.i)
        raise NotImplementedError

    def __mul__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real * other.real - self.i * other.i, self.real * other.i + other.real * self.i)
        raise NotImplementedError

    def __truediv__(self, other):
        if isinstance(other, Complex):
            return Complex((self.real * other.real + self.i * other.i) / (other.real ** 2 + other.i ** 2), \
                   (other.real * self.i - self.real * other.i) / (other.real ** 2 + other.i ** 2))
        raise NotImplementedError


a = Complex(1.2, 3)
b = Complex(1.4, 4)
# сравниваю мой класс с функцией complex()
print(a+b)
print(complex(1.2, 3) + complex(1.4, 4))
print(a-b)
print(complex(1.2, 3) - complex(1.4, 4))
print(a*b)
print(complex(1.2, 3) * complex(1.4, 4))
print(a/b)
print(complex(1.2, 3) / complex(1.4, 4))

        