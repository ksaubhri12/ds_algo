def edit_distance(str_1, str_2):
    n = len(str_1)
    m = len(str_2)
    dp_arr = [[0] * (m + 1) for a in range(n + 1)]
    for k in range(n + 1):
        dp_arr[k][0] = k
    for l in range(m + 1):
        dp_arr[0][l] = l

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str_1[i-1] == str_2[j-1]:
                dp_arr[i][j] = dp_arr[i - 1][j - 1]
            else:
                dp_arr[i][j] = 1 + min(dp_arr[i - 1][j], dp_arr[i][j - 1], dp_arr[i-1][j-1])

    return dp_arr[n][m]


if __name__ == '__main__':
    print(edit_distance("ABCAB", "EACB"))
