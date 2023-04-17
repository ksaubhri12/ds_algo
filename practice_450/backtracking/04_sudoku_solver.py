def solve_sudoku_helper(grid: [[]], row: int, col: int):
    if row == 9:
        return True

    if col == 9:
        return solve_sudoku_helper(grid, row + 1, 0)

    if grid[row][col] != 0:
        return solve_sudoku_helper(grid, row, col + 1)

    for i in range(1, 10):
        if is_safe(grid, row, col, i):
            grid[row][col] = i
            if solve_sudoku_helper(grid, row, col + 1):
                return True

            grid[row][col] = 0

    return False


def is_safe(grid, row: int, col: int, number: int):
    for i in range(0, 9):
        if grid[row][i] == number:
            return False

    for i in range(0, 9):
        if grid[i][col] == number:
            return False

    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == number:
                return False

    return True


def solve_sudoku(grid: [[]]):
    return solve_sudoku_helper(grid, 0, 0)


def print_sudoku(grid: [[]]):
    solve_sudoku(grid)
    for i in range(0, 9):
        for j in range(0, 9):
            print(grid[i][j], end=' ')

        print()


if __name__ == '__main__':
    grid_arr = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
                [5, 2, 0, 0, 0, 0, 0, 0, 0],
                [0, 8, 7, 0, 0, 0, 0, 3, 1, ],
                [0, 0, 3, 0, 1, 0, 0, 8, 0],
                [9, 0, 0, 8, 6, 3, 0, 0, 5],
                [0, 5, 0, 0, 9, 0, 6, 0, 0],
                [1, 3, 0, 0, 0, 0, 2, 5, 0],
                [0, 0, 0, 0, 0, 0, 0, 7, 4],
                [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    print_sudoku(grid_arr)
