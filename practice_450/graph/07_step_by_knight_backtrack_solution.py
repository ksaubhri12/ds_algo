# ------------Back Tracking Solution -----------#
def knight_util(curr_row: int, curr_col: int, target_row: int, target_col: int, path_count: int,
                result_arr: [], max_row: int, max_col: int, visited: [[]]):
    if curr_row == target_row and curr_col == target_col:
        result_arr[0] = min(result_arr[0], path_count)
        return

    if curr_row < 0 or curr_row > max_row:
        return

    if curr_col < 0 or curr_col > max_col:
        return

    if visited[curr_row][curr_col]:
        return

    visited[curr_row][curr_col] = True
    move_x = [2, 2, 1, 1, -1, -1, -2, -2]
    move_y = [1, -1, 2, -2, 2, -2, 1, -1]

    for i in range(8):
        new_row = curr_row + move_y[i]
        new_col = curr_col + move_x[i]
        if is_safe(max_row, max_col, new_row, new_col, visited):
            knight_util(new_row, new_col, target_row, target_col, path_count + 1, result_arr, max_row, max_col,
                        visited)

    visited[curr_row][curr_col] = False


def is_safe(max_row: int, max_col: int, row: int, col: int, visited: []):
    if row < 0 or row > max_row:
        return False
    if col < 0 or col > max_col:
        return False
    if visited[row][col]:
        return False

    return True


def knight_min_step(source_pos, target_pos, n):
    visited = [[False] * n for i in range(n)]
    source_row = n - source_pos[1]
    source_col = source_pos[0] - 1
    target_row = n - target_pos[1]
    target_col = target_pos[0] - 1
    max_row = n - 1
    max_col = n - 1
    result_arr = [float('inf')]
    knight_util(source_row, source_col, target_row, target_col, 0, result_arr, max_row, max_col, visited)
    if result_arr[0] == float('inf'):
        return -1
    else:
        return result_arr[0]


# --------Back Track Solution Ends ---------


if __name__ == '__main__':
    print(knight_min_step([3, 4], [1, 4], 4))
