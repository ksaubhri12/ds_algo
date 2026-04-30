"""
This is similar to unbounded knapsack, we have price as the value arr
wt_arr would be range(1,n+1) and capacity will be n
n here is the length of the rod
"""


def knapsack_problem_tab(value_arr: [], wt_arr: [], target_weight: int) -> int:
    n = len(value_arr)
    dp_arr = [[0 for _ in range(target_weight + 1)] for _ in range(n)]
    for target in range(target_weight + 1):
        weight = wt_arr[0]
        if weight <= target:
            dp_arr[0][target] = int(target / weight) * value_arr[0]

    for index in range(1, n):
        for target in range(1, target_weight + 1):
            non_pick = dp_arr[index - 1][target]
            pick = float("-inf")
            if wt_arr[index] <= target:
                pick = value_arr[index] + dp_arr[index][target - wt_arr[index]]
            dp_arr[index][target] = max(pick, non_pick)
    return dp_arr[n - 1][target_weight]


def rod_cutting(price_arr: []) -> int:
    n = len(price_arr)
    wt_arr = range(1, n + 1)
    target = n
    return knapsack_problem_tab(price_arr, wt_arr, target)


if __name__ == '__main__':
    print(rod_cutting([1, 5, 8, 9, 10, 17, 17, 20]))
    print(rod_cutting([3, 5, 8, 9, 10, 17, 17, 20]))
    print(rod_cutting([3]))
