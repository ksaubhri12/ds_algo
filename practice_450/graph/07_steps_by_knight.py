def shortest_path(source_pos, target_pos, n):
    board_arr = [[0] * n for i in range(n)]
    source_row = n - source_pos[1]
    source_col = source_pos[0] - 1
    target_row = n - target_pos[1]
    target_col = target_pos[0] - 1

    if source_row == target_row and source_col == target_col:
        return 0

    data_queue = [[source_row, source_col]]
    move_x = [2, 2, 1, 1, -1, -1, -2, -2]
    move_y = [1, -1, 2, -2, 2, -2, 1, -1]

    while len(data_queue) > 0:
        data = data_queue.pop(0)
        row = data[0]
        col = data[1]
        for i in range(8):
            new_row = row + move_y[i]
            new_col = col + move_x[i]
            if is_safe(board_arr, n, new_row, new_col, source_row, source_col):
                board_arr[new_row][new_col] = board_arr[row][col] + 1
                data_queue.append([new_row, new_col])

    return board_arr[target_row][target_col]


def is_safe(board_arr: [[]], n, row, col, source_row, source_col):
    if row == source_row and col == source_col:
        return False

    if row < 0 or row >= n:
        return False

    if col < 0 or col >= n:
        return False

    if board_arr[row][col] != 0:
        return False

    return True


if __name__ == '__main__':
    print(shortest_path([4, 5], [1, 1], 6))
