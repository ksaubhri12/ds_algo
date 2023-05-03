def flood_fill(input_grid, src_row: int, src_col: int, color: int):
    max_row = len(input_grid) - 1
    max_col = len(input_grid[0]) - 1
    flood_fill_algo(input_grid, max_row, max_col, color, src_row, src_col, input_grid[src_row][src_col])
    return input_grid


def flood_fill_algo(input_grid: [[]], max_row: int, max_col: int, color: int, row: int, col: int, src_color: int):
    if input_grid[row][col] != src_color:
        return

    input_grid[row][col] = color
    move_x = [1, -1, 0, 0]
    move_y = [0, 0, 1, -1]
    for i in range(4):
        new_row = row + move_y[i]
        new_col = col + move_x[i]
        if is_safe(new_row, new_col, max_row, max_col, input_grid, src_color, color):
            flood_fill_algo(input_grid, max_row, max_col, color, new_row, new_col, src_color)


def is_safe(row: int, col: int, max_row: int, max_col: int, input_grid: [[]], src_color: int, color: int):
    if row < 0 or row > max_row:
        return False

    if col < 0 or col > max_col:
        return False

    if input_grid[row][col] == color:
        return False

    if input_grid[row][col] != src_color:
        return False

    return True


if __name__ == '__main__':
    grid = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    print(flood_fill(grid, 1, 1, 2))
    grid = [[0, 0, 0], [0, 0, 0]]
    print(flood_fill(grid, 0, 0, 0))
