# divide_conquer

def divide_conquer(problem, param1, param2, ...):
    # recusion terminator:
    if problem is None:
        # print_result
        return None

    # prepare data
    data = process_data(problem)
    subproblems = split_problem(problem, data)

    # conquer subproblem
    subresutl1 = self.divide_conquer(subproblems[0], p1, ...)
    subresutl2 = self.divide_conquer(subproblems[1], p1, ...)
    subresutl3 = self.divide_conquer(subproblems[2], p1, ...)
    ...

    # process and generate the final result
    result = process_result(subresutl1, ...)

    # revert the current level status