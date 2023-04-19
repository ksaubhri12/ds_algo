def celebrity_problem(mat: [[]], n):
    for member in range(0, n):
        is_member_celeb = True
        for other_member in range(0, n):
            if member == other_member:
                continue

            if mat[member][other_member] != 0 or mat[other_member][member] == 0:
                is_member_celeb = False
                break
        if is_member_celeb:
            return member

    return -1


def celebrity_problem_v2(mat: [[]], n):
    c = 0
    for i in range(1, n):
        if mat[c][i] == 1:
            c = i

    for i in range(0, n):
        if i != c and (mat[c][i] == 1 or mat[i][c] == 0):
            return -1

    return c


if __name__ == '__main__':
    input_arr = [[0, 1, 0],
                 [0, 0, 0],
                 [0, 1, 0]]
    print(celebrity_problem(input_arr, 3))
    print(celebrity_problem_v2(input_arr, 3))
    input_arr = [[0, 1],
                 [1, 0]]
    print(celebrity_problem(input_arr, 2))
    print(celebrity_problem_v2(input_arr, 2))
    input_arr = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]
    print(celebrity_problem(input_arr, 3))
    print(celebrity_problem_v2(input_arr, 3))
