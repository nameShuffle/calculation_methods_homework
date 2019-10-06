def root_separation(function, a, b, n):
    h = abs(b - a) / n
    segments = []

    x_1 = a

    while True:
        x_2 = x_1 + h

        if x_2 > b:
            break

        if function(x_1) * function(x_2) < 0:
            segments.append([x_1, x_2])

        x_1 = x_2

    return segments
