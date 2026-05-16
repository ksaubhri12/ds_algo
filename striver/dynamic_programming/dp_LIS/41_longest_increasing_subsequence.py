def lis_rec(arr, index, prev_index, dp_arr):
    if index == len(arr):
        return 0

    if dp_arr[index][prev_index] != -1:
        return dp_arr[index][prev_index]
    length = lis_rec(arr, index + 1, prev_index, dp_arr)
    if prev_index == -1 or arr[index] > arr[prev_index]:
        length = max(length, 1 + lis_rec(arr, index + 1, index, dp_arr))

    dp_arr[index][prev_index] = length
    return length


def lis(arr):
    n = len(arr)
    dp_arr = [[-1 for i in range(n)] for _ in range(n)]
    return lis_rec(arr, 0, -1, dp_arr)


def lis_tab(arr):
    n = len(arr)
    dp_arr = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for index in range(n - 1, -1, -1):
        for prev_index in range(index - 1, -2, -1):
            length = dp_arr[index + 1][prev_index + 1]
            if prev_index == -1 or arr[index] > arr[prev_index]:
                length = max(length, 1 + dp_arr[index + 1][index + 1])
            dp_arr[index][prev_index + 1] = length

    return dp_arr[0][0]


if __name__ == '__main__':
    print(lis([3, 10, 2, 1, 20]))
    print(lis([30, 20, 10]))
    print(lis([2, 2, 2]))
    print(lis([3, 4, 5, 1, 2, 3, 4]))
