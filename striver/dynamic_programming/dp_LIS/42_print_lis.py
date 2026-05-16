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
    dp_arr = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for index in range(n - 1, -1, -1):
        for prev_index in range(index - 1, -2, -1):
            length = dp_arr[index + 1][prev_index + 1]
            if prev_index == -1 or arr[index] > arr[prev_index]:
                length = max(length, 1 + dp_arr[index + 1][index + 1])
            dp_arr[index][prev_index + 1] = length

    return dp_arr[0][0]


def lis_tab(arr):
    n = len(arr)
    dp_arr = [1 for _ in range(n)]  # 1D array of len n
    """
    Signifies lis at index i, this is what dp_arr is storing
    """

    for curr in range(1, n):
        longest = dp_arr[curr]
        for prev in range(curr):
            if arr[curr] > arr[prev]:
                longest = max(longest, 1 + dp_arr[prev])
        dp_arr[curr] = longest

    return max(dp_arr)


def print_lis(arr: []) -> []:
    n = len(arr)
    dp_arr = [1 for _ in range(n)]
    hash_arr = [i for i in range(n)]
    maxi_index = 0
    max_element = dp_arr[0]
    for curr in range(1, n):

        for prev in range(curr):
            if arr[curr] > arr[prev] and 1 + dp_arr[prev] > dp_arr[curr]:
                dp_arr[curr] = 1 + dp_arr[prev]
                hash_arr[curr] = prev

        if dp_arr[curr] > max_element:
            max_element = dp_arr[curr]
            maxi_index = curr

    lis_arr = [arr[maxi_index]]
    while True:
        prev_index = hash_arr[maxi_index]
        if prev_index < maxi_index:
            maxi_index = prev_index
            lis_arr.append(arr[prev_index])
        else:
            break

    return lis_arr[::-1]


if __name__ == '__main__':
    print(lis([3, 10, 2, 1, 20]))
    print(lis([30, 20, 10]))
    print(lis([2, 2, 2]))
    print(lis([3, 4, 5, 1, 2, 3, 4]))

    print("""----tab----""")
    print(lis_tab([3, 10, 2, 1, 20]))
    print(lis_tab([30, 20, 10]))
    print(lis_tab([2, 2, 2]))
    print(lis_tab([3, 4, 5, 1, 2, 3, 4]))

    print("----print_lis-----")
    print(print_lis([3, 10, 2, 1, 20]))
    print(print_lis([30, 20, 10]))
    print(print_lis([2, 2, 2]))
    print(print_lis([3, 4, 5, 1, 2, 3, 4]))
