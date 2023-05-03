def rat_maze(maze_data: [[]], n):
    visited = [[False] * n for i in range(n)]
    result_arr = []
    if maze_data[n - 1][n - 1] == 0:
        return []
    rat_maze_util(maze_data, n - 1, n - 1, 0, 0, result_arr, visited, '')
    return result_arr


def rat_maze_util(maze_data: [[]], max_row: int, max_col: int, row: int, col: int, result_arr: [], visited: [[]],
                  path_string):
    if row < 0 or row > max_row:
        return

    if col < 0 or col > max_col:
        return

    if row == max_row and col == max_col:
        result_arr.append(path_string)
        return

    if visited[row][col] or maze_data[row][col] == 0:
        return

    visited[row][col] = True
    rat_maze_util(maze_data, max_row, max_col, row + 1, col, result_arr, visited, path_string + 'D')
    rat_maze_util(maze_data, max_row, max_col, row, col - 1, result_arr, visited, path_string + 'L')
    rat_maze_util(maze_data, max_row, max_col, row, col + 1, result_arr, visited, path_string + 'R')
    rat_maze_util(maze_data, max_row, max_col, row - 1, col, result_arr, visited, path_string + 'U')
    visited[row][col] = False


if __name__ == '__main__':
    maze_path_arr = [[1, 0, 0, 0],
                     [1, 1, 0, 1],
                     [1, 1, 0, 0],
                     [0, 1, 1, 1]]
    print(rat_maze(maze_path_arr, 4))
