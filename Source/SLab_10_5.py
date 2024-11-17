class NegativeNumberError(Exception):
    def __init__(self, message="Отрицательное число недопустимо"):
        super().__init__(message)

import math

def calculate_square_root(value):
    if value < 0:
        raise NegativeNumberError("Ошибка: Нельзя вычислить квадратный корень из отрицательного числа.")
    return math.sqrt(value)

def subtract(a, b):
    result = a - b
    if result < 0:
        raise NegativeNumberError("Ошибка: Результат вычитания не может быть отрицательным.")
    return result

try:
    print("Вычисление квадратного корня из 9:")
    print(calculate_square_root(9))

    print("\nВычисление квадратного корня из -4:")
    print(calculate_square_root(-4))

except NegativeNumberError as e:
    print(e)

print("\n---\n")

try:
    print("Вычитание 5 - 3:")
    print(subtract(5, 3))

    print("\nВычитание 3 - 5:")
    print(subtract(3, 5))

except NegativeNumberError as e:
    print(e)