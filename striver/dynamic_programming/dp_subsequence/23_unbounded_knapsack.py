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


if __name__ == '__main__':
    print(knapsack_problem_tab([1, 30], [1, 50], 100))
    print(knapsack_problem_tab([10, 40, 50, 70], [1, 3, 4, 5], 8))
