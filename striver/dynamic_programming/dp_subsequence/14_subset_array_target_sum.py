def is_sum_possible(arr: [], target: int) -> bool:
    n = len(arr)
    dp_arr = [[None for _ in range(target + 1)] for _ in range(n)]
    for i in range(n):
        dp_arr[i][0] = True
    if arr[0] <= target:
        dp_arr[0][arr[0]] = True

    for index in range(1, n):
        for target_index in range(1, target + 1):
            not_taken = bool(dp_arr[index - 1][target_index])
            taken = False
            if arr[index] <= target_index:
                taken = bool(dp_arr[index - 1][target_index - arr[index]])

            dp_arr[index][target_index] = (not_taken or taken)

    return bool(dp_arr[n - 1][target])


if __name__ == '__main__':
    # print(is_sum_possible([1, 2, 3, 3, 1], 4))
    print(is_sum_possible([6, 3, 7, 4, 1, 6, 4, 3, 7, 4], 4))
