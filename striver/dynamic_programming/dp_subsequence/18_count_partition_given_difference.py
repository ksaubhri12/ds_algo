def count_subset_tab(arr: [], target: int) -> int:
    n = len(arr)
    dp_arr = [[0 for _ in range(target + 1)] for _ in range(n)]

    if arr[0] == 0:
        dp_arr[0][0] = 2
    else:
        dp_arr[0][0] = 1

    if arr[0] != 0 and arr[0] <= target:
        dp_arr[0][arr[0]] = 1

    for index in range(1, n):
        for target_index in range(0, target + 1):
            not_taken = dp_arr[index - 1][target_index]
            taken = 0
            if arr[index] <= target_index:
                taken = dp_arr[index - 1][target_index - arr[index]]

            dp_arr[index][target_index] = not_taken + taken
    return dp_arr[n - 1][target]


def count_partition(arr: [], diff: int) -> int:
    small_sum = (int(sum(arr)) - diff) / 2

    if small_sum % 2 != 0:
        return False

    return count_subset_tab(arr, int(small_sum))
