import math


def count_squares(N):
    square_root = int(math.sqrt(N))
    if square_root * square_root == N:
        return square_root - 1
    else:
        return square_root


if __name__ == '__main__':
    print(count_squares(9))
    print(count_squares(27))
    print(count_squares(25))
    print(count_squares(30))
