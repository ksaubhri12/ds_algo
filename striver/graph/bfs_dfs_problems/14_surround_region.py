def surround_region(matrix: [[]]):
    row_len = len(matrix)
    col_len = len(matrix[0])
    row_boundaries = [0, row_len - 1]
    col_boundaries = [0, col_len - 1]

    visited = [[False for _ in range(col_len)] for _ in range(row_len)]
    for row_boundary in row_boundaries:
        for col in range(col_len):
            if matrix[row_boundary][col] == "O":
                dfs_util(row_boundary, col, row_len, col_len, visited, matrix)

    for col_boundary in col_boundaries:
        for row in range(row_len):
            if matrix[row][col_boundary] == "O":
                dfs_util(row, col_boundary, row_len, col_len, visited, matrix)

    for row in range(row_len):
        for col in range(col_len):
            if matrix[row][col] == "O" and not visited[row][col]:
                matrix[row][col] = "X"

    return matrix


def dfs_util(row, col, row_len, col_len, visited, matrix: [[]]):
    visited[row][col] = True

    neighbours_dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for neighbour in neighbours_dir:
        new_row = row + neighbour[0]
        new_col = col + neighbour[1]

        if 0 <= new_row < row_len and 0 <= new_col < col_len:
            if matrix[new_row][new_col] == "O" and not visited[new_row][new_col]:
                dfs_util(new_row, new_col, row_len, col_len, visited, matrix)


if __name__ == '__main__':
    print(surround_region([['X', 'X', 'X', 'X'],
                           ['X', 'O', 'X', 'X'],
                           ['X', 'O', 'O', 'X'],
                           ['X', 'O', 'X', 'X'],
                           ['X', 'X', 'O', 'O']]))
