from math import cos, sin

from solving_equation.root_separation import root_separation
from solving_equation.bisection_method import bisection_method
from solving_equation.newtons_method import newtons_method
from solving_equation.modified_newtons_method import modified_newtons_method
from solving_equation.secant_method import secant_method


def find_roots(func, deriv, a, b, eps):
    print("Этап 1: Отделение корней")
    print("N: ")
    n = input()
    segments = root_separation(func, a, b, float(n))
    print("Отрезки перемены знака: ")
    for segment in segments:
        print("[", segment[0], ", ", segment[1], "]")
    print("Количество отрезков перемены знака: ", len(segments))
    print()

    print("Этап 2: Уточнение корней")
    print("Метод бисекции")
    for segment in segments:
        x, number_of_moves, length = bisection_method(func, segment[0], segment[1], eps)
        print("     Отрезок: [", segment[0], ", ", segment[1], "]")
        print("     Количество шагов: ", number_of_moves)
        print("     Приближенное решение: ", x)
        print("     Длина отрезка в последнем шаге", length)
        print("     Абсолютная величина невязки для найденного решения:", abs(func(x)))
        print()

    print("Метод Ньютона")
    for segment in segments:
        x_0, x, number_of_moves, length = newtons_method(func, deriv, segment[0], segment[1], eps)
        print("     Отрезок: [", segment[0], ", ", segment[1], "]")
        print("     Начальное приближение: ", x_0)
        print("     Количество шагов: ", number_of_moves)
        print("     Приближенное решение: ", x)
        print("     Длина отрезка в последнем шаге", length)
        print("     Абсолютная величина невязки для найденного решения:", abs(func(x)))
        print()

    print("Модифицированный метод Ньютона")
    for segment in segments:
        x_0, x, number_of_moves, length = modified_newtons_method(func, deriv, segment[0], segment[1], eps)
        print("     Отрезок: [", segment[0], ", ", segment[1], "]")
        print("     Начальное приближение: ", x_0)
        print("     Количество шагов: ", number_of_moves)
        print("     Приближенное решение: ", x)
        print("     Длина отрезка в последнем шаге", length)
        print("     Абсолютная величина невязки для найденного решения:", abs(func(x)))
        print()

    print("Метод секущих")
    for segment in segments:
        x, number_of_moves, length = secant_method(func, segment[0], segment[1], eps)
        print("     Отрезок: [", segment[0], ", ", segment[1], "]")
        print("     Количество шагов: ", number_of_moves)
        print("     Приближенное решение: ", x)
        print("     Длина отрезка в последнем шаге", length)
        print("     Абсолютная величина невязки для найденного решения:", abs(func(x)))
        print()


if __name__ == "__main__":
    print()
    print("Лабораторная работа номер 1: 'ЧИСЛЕННЫЕ МЕТОДЫ РЕШЕНИЯ НЕЛИНЕЙНЫХ УРАВНЕНИЙ'")
    print("Вариант 6")
    print("Исходные параметры:")
    print("     f(x) = 8*cos(x) - x - 6")
    print("     [-9, 1]")
    print("     Точность - 10^-7")
    print()

    def function(x):
        return 8 * cos(x) - x - 6

    def derivative(x):
        return - 8 * sin(x) - 1

    find_roots(function, derivative, -9.0, 1.0, 0.000000000001)
