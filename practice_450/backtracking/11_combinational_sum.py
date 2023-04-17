def combination_sum_helper(input_arr: [], target: int, index: int, curr_sum: int, temp_path: [], result_arr: [[]],
                           input_map: {}):
    if curr_sum > target:
        return

    if index == len(input_arr):
        if curr_sum == target:
            str_result = str(temp_path.copy())
            if str_result not in input_map:
                input_map[str_result] = 1
                result_arr.append(temp_path.copy())
        return

    curr_sum = curr_sum + input_arr[index]
    temp_path.append(input_arr[index])
    combination_sum_helper(input_arr, target, index, curr_sum, temp_path, result_arr, input_map)
    curr_sum = curr_sum - input_arr[index]
    temp_path.pop(-1)

    combination_sum_helper(input_arr, target, index + 1, curr_sum, temp_path, result_arr, input_map)


def combination_sum(input_arr: [], target: int):
    input_arr = sorted(input_arr)
    result_arr = []
    path_arr = []
    combination_sum_helper(input_arr, target, 0, 0, path_arr, result_arr, {})
    return result_arr


if __name__ == '__main__':
    print(combination_sum([8, 1, 8, 6, 8], 12))
    print(combination_sum([7, 2, 6, 5], 16))
