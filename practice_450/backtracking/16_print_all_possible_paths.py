def print_all_possible_paths(max_row: int, max_col: int):
    result_arr = []
    path_arr = [1]
    visited_arr = [[0] * (max_col + 1) for i in range(max_row + 1)]
    print_all_possible_paths_helper(max_row, max_col, 0, 0, result_arr, path_arr, visited_arr)
    return result_arr


def print_all_possible_paths_helper(max_row: int, max_col: int, row: int, col: int, result_arr: [], path_arr: [],
                                    visited_arr: [[]]):
    if row < 0 or row > max_row:
        return

    if col < 0 or col > max_col:
        return

    if row == max_row and col == max_col:
        result_arr.append(path_arr.copy())

    move_x = [0, 1]
    move_y = [1, 0]
    for i in range(2):
        new_row = row + move_y[i]
        new_col = col + move_x[i]
        if is_safe(visited_arr, new_row, new_col, max_row, max_col):
            visited_arr[new_row][new_col] = 1
            path_arr.append(new_row * (max_col + 1) + new_col + 1)
            print_all_possible_paths_helper(max_row, max_col, new_row, new_col, result_arr, path_arr, visited_arr)
            visited_arr[new_row][new_col] = 0
            path_arr.pop(-1)


def is_safe(visited_arr: [], row, col, max_row, max_col):
    if row < 0 or row > max_row:
        return False
    if col < 0 or col > max_col:
        return False
    if visited_arr[row][col] == 1:
        return False

    return True


if __name__ == '__main__':
    print(print_all_possible_paths(1, 1))
    print(print_all_possible_paths(1, 2))
