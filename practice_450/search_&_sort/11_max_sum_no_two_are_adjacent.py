def max_sum_no_two_adjacent(arr: [], n):
    dp = [-1] * n
    return max_sum(arr, n - 1, dp)


def max_sum(arr: [], index: int, dp: []):
    if index <= -1:
        return 0

    if dp[index] != -1:
        return dp[index]

    option_1 = arr[index] + max_sum(arr, index - 2, dp)
    option_2 = max_sum(arr, index - 1, dp)
    dp[index] = max(option_2, option_1)
    return dp[index]


if __name__ == '__main__':
    print(max_sum_no_two_adjacent([5, 5, 10, 100, 10, 5], 6))
    print(max_sum_no_two_adjacent([1, 2, 3], 3))
