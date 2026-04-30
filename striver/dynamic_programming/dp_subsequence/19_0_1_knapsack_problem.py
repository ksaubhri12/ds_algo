def knapsack_problem(value_arr: [], wt_arr: [], target_weight: int) -> int:
    n = len(value_arr)
    return knapsack_problem_rec(n - 1, value_arr, wt_arr, target_weight)


def knapsack_problem_rec(index: int, value_arr: [], wt_arr: [], target: int) -> int:
    if target == 0:
        return 0
    if index == 0:
        if wt_arr[index] <= target:
            return value_arr[index]
        else:
            return 0
    non_pick = knapsack_problem_rec(index - 1, value_arr, wt_arr, target)
    pick = float("-inf")
    if wt_arr[index] <= target:
        pick = value_arr[index] + knapsack_problem_rec(index - 1, value_arr, wt_arr, target - wt_arr[index])
    return max(pick, non_pick)


def knapsack_problem_tab(value_arr: [], wt_arr: [], target_weight: int) -> int:
    n = len(value_arr)
    dp_arr = [[0 for _ in range(target_weight + 1)] for _ in range(n)]
    for target in range(target_weight + 1):
        if wt_arr[0] <= target:
            dp_arr[0][target] = value_arr[0]

    for index in range(1, n):
        for target in range(1, target_weight + 1):
            non_pick = dp_arr[index - 1][target]
            pick = float("-inf")
            if wt_arr[index] <= target:
                pick = value_arr[index] + dp_arr[index - 1][target - wt_arr[index]]
            dp_arr[index][target] = max(pick, non_pick)
    return dp_arr[n - 1][target_weight]


if __name__ == '__main__':
    # print(knapsack_problem([1, 2, 3], [4, 5, 1], 4))
    # print(knapsack_problem_tab([1, 2, 3], [4, 5, 1], 4))
    print(knapsack_problem_tab([10, 8, 6], [1, 7, 9], 7))
