def flood_fill(image: [[]], source_row, source_col, new_color):
    initial_color = image[source_row][source_col]
    col_len = len(image[0])
    row_len = len(image)
    visited = [[False for _ in range(col_len)] for _ in range(row_len)]
    dfs_util(image, source_row, source_col, initial_color, new_color, col_len, row_len, visited)
    return image


def dfs_util(image: [[]], row, col, original_color, new_color, col_len, row_len, visited):
    if row < 0 or row >= row_len:
        return

    if col < 0 or col >= col_len:
        return

    if visited[row][col]:
        return

    if image[row][col] != original_color:
        return

    visited[row][col] = True
    image[row][col] = new_color

    neighbours_dir = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    for neighbour in neighbours_dir:
        dfs_util(image, row + neighbour[0], col + neighbour[1], original_color, new_color, col_len, row_len, visited)


if __name__ == '__main__':
    print(flood_fill([[1, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]], 1, 2, 2))
    print(flood_fill([[0, 1, 0], [0, 1, 0]], 0, 1, 0))
