def find_derivative(n):
    coefficients = [1]

    for move in range(1, n + 1):
        previous_coefficients = coefficients.copy()
        previous_coefficients.append(0)
        coefficients = [0] * len(previous_coefficients)

        for degree in range(1, len(coefficients)):
            coefficients[degree - 1] += previous_coefficients[degree] * degree
            coefficients[degree] += previous_coefficients[degree - 1] * (-2)

    return coefficients


def find_chebyshev_hermite_polynomial(n):
    coefficients = find_derivative(n)

    def polynomial(x):
        result = 0
        for degree in range(len(coefficients)):
            result += coefficients[degree] * (x ** degree)
        return ((-1) ** n) * result

    return polynomial
