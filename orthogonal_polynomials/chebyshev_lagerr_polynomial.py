a = 1


def find_derivative(n):
    coefficients = [0] * (n + a)
    coefficients.append(1)

    for move in range(1, n + 1):
        previous_coefficients = coefficients.copy()
        previous_coefficients.append(0)
        coefficients = [0] * len(previous_coefficients)

        for degree in range(len(coefficients)):
            if degree != 0:
                coefficients[degree - 1] += previous_coefficients[degree] * degree
            coefficients[degree] += previous_coefficients[degree] * (-1)

    for i in range(n + 1):
        coefficients[i] = coefficients[i + a]

    coefficients = coefficients[:n + 1]

    return coefficients


def find_chebyshev_lagerr_polynomial(n):
    coefficients = find_derivative(n)

    def polynomial(x):
        result = 0
        for degree in range(len(coefficients)):
            result += coefficients[degree] * (x ** degree)
        return ((-1) ** n) * result

    return polynomial
