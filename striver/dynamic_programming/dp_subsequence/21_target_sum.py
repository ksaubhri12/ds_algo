def target_sum_rec(arr: [], index, desired_sum) -> int:
    if index == 0:
        if arr[0] == abs(desired_sum):
            return 1
        else:
            return 0

    negative_sign = target_sum_rec(arr, index - 1, desired_sum + arr[index])

    positive_sign = target_sum_rec(arr, index - 1, desired_sum - arr[index])
    return negative_sign + positive_sign


def target_sum(arr: [], desired_sum) -> int:
    return target_sum_rec(arr, len(arr) - 1, desired_sum)


def target_sum_tab(arr: [], desired_sum) -> int:
    n = len(arr)
    total_sum = sum(arr)
    dp_arr = [[0 for _ in range(total_sum + 1)] for _ in range(n)]
    if arr[0] <= total_sum:
        dp_arr[0][arr[0]] = 1
    for index in range(1, n):
        for sum_value in range(total_sum + 1):
            curr_elem = arr[index]
            positive_sign = dp_arr[index - 1][abs(sum_value - arr[index])]
            negative_sign = 0
            if sum_value + curr_elem <= total_sum:
                negative_sign = dp_arr[index - 1][sum_value + arr[index]]
            dp_arr[index][sum_value] = negative_sign + positive_sign
    return dp_arr[n - 1][desired_sum]


if __name__ == '__main__':
    # print(target_sum([1, 2, 3, 1], 3))
    print(target_sum_tab([1, 2, 3, 1], 3))
