def modified_newtons_method(function, derivative, a, b, eps):
    x_0 = b
    while derivative(x_0) == 0:
        x_0 = (a - x_0) / 2

    x = x_0
    counter = 0

    while True:
        counter += 1

        x_next = x - (function(x) / derivative(x_0))

        if abs(x_next - x) < eps:
            last_length = abs(x_next - x)
            x = x_next
            break

        x = x_next

    return x_0, x, counter, last_length
