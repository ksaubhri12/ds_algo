def min_path_tab(grid_arr: [[]]):
    row_len = len(grid_arr)
    col_len = len(grid_arr[0])
    dp_arr = [[-1 for _ in range(col_len)] for _ in range(row_len)]
    dp_arr[0][0] = grid_arr[0][0]
    for row in range(row_len):
        for col in range(col_len):
            if row == 0 and col == 0:
                continue
            from_right = float("inf")
            if col >= 1:
                from_right = dp_arr[row][col - 1]
            from_top = float("inf")
            if row >= 1:
                from_top = dp_arr[row - 1][col]

            dp_arr[row][col] = grid_arr[row][col] + min(from_right, from_top)

    return dp_arr[row_len - 1][col_len - 1]


if __name__ == '__main__':
    print(min_path_tab([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
