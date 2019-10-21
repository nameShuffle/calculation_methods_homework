def simpson(h, values, values_half_h):
    """
        Составная формула Симпона.
        :param h: шаг, с которым вычисляются равноотстоящие узлы
        :param values: значение в узлах z_k
        :param values_half_h: значение в узлах z_k + h/2
        :return: значение интеграла по составной формуле Симпсона
    """
    return h * (1 / 6 * values[0] + 1/6 * values[-1] + 1 / 3 * sum(values[1:-1]) + 4 / 6 * sum(values_half_h[:-1]))
