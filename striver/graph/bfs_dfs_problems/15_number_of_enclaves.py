def number_of_enclaves(matrix: [[]]):
    row_len = len(matrix)
    col_len = len(matrix[0])

    visited = [[False for _ in range(col_len)] for _ in range(row_len)]
    row_boundaries = [0, row_len - 1]
    col_boundaries = [0, col_len - 1]

    for row_boundary in row_boundaries:
        for col in range(col_len):
            if matrix[row_boundary][col] == 1 and not visited[row_boundary][col]:
                dfs_util(row_boundary, col, row_len, col_len, visited, matrix)

    for col_boundary in col_boundaries:
        for row in range(row_len):
            if matrix[row][col_boundary] == 1 and not visited[row][col_boundary]:
                dfs_util(row, col_boundary, row_len, col_len, visited, matrix)

    count = 0
    for i in range(row_len):
        for j in range(col_len):
            if matrix[i][j] == 1 and not visited[i][j]:
                count += 1

    return count


def dfs_util(row, col, row_len, col_len, visited, matrix):
    visited[row][col] = True

    neighbours_dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for neighbour in neighbours_dir:
        new_row = row + neighbour[0]
        new_col = col + neighbour[1]

        if 0 <= new_row < row_len and 0 <= new_col < col_len:
            if not visited[new_row][new_col] and matrix[new_row][new_col] == 1:
                dfs_util(new_row, new_col, row_len, col_len, visited, matrix)


if __name__ == '__main__':
    print(number_of_enclaves([[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))
    print(number_of_enclaves(
        [[1, 1, 0, 0, 0, 1], [0, 1, 1, 0, 1, 0], [0, 0, 0, 1, 1, 0], [0, 0, 0, 1, 1, 0], [0, 1, 0, 1, 0, 0],
         [1, 1, 0, 0, 0, 1]]))
