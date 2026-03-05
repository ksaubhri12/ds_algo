def triangle_rec_util(triangle_arr: [[]], row_index, col_index):
    if row_index == 0:
        return triangle_arr[0][0]

    from_top = float("inf")
    if row_index >= 1:
        valid_col_index_for_jump_max_value = row_index - 1
        if col_index <= valid_col_index_for_jump_max_value:
            from_top = triangle_rec_util(triangle_arr, row_index - 1, col_index)
    from_diagonal = float("inf")
    if col_index != 0:
        from_diagonal = triangle_rec_util(triangle_arr, row_index - 1, col_index - 1)

    min_path = triangle_arr[row_index][col_index] + min(from_top, from_diagonal)
    return min_path


def triangle_rec(triangle_arr: [[]]):
    rows = len(triangle_arr)
    last_row_len = len(triangle_arr[rows - 1])

    min_sum = float("inf")
    for last_index in range(last_row_len):
        path_value = triangle_rec_util(triangle_arr, rows - 1, last_index)
        min_sum = min(min_sum, path_value)
    return min_sum


def triangle_mem_util(triangle_arr: [[]], row_index, col_index, dp_arr):
    if row_index == 0:
        dp_arr[0][0] = triangle_arr[0][0]
        return triangle_arr[0][0]
    if dp_arr[row_index][col_index] != -1:
        return dp_arr[row_index][col_index]

    from_top = float("inf")
    if row_index >= 1:
        valid_col_index_for_jump_max_value = row_index - 1
        if col_index <= valid_col_index_for_jump_max_value:
            from_top = triangle_mem_util(triangle_arr, row_index - 1, col_index, dp_arr)
    from_diagonal = float("inf")
    if col_index != 0:
        from_diagonal = triangle_mem_util(triangle_arr, row_index - 1, col_index - 1, dp_arr)

    min_path = triangle_arr[row_index][col_index] + min(from_top, from_diagonal)
    dp_arr[row_index][col_index] = min_path
    return min_path


def triangle_mem(triangle_arr: [[]]):
    rows = len(triangle_arr)
    last_row_len = len(triangle_arr[rows - 1])
    dp_arr = [[-1 for _ in range(last_row_len)] for _ in range(rows)]
    min_sum = float("inf")
    for last_index in range(last_row_len):
        path_value = triangle_mem_util(triangle_arr, rows - 1, last_index, dp_arr)
        min_sum = min(min_sum, path_value)
    return min_sum


def triangle_tab(triangle_arr: [[]]):
    rows = len(triangle_arr)
    last_row_len = len(triangle_arr[rows - 1])
    dp_arr = [[-1 for _ in range(last_row_len)] for _ in range(rows)]
    dp_arr[0][0] = triangle_arr[0][0]
    for row in range(1, rows):
        for col in range(row + 1):
            from_top = float("inf")
            if row >= 1:
                valid_col_index_for_jump_max_value = row - 1
                if col <= valid_col_index_for_jump_max_value:
                    from_top = dp_arr[row - 1][col]
            from_diagonal = float("inf")
            if col != 0:
                from_diagonal = dp_arr[row - 1][col - 1]

            min_path = triangle_arr[row][col] + min(from_top, from_diagonal)
            dp_arr[row][col] = min_path
    min_path = min(dp_arr[rows - 1])
    return min_path


if __name__ == '__main__':
    print(triangle_rec([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
    print("MEM")
    print(triangle_mem([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
    print("TAB")
    print(triangle_tab([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
