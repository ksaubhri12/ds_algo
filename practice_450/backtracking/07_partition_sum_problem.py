def partition_sum_problem(input_arr: []):
    sum_value = sum(input_arr)
    if sum_value % 2 != 0:
        return False

    return can_partition_helper(0, int(sum_value // 2), len(input_arr) - 1, input_arr)


def can_partition_helper(index: int, remaining_sum: int, end_index, input_arr: []):
    if remaining_sum == 0:
        return True

    if index > end_index or remaining_sum < 0:
        return False

    return can_partition_helper(index + 1, remaining_sum - input_arr[index], end_index,
                                input_arr) or can_partition_helper(
        index + 1, remaining_sum, end_index, input_arr)


if __name__ == '__main__':
    print(partition_sum_problem([1, 5, 5, 11]))
