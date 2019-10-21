import copy

from interpolation_polinomial.main import create_table, sort_table
from interpolation_polinomial.lagrange_method import create_polynomial_lagrange_method
from math import sqrt
from solving_equation.bisection_method import bisection_method
from solving_equation.root_separation import root_separation


def func(x):
    return sqrt(1 + x * x)


def find_x_to_sort(table, f):
    def sort_key(element):
        return element[1]
    new_table = sorted(table, key=sort_key)

    p_1 = new_table[0][0]
    p_2 = new_table[len(new_table) - 1][0]

    for i in range(len(new_table)):
        if f < new_table[i][1]:
            p_1 = new_table[i - 1][0]
            p_2 = new_table[i][0]
            break

    return (p_1 + p_2) / 2


def communication(a, b, function):
    while True:
        print()
        number = int(input("Введите количество элементов в таблице: "))

        m = number - 1
        table = create_table(a, b, number, function)
        print("Исходная таблица узлов:")
        for row in table:
            print(row)

        n = int(input("Введите степень интерполяционного многочлена <= " + str(m) + ": "))
        while n > m:
            n = int(input("Значение n должно быть меньше " +  str(m) + "! Введите n повторно: "))
        f = float(input("Введите значение F для задачи обратного интерполирования: "))
        reversed_table = copy.deepcopy(table)
        for row in reversed_table:
            row[0], row[1] = row[1], row[0]

        print()
        print("СПОСОБ 1")
        print("Перевернутая таблица с", n + 1, "ближайшими к точке ", f, " значениями:")
        sorted_table = sort_table(reversed_table, f, n + 1)
        for row in sorted_table:
            print(row)

        # Метод Лагранжа
        print()
        print("МЕТОД ЛАГРАНЖА")
        p_lagrange = create_polynomial_lagrange_method(sorted_table)
        result = p_lagrange(f)
        print("Ответ: ", result)
        print("Фактическая погрешность: ", abs(function(result) - f))

        print()
        print("СПОСОБ 2")
        x_s = find_x_to_sort(table, f)
        sorted_table = sort_table(table, x_s, n + 1)
        print("Отсортированная таблица: ")
        for row in sorted_table:
            print(row)
        p_lagrange = create_polynomial_lagrange_method(sorted_table)

        def function(arg):
            return p_lagrange(arg) - f

        segments = root_separation(function, a, b, 100)
        results = []
        print("Точность: 10e-12")
        for segment in segments:
            x, _, _ = bisection_method(function, *segment, 10e-12)

            results.append(x)

        for result in results:
            print("Ответ: ", result)
            print("Фактическая погрешность: ", abs(func(result) - f))

        print("Продолжить? (y - да, n - нет)")
        answer = input()
        if answer == "n":
            break


if __name__ == "__main__":
    print()
    print("Лабораторная работа номер 3.1: 'ЗАДАЧА ОБРАТНОГО ИНТЕРПОЛИРОВАНИЯ'")
    print("Вариант 4")
    print("Исходные данные:")
    print("     f(x) = sqrt(1 - x^2)")
    print("     [1; 2]")

    communication(1, 2, func)
