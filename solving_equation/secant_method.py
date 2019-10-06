def secant_method(function, a, b, eps):
    x_previous = a
    x = b

    counter = 0

    while True:
        counter += 1

        x_next = x - function(x) * (x - x_previous) / (function(x) - function(x_previous))

        if abs(x_next - x) < eps:
            last_length = abs(x_next - x)
            x = x_next
            break

        x_previous = x
        x = x_next

    return x, counter, last_length
