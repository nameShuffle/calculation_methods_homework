def create_separated_differences(table):
    differences = []
    new_row = []
    for j in range(len(table) - 1):
        new_row.append((table[j + 1][1] - table[j][1]) / (table[j + 1][0] - table[j][0]))
    differences.append(new_row)

    for i in range(len(table) - 2):
        new_row = []
        for j in range(len(differences[i]) - 1):
            new_row.append((differences[i][j + 1] - differences[i][j])/(table[i + j + 2][0] - table[j][0]))

        differences.append(new_row)

    return differences


def create_polynomial_newton_method(table, differences):
    def p_n(x):
        result = table[0][1]
        iter = 1

        for row in differences:
            addendum = row[0]
            for i in range(iter):
                addendum *= (x - table[i][0])

            iter += 1
            result += addendum

        return result

    return p_n
