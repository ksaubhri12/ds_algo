def count_subset_rec_util(arr: [], index: int, tar: int) -> int:
    if tar == 0:
        return 1

    if index == 0:
        if arr[index] == tar:
            return 1
        else:
            return 0

    non_pick = count_subset_rec_util(arr, index - 1, tar)
    pick = 0
    if arr[index] <= tar:
        pick = count_subset_rec_util(arr, index - 1, tar - arr[index])
    return pick + non_pick


def count_subset(arr: [], target: int) -> int:
    n = len(arr)
    return count_subset_rec_util(arr, n - 1, target)


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


if __name__ == '__main__':
    print(count_subset([5, 2, 3, 10, 6, 8], 10))
    print(count_subset([2, 5, 1, 4, 3], 10))
    print(count_subset_tab([5, 2, 3, 10, 6, 8], 10))
    print(count_subset_tab([2, 5, 1, 4, 3], 10))
    print(count_subset_tab([28, 4, 3, 27, 0, 24, 26], 24))
    print(count_subset_tab([0, 10, 0], 0))
