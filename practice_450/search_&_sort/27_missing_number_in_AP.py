def in_sequence(A, B, C):
    if C == 0:
        if B == A:
            return 1
        else:
            return 0

    if C > 0 and B < A:
        return 0

    if C < 0 and B > A:
        return 0

    if (B - A) % C == 0:
        return 1
    else:
        return 0


if __name__ == '__main__':
    print(in_sequence(1, 3, 2))
