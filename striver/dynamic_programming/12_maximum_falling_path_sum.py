def max_falling_path_sum_tab(grid_arr: [[]]):
    row_len = len(grid_arr)
    col_len = len(grid_arr[0])

    dp_arr = [[[-1 for _ in range(col_len)] for _ in range(row_len)] for _ in range(col_len)]

    max_sum = float("-inf")
    for start_index in range(col_len):
        dp_arr[start_index][0][start_index] = grid_arr[0][start_index]
        for row in range(row_len):
            for col in range(col_len):
                if dp_arr[start_index][row][col] != -1:
                    continue

                got_break = False
                from_top = float("-inf")
                if row >= 1 and dp_arr[start_index][row - 1][col] != -1:
                    from_top = dp_arr[start_index][row - 1][col]
                    got_break = True

                from_right_diagonal = float("-inf")
                if row >= 1 and col + 1 < col_len and dp_arr[start_index][row - 1][col + 1] != -1:
                    from_right_diagonal = dp_arr[start_index][row - 1][col + 1]
                    got_break = True

                from_left_diagonal = float("-inf")
                if row >= 1 and col - 1 >= 0 and dp_arr[start_index][row - 1][col - 1] != -1:
                    from_left_diagonal = dp_arr[start_index][row - 1][col - 1]
                    got_break = True

                if got_break:
                    dp_arr[start_index][row][col] = grid_arr[row][col] + max(from_top, from_left_diagonal,
                                                                             from_right_diagonal)
        max_grid_sum = max(dp_arr[start_index][row_len - 1])
        max_sum = max(max_sum, max_grid_sum)

    return max_sum


def max_falling_path_sum_tab_optimized(grid_arr: [[]]):
    row_len = len(grid_arr)
    col_len = len(grid_arr[0])
    dp_arr = [[-1 for _ in range(col_len)] for _ in range(row_len)]
    for col in range(col_len):
        dp_arr[0][col] = grid_arr[0][col]

    for row in range(1, row_len):
        for col in range(col_len):
            if dp_arr[row][col] != -1:
                continue

            got_break = False
            from_top = float("-inf")
            if row >= 1 and dp_arr[row - 1][col] != -1:
                from_top = dp_arr[row - 1][col]
                got_break = True

            from_right_diagonal = float("-inf")
            if row >= 1 and col + 1 < col_len and dp_arr[row - 1][col + 1] != -1:
                from_right_diagonal = dp_arr[row - 1][col + 1]
                got_break = True

            from_left_diagonal = float("-inf")
            if row >= 1 and col - 1 >= 0 and dp_arr[row - 1][col - 1] != -1:
                from_left_diagonal = dp_arr[row - 1][col - 1]
                got_break = True

            if got_break:
                dp_arr[row][col] = grid_arr[row][col] + max(from_top, from_left_diagonal,
                                                            from_right_diagonal)

    return max(dp_arr[row_len - 1])


if __name__ == '__main__':
    print(max_falling_path_sum_tab([[3, 6, 1], [2, 3, 4], [5, 5, 1]]))
    print(max_falling_path_sum_tab([[2, 1, 1], [1, 2, 2]]))
    print(max_falling_path_sum_tab([[25]]))
    print("OPTIMISATION")
    print(max_falling_path_sum_tab_optimized([[3, 6, 1], [2, 3, 4], [5, 5, 1]]))
    print(max_falling_path_sum_tab_optimized([[2, 1, 1], [1, 2, 2]]))
    print(max_falling_path_sum_tab_optimized([[25]]))
