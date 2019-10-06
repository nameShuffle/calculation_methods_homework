from interpolation_polinomial.main import communication
from math import sqrt


def func(x):
    return sqrt(1 + x * x)


if __name__ == "__main__":
    print()
    print("Лабораторная работа номер 3.1: 'ЗАДАЧА ОБРАТНОГО ИНТЕРПОЛИРОВАНИЯ'")
    print("Вариант 4")
    print("Исходные данные:")
    print("     f(x) = sqrt(1 - x^2)")
    print("     [0; 0.7]")

    print()
    print("СПОСОБ 1")
    communication(0, 0.7, func, True)

    print()
    print("СПОСОБ 2")
