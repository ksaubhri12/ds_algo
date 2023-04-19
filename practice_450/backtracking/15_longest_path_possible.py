def path_traveler_helper(board: [[]], max_row, max_col, row, col, target_row, target_col, path_value, result_arr,
                         visited: []):
    if row < 0 or row > max_row:
        return
    if col < 0 or col > max_col:
        return

    if col == target_col and row == target_row:
        result_arr[0] = max(path_value, result_arr[0])
        return

    move_x = [1, -1, 0, 0]
    move_y = [0, 0, 1, -1]

    for i in range(4):
        new_row = row + move_y[i]
        new_col = col + move_x[i]
        if is_safe(max_row, max_col, new_row, new_col, board, visited):
            visited[new_row][new_col] = 1
            path_traveler_helper(board, max_row, max_col, new_row, new_col, target_row, target_col, path_value + 1,
                                 result_arr, visited)
            visited[new_row][new_col] = 0


def is_safe(max_row, max_col, row, col, board, visited):
    if row < 0 or row > max_row:
        return False

    if col < 0 or col > max_col:
        return False

    if board[row][col] == 0:
        return False

    if visited[row][col] == 1:
        return False

    return True


def longest_path(board: [[]], source_row, source_col, target_row, target_col, n, m):
    result_arr = [float('-inf')]
    visited = [[0] * n for i in range(m)]
    if board[source_row][source_col] == 0:
        return -1
    if board[target_row][target_col] == 0:
        return -1
    visited[source_row][source_col] = 1
    path_traveler_helper(board, m - 1, n - 1, source_row, source_col, target_row, target_col, 0, result_arr, visited)
    return result_arr[0]


if __name__ == '__main__':
    input_arr = [
        [1, 1, 0],
        [0, 1, 1],
        [1, 0, 1]
    ]
    print(longest_path(input_arr, 0, 0, 2, 2, 3, 3))

    input_arr = [
        [0, 1, 0],
        [0, 1, 1],
        [1, 0, 1]
    ]
    print(longest_path(input_arr, 0, 0, 2, 2, 3, 3))

    input_arr = [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ]
    print(longest_path(input_arr, 0, 0, 3, 3, 4, 4))

    input_arr = [
        [1, 1, 0]
        , [0, 1, 1]
        , [1, 1, 1]
        , [0, 1, 1]
    ]

    print(longest_path(input_arr, 1, 1, 2, 0, 3, 4))
