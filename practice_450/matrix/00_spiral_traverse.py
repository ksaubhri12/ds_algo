def spiral_traverse(matrix: [[int]], r, c):
    result_arr = []
    print_util(matrix, 0, 0, r - 1, c - 1, result_arr)
    return result_arr


def print_util(matrix_arr: [[int]], start_row, start_col, max_row, max_col, result_arr: []):
    if start_row > max_row:
        return
    if start_col > max_col:
        return

    for i in range(start_col, max_col + 1):
        result_arr.append(matrix_arr[start_row][i])

    for i in range(start_row + 1, max_row + 1):
        result_arr.append(matrix_arr[i][max_col])

    if max_row != start_row:
        for i in reversed(range(start_col, max_col)):
            result_arr.append(matrix_arr[max_row][i])

    for i in reversed(range(start_row + 1, max_row)):
        result_arr.append(matrix_arr[i][start_col])

    print_util(matrix_arr, start_row + 1, start_col + 1, max_row - 1, max_col - 1, result_arr)


if __name__ == '__main__':
    input_matrix = [
        [22, 3, 21, 2]
    ]

    print(spiral_traverse(input_matrix, 1, 4))

    input_matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]

    # print(spiral_traverse(input_matrix, 3, 4))

    input_matrix = [[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [13, 14, 15, 16]]
    # print(spiral_traverse(input_matrix, 4, 4))

    input_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ]

    # print(spiral_traverse(input_matrix, 4, 3))

    # print_util(input_matrix, 1, 1, 1, 2)
    # print_util(input_matrix, 2, 2, 0, )
# print_util(input_matrix, 2, 2, 2, 2)
