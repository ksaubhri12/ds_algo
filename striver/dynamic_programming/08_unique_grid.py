def unique_grid(row_len, col_len):
    return unique_grid_rec_util(row_len - 1, col_len - 1)


def unique_grid_rec_util(right_index, down_index):
    if right_index < 0:
        return 0

    if down_index < 0:
        return 0

    if right_index == 0 and down_index == 0:
        return 0

    if right_index == 1 and down_index == 0:
        return 1

    if right_index == 0 and down_index == 1:
        return 1

    return unique_grid_rec_util(right_index - 1, down_index) + unique_grid_rec_util(right_index,
                                                                                    down_index - 1)


def unique_grid_mem(row_len, col_len):
    dp_arr = [[-1 for _ in range(col_len)] for _ in range(row_len)]
    return unique_grid_mem_util(col_len - 1, row_len - 1, dp_arr)


def unique_grid_mem_util(right_index, down_index, dp_arr):
    if dp_arr[down_index][right_index] != -1:
        return dp_arr[down_index][right_index]

    if right_index < 0:
        return 0
    if down_index < 0:
        return 0

    if right_index == 0 and down_index == 0:
        return 1

    if right_index == 1 and down_index == 0:
        return 1

    if right_index == 0 and down_index == 1:
        return 1

    unique_paths = unique_grid_mem_util(right_index - 1, down_index, dp_arr) + unique_grid_mem_util(right_index,
                                                                                                    down_index - 1,
                                                                                                    dp_arr)
    dp_arr[down_index][right_index] = unique_paths

    return dp_arr[down_index][right_index]


def unique_grid_tab(row_len, col_len):
    if row_len == 1 and col_len == 1:
        return 1
    dp_arr = [[-1 for _ in range(col_len)] for _ in range(row_len)]
    for i in range(row_len):
        dp_arr[i][0] = 1
    for i in range(col_len):
        dp_arr[0][i] = 1

    for i in range(1, row_len):
        for j in range(1, col_len):
            dp_arr[i][j] = dp_arr[i - 1][j] + dp_arr[i][j - 1]
    return dp_arr[row_len - 1][col_len - 1]


if __name__ == '__main__':
    print(unique_grid(2, 2))
    print(unique_grid(3, 1))
    print(unique_grid(3, 3))
    print(unique_grid(2, 3))
    print(unique_grid(1, 4))

    # Mem
    print("MEM Approach")
    print(unique_grid_mem(2, 2))
    print(unique_grid_mem(3, 1))
    print(unique_grid_mem(3, 3))
    print(unique_grid_mem(2, 3))
    print(unique_grid_mem(1, 4))

    # Tab
    print("Tab Approach")
    print(unique_grid_tab(2, 2))
    print(unique_grid_tab(3, 1))
    print(unique_grid_tab(3, 3))
    print(unique_grid_tab(2, 3))
    print(unique_grid_tab(1, 4))
