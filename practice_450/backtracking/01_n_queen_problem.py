def queen_path(board: [[]], n, row, result_arr: [[]]):
    if row == n:
        path = []
        for i in range(0, n):
            for j in range(0, n):
                if board[i][j] == 1:
                    path.append(j + 1)

        result_arr.append(path)
        return

    for i in range(0, n):
        if is_safe(board, row, i, n):
            board[row][i] = 1
            queen_path(board, n, row + 1, result_arr)
            board[row][i] = 0


def is_safe(board: [[]], row, col, n):
    for i in range(0, row):
        if board[i][col] == 1:
            return False

    cur_row = row - 1
    cur_col = col - 1

    while cur_col >= 0 and cur_row >= 0:
        if board[cur_row][cur_col] == 1:
            return False
        cur_row = cur_row - 1
        cur_col = cur_col - 1

    cur_row = row - 1
    cur_col = col + 1
    while cur_row >= 0 and cur_col < n:
        if board[cur_row][cur_col] == 1:
            return False
        cur_row = cur_row - 1
        cur_col = cur_col + 1

    return True


def queen_path_main(n):
    board_arr = [[0] * n for i in range(n)]
    result_arr = []
    queen_path(board_arr, n, 0, result_arr)
    return result_arr


if __name__ == '__main__':
    print(queen_path_main(4))
