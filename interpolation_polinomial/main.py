from math import sqrt
from interpolation_polinomial.lagrange_method import create_polynomial_lagrange_method
from interpolation_polinomial.newtons_method import create_separated_differences
from interpolation_polinomial.newtons_method import create_polynomial_newton_method


def func(x):
    return sqrt(1 + x*x)


def create_table(a, b, n, function):
    table = []
    m = n - 1

    for j in range(n):
        x = a + j * (b - a) / m
        table.append([x, function(x)])

    return table


def sort_table(table, x, n):
    def sort_key(element):
        return abs(element[0] - x)

    return sorted(table, key=sort_key)[:n]


def communication(a, b, function):
    while True:
        print("")
        print("Введите количество элементов в таблице:")
        number = int(input())

        m = number - 1
        table = create_table(a, b, number, function)
        print("Исходная таблица узлов:")
        for row in table:
            print(row)

        print("Введите степень интерполяционного многочлена <= ", m, ":")
        n = int(input())
        while n > m:
            print("Значение n должно быть меньше", m, "! Введите n повторно:")
            n = int(input())

        print("Введите точку интерполяции x:")
        x = float(input())

        print("Таблица с", n + 1, "ближайшими к точке ", x, " значениями:")
        newTable = sort_table(table, x, n + 1)
        for row in newTable:
            print(row)

        # Метод Ньютона
        print()
        print("МЕТОД НЬЮТОНА")
        print("Разделенные разности:")
        differences = create_separated_differences(newTable)
        for i in range(len(differences)):
            print(i + 1, " порядка: ", differences[i])
        p_newton = create_polynomial_newton_method(newTable, differences)
        result = p_newton(x)
        print("Ответ: ", result)
        print("Фактическая погрешность: ", abs(function(x) - result))

        # Метод Лагранжа
        print()
        print("МЕТОД ЛАГРАНЖА")
        p_lagrange = create_polynomial_lagrange_method(newTable)
        result = p_lagrange(x)
        print("Ответ: ", result)
        print("Фактическая погрешность: ", abs(function(x) - result))

        print("Продолжить? (y - да, n - нет)")
        answer = input()
        if answer == "n":
            break


if __name__ == "__main__":
    print()
    print("Лабораторная работа номер 1: 'ЗАДАЧА АЛГЕБРАИЧЕСКОГО ИНТЕРПОЛИРОВАНИЯ'")
    print("Вариант 4")
    print("Исходные данные:")
    print("     f(x) = sqrt(1 - x^2)")
    print("     [0; 0.7]")

    communication(0, 0.7, func)
