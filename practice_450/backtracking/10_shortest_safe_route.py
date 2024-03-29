def path_helper(grid: [[]], row: int, col: int, row_max: int, col_max: int, path_length: int, result_arr: [],
                visited: [[]]):
    if grid[row][col] == 0:
        return

    if row < 0:
        return

    if col < 0:
        return

    if row > row_max:
        return
    if col > col_max:
        return

    if col == col_max:
        result_arr[0] = min(result_arr[0], path_length)
        return

    move_y = [1, -1, 0, 0]
    move_x = [0, 0, 1, -1]

    for i in range(4):
        if is_safe(grid, row + move_y[i], col + move_x[i], row_max, col_max, visited):
            visited[row + move_y[i]][col + move_x[i]] = 1
            path_helper(grid, row + move_y[i], col + move_x[i], row_max, col_max, path_length + 1, result_arr, visited)
            visited[row + move_y[i]][col + move_x[i]] = 0

    return


def is_safe(grid: [[]], row: int, col: int, row_max, col_max, visited: [[]]):

    if row < 0 or row > row_max:
        return False
    if col < 0 or col > col_max:
        return False

    if grid[row][col] == 0:
        return False

    if visited[row][col] == 1:
        return False

    move_y = [1, -1, 0, 0]
    move_x = [0, 0, 1, -1]
    for i in range(4):
        new_row = row + move_y[i]
        new_col = col + move_x[i]
        if 0 <= new_row <= row_max and 0 <= new_col <= col_max and grid[new_row][new_col] == 0:
            return False

    return True


def path_finder_main(input_grid: [[]], row_max, col_max):
    final_answer = float('inf')
    for row in range(0, row_max + 1):
        visited = [[0] * (col_max + 1) for i in range(row_max + 1)]
        starting_point = input_grid[row][0]
        if is_safe(input_grid, row, 0, row_max, col_max, visited):
            result_arr = [float('inf')]
            visited[row][0] = 1
            path_helper(input_grid, row, 0, row_max, col_max, 0, result_arr, visited)
            if len(result_arr) > 0:
                final_answer = min(final_answer, result_arr[0])

    return final_answer


if __name__ == '__main__':
    grid_arr = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1]
    ]
    print(path_finder_main(grid_arr, 11, 9))
