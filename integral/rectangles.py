def left_rectangles(h, values):
    """
    Состовная формула левых прямоугольников.
    :param h: шаг, с которым вычислятся равноотстоящие узлы
    :param values: значение в узлах
    :return: значение интеграла по составной формуле левых прямоугольников
    """
    return h * sum(values[:-1])


def right_rectangles(h, values):
    """
    Сотавная формула правых прямоугольников.
    :param h: шаг, с которым вычисляются равноотстоящие узлы
    :param values: значение в узлах
    :return: значение интеграла по составной формуле правых прямоугольников
    """
    return h * sum(values[1:])


def medium_rectangles(h, values):
    """
    Составная формула средних прямоугольников.
    :param h: шаг, с которым вычисляются равноотстоящие узлы
    :param values: значение в узлах z_k
    :return: значение интеграла по составной формуле средних прямоугольников
    """
    return h * sum(values[:-1])
