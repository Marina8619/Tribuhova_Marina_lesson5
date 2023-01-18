# Задание 4 (II). Создайте консольную программу для доказательства гипотезы Гольдбаха
# (см. что это такое здесь). Программа принимает число для ввода и вывода результата. При вводе
# ‘q’ программа должна завершится.
# Input: 4
# Output: 2 2
# Input: 6
# Output: 3 3

from MarinaTribuhovaLesson21 import WrongTypeOfArgument


def check_numbers(num: int) -> bool:
    if not isinstance(num, int):
        raise WrongTypeOfArgument
    return num % 2 == 0


def proof_hypothesis(num: int) -> bool:
    if check_numbers(num):
        if num >= 4:
            return f"{str(int(num/2))} + {str(int(num/2))}"
        else:
            return f"With the number {num} the hypothesis is not proven!"
    else:
        return f"With the number {num} the hypothesis is not proven!"


while True:
    try:
        a = input("Enter the integer or press 'q' to exit!\n")
        if a == 'q':
            break
        else:
            print(proof_hypothesis(int(a)))
    except ValueError as exp:
        print(f"Be careful! You didn't enter a number! The error is {exp}!")

