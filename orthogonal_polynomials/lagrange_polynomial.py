def find_lagrange_polynomial(n):
    def find_help(current_move, current_result, previous_result):
        if current_move > n:
            return current_result
        else:
            def new_result(x):
                return (2 * current_move - 1) / current_move * x * current_result(x) - (current_move - 1) / \
                       current_move * previous_result(x)

            return find_help(current_move + 1, new_result, current_result)

    def p_0(x):
        return 1

    def p_1(x):
        return x

    return find_help(2, p_1, p_0)
