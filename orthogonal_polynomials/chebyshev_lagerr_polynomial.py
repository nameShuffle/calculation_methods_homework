from math import exp


def find_chebyshev_hermite_polynomial(n, a):
    def polynomial(x):
        return ((-1) ** n) * (x ** (-a)) * ((-1) ** n)

    return polynomial

#((-1) ** n) * exp(x ** 2) * ((-1) ** n) * (2 ** n) * (x ** n) * exp(x ** (-2))