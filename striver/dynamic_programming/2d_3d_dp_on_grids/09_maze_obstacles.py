def maze_obstacles_mem(maze_grid: [[]]):
    row_len = len(maze_grid)
    col_len = len(maze_grid[0])
    dp_arr = [[-1 for _ in range(col_len)] for _ in range(row_len)]
    if maze_grid[row_len - 1][col_len - 1] == 1:
        return 0
    return maze_obstacles_mem_util(maze_grid, col_len - 1, row_len - 1, dp_arr)


def maze_obstacles_mem_util(maze_grid: [[]], right_index: int, down_index: int, dp_arr):
    if right_index < 0:
        return 0
    if down_index < 0:
        return 0

    if dp_arr[down_index][right_index] != -1:
        return dp_arr[down_index][right_index]

    if right_index == 0 and down_index == 0:
        return 1 if maze_grid[right_index][down_index] != 1 else 0

    if right_index == 1 and down_index == 0:
        return 1 if maze_grid[down_index][right_index] != 1 else 0

    if right_index == 0 and down_index == 1:
        return 1 if maze_grid[down_index][right_index] != 1 else 0

    count = 0
    if down_index >= 1 and maze_grid[down_index - 1][right_index] != 1:
        count += maze_obstacles_mem_util(maze_grid, right_index, down_index - 1, dp_arr)
    if right_index >= 1 and maze_grid[down_index][right_index - 1] != 1:
        count += maze_obstacles_mem_util(maze_grid, right_index - 1, down_index, dp_arr)
    dp_arr[down_index][right_index] = count
    return count


def maze_obstacles_tab(maze_grid: [[]]):
    row_len = len(maze_grid)
    col_len = len(maze_grid[0])
    dp_arr = [[-1 for _ in range(col_len)] for _ in range(row_len)]

    if maze_grid[0][0] == 1:
        dp_arr[0][0] = 0
    else:
        dp_arr[0][0] = 1

    for row in range(0, row_len):
        for col in range(0, col_len):
            if row == 0 and col == 0:
                continue
            if maze_grid[row][col] == 1:
                dp_arr[row][col] = 0
            else:
                count = 0
                if row >= 1:
                    count += dp_arr[row - 1][col]
                if col >= 1:
                    count += dp_arr[row][col - 1]
                dp_arr[row][col] = count

    return dp_arr[row_len - 1][col_len - 1]


if __name__ == '__main__':
    print(maze_obstacles_mem([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    print(maze_obstacles_mem([[1, 0, 1]]))
    print("tab")
    print(maze_obstacles_tab([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    print(maze_obstacles_tab([[1, 0, 1]]))
