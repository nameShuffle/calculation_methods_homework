from math import exp


def func(x):
    return exp(6 * x)


def derivative(x):
    return 6 * exp(6 * x)


def derivative_2(x):
    return 36 * exp(6 * x)


def create_table(a, h, number, function):
    table = []

    for j in range(number):
        x = a + j * h
        table.append([x, function(x)])

    return table


def print_table(table):
    def create_string_row(row, column_width):
        string_row = "|"

        for i in range(len(row)):
            string_column = str(row[i])

            for _ in range(column_width[i] - len(str(row[i]))):
                string_column += " "

            string_row += (" " + string_column + " |")

        return string_row

    columns = zip(*table)
    column_width = [max(len(str(x)) for x in column) for column in columns]
    pred_last_column = max(len(str(row[-2])) for row in table[1:-1])
    column_width.append(pred_last_column)
    last_column = max(len(str(row[-1])) for row in table[1:-1])
    column_width.append(last_column)

    name = ["x", "f(x)", "f'(x)", "|f'(x)чд - f'(x)р|", "f''(x)", "|f''(x)чд - f''(x)р|"]
    print()
    print(create_string_row(name, column_width))

    for row in table:
        print()
        print(create_string_row(row, column_width))


if __name__ == "__main__":
    print()
    print("Лабораторная работа номер 3.2: 'ФОРМУЛЫ ЧИСЛЕННОГО ДИФФЕРЕНЦИРОВАНИЯ'")
    print("Вариант 4")
    print("Исходные данные:")
    print("     f(x) = e^(6 * x)")

    while True:
        print()
        a = float(input("Введите начальную точку a: "))

        m_plus_1 = int(input("Введите количество точек в таблице (>=3): "))
        while m_plus_1 < 3:
            m_plus_1 = int(input("Введите значение >= 3"))
        m = m_plus_1 - 1

        h = float(input("Введите шаг h: "))

        table = create_table(a, h, m_plus_1, func)

        for i in range(len(table)):
            if i == 0:
                f_1 = (-3 * table[i][1] + 4 * table[i + 1][1] - table[i + 2][1]) / (2 * h)

                table[i].append(f_1)
                table[i].append(abs(f_1 - derivative(table[i][0])))
            elif i == m:
                f_1 = (3 * table[i][1] - 4 * table[i - 1][1] + table[i - 2][1]) / (2 * h)

                table[i].append(f_1)
                table[i].append(abs(f_1 - derivative(table[i][0])))
            else:
                f_1 = (table[i + 1][1] - table[i - 1][1]) / (2 * h)
                f_2 = (table[i + 1][1] - 2 * table[i][1] + table[i - 1][1]) / (h * h)

                table[i].append(f_1)
                table[i].append(abs(f_1 - derivative(table[i][0])))

                table[i].append(f_2)
                table[i].append(abs(f_2 - derivative_2(table[i][0])))

        print()
        print_table(table)

        answer = input("Продолжить? (y - да, n - нет) ")
        if answer == 'n':
            break
