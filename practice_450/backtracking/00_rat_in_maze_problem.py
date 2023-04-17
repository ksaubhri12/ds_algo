def path_finder_util(maze_arr: [[]], i, j, output_string: str, result_arr: [], n, prev_i, prev_j, visited_matrix: [[]]):
    if visited_matrix[i][j] == 1:
        return

    if maze_arr[i][j] == 0:
        return

    visited_matrix[i][j] = 1

    if i == n - 1 and j == n - 1:
        result_arr.append(output_string)

    left_move = maze_arr[i][j - 1] if j > 0 and (i != prev_i or j - 1 != prev_j) and maze_arr[i][j - 1] != 0 else None
    right_move = maze_arr[i][j + 1] if j < n - 1 and (i != prev_i or j + 1 != prev_j) and maze_arr[i][
        j + 1] != 0 else None
    up_move = maze_arr[i - 1][j] if i > 0 and (i - 1 != prev_i or j != prev_j) and maze_arr[i - 1][j] != 0 else None
    down_move = maze_arr[i + 1][j] if i < n - 1 and (i + 1 != prev_i or j != prev_j) and maze_arr[i + 1][
        j] != 0 else None

    if down_move is not None:
        path_finder_util(maze_arr, i + 1, j, output_string + 'D', result_arr, n, i, j, visited_matrix)
    if left_move is not None:
        path_finder_util(maze_arr, i, j - 1, output_string + 'L', result_arr, n, i, j, visited_matrix)
    if right_move is not None:
        path_finder_util(maze_arr, i, j + 1, output_string + 'R', result_arr, n, i, j, visited_matrix)
    if up_move is not None:
        path_finder_util(maze_arr, i - 1, j, output_string + 'U', result_arr, n, i, j, visited_matrix)

    visited_matrix[i][j] = 0
    return


def rat_in_maze(path_arr, n):
    result_arr = []
    visited_matrix = [[0] * n for i1 in range(n)]
    path_finder_util(path_arr, 0, 0, '', result_arr, n, None, None, visited_matrix)
    if len(result_arr) > 0:
        return result_arr
    else:
        return -1


if __name__ == '__main__':
    maze_path_arr = [[1, 0, 0, 0],
                     [1, 1, 0, 1],
                     [1, 1, 0, 0],
                     [0, 1, 1, 1]]

    print(rat_in_maze(maze_path_arr, 4))
