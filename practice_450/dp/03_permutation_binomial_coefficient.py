def permutation(n, r):
    if r > n:
        return 0
    dp_arr = [0] * r
    dp_arr[0] = n

    for i in range(1, r):
        dp_arr[i] = (n - i) * dp_arr[i - 1]

    return dp_arr[r - 1]


if __name__ == '__main__':
    print(permutation(5, 2))
