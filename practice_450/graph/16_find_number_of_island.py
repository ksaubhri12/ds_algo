def find_number_of_island(grid: [[]]):
    max_row = len(grid) - 1
    max_col = len(grid[0]) - 1
    visited = [[False] * (max_col + 1) for i in range(max_row + 1)]
    count = 0
    for i in range(max_row + 1):
        for j in range(max_col + 1):
            if not visited[i][j] and grid[i][j] == 1:
                count = count + 1
                dfs_util(i, j, max_row, max_col, visited, grid)

    return count


def dfs_util(row: int, col: int, max_row: int, max_col: int, visited: [], grid: [[]]):
    if visited[row][col]:
        return

    visited[row][col] = True

    move_x = [1, -1, 0, 0, 1, 1, -1, -1]
    move_y = [0, 0, 1, -1, 1, -1, 1, -1]
    for i in range(8):
        new_row = row + move_y[i]
        new_col = col + move_x[i]
        if is_safe(new_row, new_col, grid, max_row, max_col, visited):
            dfs_util(new_row, new_col, max_row, max_col, visited, grid)


def is_safe(row: int, col: int, grid: [[]], max_row: int, max_col: int, visited: [[]]):
    if row < 0 or row > max_row:
        return False

    if col < 0 or col > max_col:
        return False

    if visited[row][col]:
        return False

    if grid[row][col] == 0:
        return False

    return True


if __name__ == '__main__':
    mat = [[0, 1], [1, 0], [1, 1], [1, 0]]
    print(find_number_of_island(mat))

    mat = [[0, 1, 1, 1, 0, 0, 0], [0, 0, 1, 1, 0, 1, 0]]
    print(find_number_of_island(mat))
