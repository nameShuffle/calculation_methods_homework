def find_chebyshev_polynomial(n):
    def find_help(current_move, current_result, previous_result):
        if current_move > n:
            return current_result
        else:
            def new_result(x):
                return 2 * x * current_result(x) - previous_result(x)

            return find_help(current_move + 1, new_result, current_result)

    def t_0(x):
        return 1

    def t_1(x):
        return x

    return find_help(2, t_1, t_0)
