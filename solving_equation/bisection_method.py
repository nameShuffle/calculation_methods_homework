def bisection_method(function, a, b, eps):
    x_1 = a
    x_2 = b
    c = (a + b) / 2

    double_eps = 2 * eps

    counter = 0

    while True:
        counter += 1

        if function(x_1) * function(c) < 0:
            x_2 = c
            c = (x_1 + x_2) / 2
        else:
            x_1 = c
            c = (x_1 + x_2) / 2

        if x_2 - x_1 < double_eps:
            last_length = abs(x_1 - x_2)
            break

    return c, counter, last_length
