def chocola_chocolate_problem(horizontal_cut: [], vertical_cut: []):
    horizontal_len = len(horizontal_cut)
    vertical_len = len(vertical_cut)
    horizontal_cut = sorted(horizontal_cut, reverse=True)
    vertical_cut = sorted(vertical_cut, reverse=True)
    horizontal_piece = 1
    vertical_piece = 1
    horizontal_pointer = 0
    vertical_pointer = 0

    cost = 0
    while horizontal_pointer < horizontal_len or vertical_pointer < vertical_len:
        if horizontal_pointer >= horizontal_len:
            horizontal_piece = horizontal_piece + 1
            cost = cost + vertical_cut[vertical_pointer] * vertical_piece
            vertical_pointer = vertical_pointer + 1

        elif vertical_pointer >= vertical_len:
            vertical_piece = vertical_piece + 1

            cost = cost + horizontal_cut[horizontal_pointer] * horizontal_piece
            horizontal_pointer = horizontal_pointer + 1

        elif horizontal_cut[horizontal_pointer] > vertical_cut[vertical_pointer]:
            vertical_piece = vertical_piece + 1

            cost = cost + horizontal_cut[horizontal_pointer] * horizontal_piece
            horizontal_pointer = horizontal_pointer + 1
        else:
            horizontal_piece = horizontal_piece + 1
            cost = cost + vertical_cut[vertical_pointer] * vertical_piece
            vertical_pointer = vertical_pointer + 1

    return cost


if __name__ == '__main__':
    print(chocola_chocolate_problem([2, 1, 3, 1, 4], [4, 1, 2]))
