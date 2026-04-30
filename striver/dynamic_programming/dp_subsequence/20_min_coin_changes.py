def min_coin_changes(coins: [], desired_sum: int) -> int:
    if desired_sum == 0:
        return 0
    n = len(coins)
    dp_arr = [[float("inf") for _ in range(desired_sum + 1)] for _ in range(n)]
    for sum_values in range(desired_sum + 1):
        coin_value = coins[0]
        if sum_values % coin_value == 0:  # if sum is divisible by the coin value
            dp_arr[0][sum_values] = int(sum_values / coin_value)
    for i in range(n):
        dp_arr[i][0] = 0

    for index in range(1, n):
        for sum_value in range(1, desired_sum + 1):
            non_pick = dp_arr[index - 1][sum_value]
            pick = float("inf")
            if coins[index] <= sum_value:
                pick = 1 + dp_arr[index][sum_value - coins[index]]
            dp_arr[index][sum_value] = min(pick, non_pick)
    if dp_arr[n - 1][desired_sum] == float("inf"):
        return -1
    else:
        return int(dp_arr[n - 1][desired_sum])


if __name__ == '__main__':
    # print(min_coin_changes([25, 10, 5], 30))
    # print(min_coin_changes([9, 6, 5, 1], 19))
    # print(min_coin_changes([5, 1], 0))
    # print(min_coin_changes([4, 6, 2], 5))
    print(min_coin_changes([2, 4, 17, 2, 1, 19], 39))
