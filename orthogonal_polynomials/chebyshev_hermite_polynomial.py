from math import exp


def find_chebyshev_hermite_polynomial(n):
    def polynomial(x):
        return ((-1) ** n) * ((-1) ** n) * (2 ** n) * (x ** n)

    return polynomial

#((-1) ** n) * exp(x ** 2) * ((-1) ** n) * (2 ** n) * (x ** n) * exp(x ** (-2))