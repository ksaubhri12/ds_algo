def distinct_islands(matrix: [[]]):
    row_len = len(matrix)
    col_len = len(matrix[0])
    visited = [[False for _ in range(col_len)] for _ in range(row_len)]

    distinct_number = set()

    for row in range(row_len):
        for col in range(col_len):
            if matrix[row][col] == 1 and not visited[row][col]:
                count = dfs_util(row, col, row_len, col_len, visited, matrix, [[0, 0]])
                flatten_list = [str(item) for sublist in count for item in sublist]
                flatten_list_str = "+".join(flatten_list)
                distinct_number.add(flatten_list_str)

    return len(distinct_number)


def dfs_util(row, col, row_len, col_len, visited, matrix, dir):
    visited[row][col] = True

    neighbours_dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    for neighbour in neighbours_dir:
        new_row = row + neighbour[0]
        new_col = col + neighbour[1]

        if 0 <= new_row < row_len and 0 <= new_col < col_len:
            if not visited[new_row][new_col] and matrix[new_row][new_col] == 1:
                prev_dir = [dir[-1][0], dir[-1][1]]
                dir.append([prev_dir[0] + neighbour[0], prev_dir[1] + neighbour[1]])
                dfs_util(new_row, new_col, row_len, col_len, visited, matrix, dir)

    return dir


if __name__ == '__main__':
    print(distinct_islands([[1, 1, 0, 0, 0],
                            [1, 1, 0, 0, 0],
                            [0, 0, 0, 1, 1],
                            [0, 0, 0, 1, 1]]))

    print(distinct_islands([[1, 1, 0, 1, 1],
                            [1, 0, 0, 0, 0],
                            [0, 0, 0, 0, 1],
                            [1, 1, 0, 1, 1]]))
