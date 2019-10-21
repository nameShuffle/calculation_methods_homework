from math import sin, cos
from integral.rectangles import left_rectangles, right_rectangles, medium_rectangles
from integral.trapeze import trapeze
from integral.simpson import simpson


def f(x):
    return sin(x) - 2 * (x ** 2)


def w(x):
    return 1


def integral(x):
    return - cos(x) - 2 * (x ** 3) / 3


if __name__ == "__main__":
    print()
    print("Лабораторная работа номер 4: 'ПРИБЛИЖЕННОЕ ВЫЧИСЛЕНИЕ ИНТЕГРАЛА ПО СОСТАВНЫМ КВАДРАТУРНЫМ ФОРМУЛАМ'")
    print("Исходные параметры:")
    print("     f(x) = sin(x) - 2x^2")
    print()

    a = float(input("Введите значение A: "))
    b = float(input("Введите значение B: "))
    m = int(input("Введите число промежутков деления в составной КФ: "))

    j = integral(b) - integral(a)
    print("Точное значение интеграла по конечному промежутку [", a, ", ", b, "]: ", j)

    h = (b - a) / m

    z_points = []
    f_z_values = []
    f_z_plus_half_h_values = []
    for k in range(m + 1):
        z_k = a + k * h
        z_points.append(z_k)
        f_z_values.append(f(z_k))
        f_z_plus_half_h_values.append(f(z_k + h / 2))

    print()
    if m == 1:
        print("ФОРМУЛА ЛЕВОГО ПРЯМОУГОЛЬНИКА")
    else:
        print("СОСТАВНАЯ ФОРМУЛА ЛЕВЫХ ПРЯМОУГОЛЬНИКОВ")
    answer = left_rectangles(h, f_z_values)
    print("Ответ: ", answer)
    print("Абсолютная фактическая погрешность: ", abs(j - answer))

    print()
    if m == 1:
        print("ФОРМУЛА ПРАВОГО ПРЯМОУГОЛЬНИКА")
    else:
        print("СОСТАВНАЯ ФОРМУЛА ПРАВЫХ ПРЯМОУГОЛЬНИКОВ")
    answer = right_rectangles(h, f_z_values)
    print("Ответ: ", answer)
    print("Абсолютная фактическая погрешность: ", abs(j - answer))

    print()
    if m == 1:
        print("ФОРМУЛА СРЕДНЕГО ПРЯМОУГОЛЬНИКА")
    else:
        print("СОСТАВНАЯ ФОРМУЛА СРЕДНИХ ПРЯМОУГОЛЬНИКОВ")
    answer = medium_rectangles(h, f_z_plus_half_h_values)
    print("Ответ: ", answer)
    print("Абсолютная фактическая погрешность: ", abs(j - answer))

    print()
    if m == 1:
        print("ФОРМУЛА ТРАПЕЦИИ")
    else:
        print("СОСТАВНАЯ ФОРМУЛА ТРАПЕЦИЙ")
    answer = trapeze(h, f_z_values)
    print("Ответ: ", answer)
    print("Абсолютная фактическая погрешность: ", abs(j - answer))

    print()
    if m == 1:
        print("ФОРМУЛА СИМПСОНА")
    else:
        print("СОСТАВНАЯ ФОРМУЛА СИМПСОНА")
    answer = simpson(h, f_z_values, f_z_plus_half_h_values)
    print("Ответ: ", answer)
    print("Абсолютная фактическая погрешность: ", abs(j - answer))



