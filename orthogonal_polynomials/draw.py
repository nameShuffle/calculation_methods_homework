import matplotlib.pyplot as plt


def create_points(a, b, n, function):
    h = (b - a) / n
    point = a

    x_points = []
    y_points = []

    while point <= b:
        x_points.append(point)
        y_points.append(function(point))

        point += h

    return x_points, y_points


def draw_graph(x, y, name):
    plt.plot(x, y)
    plt.title(name)

    a_scale = float(max(x)) / float(100)

    for i in range(0, len(x) - 1):
        plt.arrow(x[i], y[i], (x[i + 1] - x[i]), (y[i + 1] - y[i]), head_width=a_scale,
                  color='g', length_includes_head=True)

    plt.show()
