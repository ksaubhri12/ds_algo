def is_sum_possible(arr: [], target: int) -> [[]]:
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

    return dp_arr


def min_sum_partition(arr: []) -> int:
    n = len(arr)
    total_sum = sum(arr)
    if total_sum % 2 == 0:
        target_sum = int(total_sum / 2)
    else:
        target_sum = int((total_sum - 1) / 2)

    dp_arr = is_sum_possible(arr, target_sum)

    achievable_target_sum = None
    for target_sum_values in reversed(range(target_sum + 1)):
        if dp_arr[n - 1][target_sum_values]:
            achievable_target_sum = target_sum_values
            break

    other_sum_value = total_sum - achievable_target_sum
    min_sum = abs(other_sum_value - achievable_target_sum)
    return min_sum


if __name__ == '__main__':
    print(min_sum_partition([1, 6, 11, 15]))
    print(min_sum_partition([1, 4]))
    print(min_sum_partition([1]))
