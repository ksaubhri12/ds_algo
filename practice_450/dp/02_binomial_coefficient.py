def binomial_coefficient(n, r):
    if r > n:
        return 0
    dp_arr = [0] * (r + 1)
    if n - r < r:
        r = n - r
    dp_arr[0] = 1
    mod = pow(10, 9) + 7
    for i in range(1, n + 1):
        for j in reversed(range(1, min(r, i) + 1)):
            if j > i:
                break
            if j == 0:
                dp_arr[j] = 1
            else:
                dp_arr[j] = (dp_arr[j] + dp_arr[j - 1]) % mod

    return dp_arr[r]


if __name__ == '__main__':
    # print(binomial_coefficient(3, 2))
    # print(binomial_coefficient(2, 4))
    # print(binomial_coefficient(5, 2))
    print(binomial_coefficient(6, 3))
    print(binomial_coefficient(69,43))
