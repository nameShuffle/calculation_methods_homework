def create_polynomial_lagrange_method(table):
    def z(x, k):
        result = 1
        for j in range(len(table)):
            if j == k:
                continue

            result *= (x - table[j][0])

        return result

    def p_n(x):
        result = 0
        for k in range(len(table)):
            result += z(x, k) / z(table[k][0], k) * table[k][1]

        return result

    return p_n
