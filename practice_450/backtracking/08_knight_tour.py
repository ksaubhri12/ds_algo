def knight_helper(board: [[]], row, col, value: int, max_number: int, board_size: int):
    if value == max_number:
        return True

    give_options = get_next_options(row, col)
    for option in give_options:
        if is_safe(board, option[0], option[1], board_size):
            board[option[0]][option[1]] = value + 1
            if knight_helper(board, option[0], option[1], value + 1, max_number, board_size):
                return True
            else:
                board[option[0]][option[1]] = -1


def get_next_options(row, col):
    option_1 = [row - 1, col + 2]
    option_2 = [row + 1, col + 2]
    option_3 = [row + 2, col - 1]
    option_4 = [row + 2, col + 1]
    option_5 = [row - 2, col + 1]
    option_6 = [row - 2, col - 1]
    option_7 = [row - 1, col - 2]
    option_8 = [row + 1, col - 2]
    return [option_1, option_2, option_3, option_4, option_5, option_6, option_7, option_8]


def is_safe(board, row, col, board_size):
    if 0 <= row < board_size and 0 <= col < board_size and board[row][col] == -1:
        return True
    return False


def print_knight_path(board_size: int):
    board = [[-1] * board_size for i in range(board_size)]
    max_number = board_size * board_size
    board[0][0] = 1
    ans = knight_helper(board, 0, 0, 1, max_number, board_size)
    if ans:
        for i in range(0, board_size):
            for j in range(0, board_size):
                print(board[i][j], end=' ')
            print()

    else:
        print('Does not exist')


if __name__ == '__main__':
    print_knight_path(5)
