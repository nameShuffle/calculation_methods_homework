from math import sin, cos, pi
from solving_equation.bisection_method import bisection_method
from solving_equation.root_separation import root_separation
from orthogonal_polynomials.lagrange_polynomial import find_lagrange_polynomial
from orthogonal_polynomials.сhebyshev_polynomial import find_chebyshev_polynomial
from orthogonal_polynomials.chebyshev_hermite_polynomial import find_chebyshev_hermite_polynomial


if __name__ == "__main__":
    print()
    print("Лабораторная работа номер 5: 'КЛАССИЧЕСКИЕ ОРТОГОНАЛЬНЫЕ МНОГОЧЛЕНЫ'")

    n = int(input("Введите степень многочлена N: "))

    print()
    print("МНОГОЧЛЕН ЛАГРАНЖА")
    lagrange_polynomial = find_lagrange_polynomial(n)
    segments = root_separation(lagrange_polynomial, -1, 1, n)
    roots = []
    for segment in segments:
        x, number_of_moves, length = bisection_method(lagrange_polynomial, segment[0], segment[1], 0.00001)
        roots.append(x)
    print("Корни многочлена на отрезке [-1; 1]: ", roots)
    print("Проверка: ")
    print("P_", int(n), "(1) = ", lagrange_polynomial(1))
    print("P_", int(n), "(-1) = ", lagrange_polynomial(-1))

    print()
    print("МНОГОЧЛЕН ЧЕБЫШЕВА I РОДА")
    chebyshev_polynomial = find_chebyshev_polynomial(n)
    roots = []
    for k in range(n):
        roots.append(cos(2 * (k + 1) * pi / (2 * n)))
    extremum_points = []
    for l in range(n + 1):
        extremum_points.append(cos(pi * l / n))
    print("Корни многочлена: ", roots)
    print("Точки экстремума многочлена: ", extremum_points)
    print("Проверка:")
    for point in extremum_points:
        print("T_", n, "(", point, ") = ", chebyshev_polynomial(point))

    print()
    print("МНОГОЧЛЕН ЧЕБЫШЕВА-ЭРМИТА")
    chebyshev_hermite_polynomial = find_chebyshev_hermite_polynomial(n)
    segments = root_separation(chebyshev_hermite_polynomial, -5, 5, n)
    roots = []
    for segment in segments:
        x, number_of_moves, length = bisection_method(chebyshev_hermite_polynomial, segment[0], segment[1], 0.00001)
        roots.append(x)
    print("Корни многочлена на отрезке [-5; 5]: ", roots)
    print("Проверка: ")
    print("P_", int(n), "(1) = ", lagrange_polynomial(1))
    print("P_", int(n), "(-1) = ", lagrange_polynomial(-1))



