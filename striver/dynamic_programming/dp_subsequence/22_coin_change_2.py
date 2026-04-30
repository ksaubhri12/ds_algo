"""
Similar to min coin, here we have to consider both take and not take and then add them
"""


def all_coin_changes(coins: [], desired_sum: int) -> int:
    if desired_sum == 0:
        return 0
    n = len(coins)
    dp_arr = [[0 for _ in range(desired_sum + 1)] for _ in range(n)]
    for sum_values in range(desired_sum + 1):
        coin_value = coins[0]
        if sum_values % coin_value == 0:  # if sum is divisible by the coin value
            dp_arr[0][sum_values] = 1
    for i in range(n):
        dp_arr[i][0] = 1

    for index in range(1, n):
        for sum_value in range(1, desired_sum + 1):
            non_pick = dp_arr[index - 1][sum_value]
            pick = 0
            if coins[index] <= sum_value:
                pick = dp_arr[index][sum_value - coins[index]]
            dp_arr[index][sum_value] = pick + non_pick

    return int(dp_arr[n - 1][desired_sum])


if __name__ == '__main__':
    print(all_coin_changes([1, 2, 3], 4))
    print(all_coin_changes([2, 5, 3, 6], 10))
    print(all_coin_changes([5, 10], 3))
