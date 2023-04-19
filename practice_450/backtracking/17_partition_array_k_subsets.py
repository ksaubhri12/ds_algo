def partition_arr(input_arr: [], index, n, k, result_arr: [], path_arr: []):
    if index >= n:
        for arr in path_arr:
            if len(arr) == 0:
                return
        result_temp_arr = []
        for arr in path_arr:
            result_temp_arr.append(arr.copy())
        result_arr.append(result_temp_arr)
        return

    element = input_arr[index]
    for i in range(k):
        arr = path_arr[i]
        if len(arr) == 0:
            path_arr[i].append(element)
            partition_arr(input_arr, index + 1, n, k, result_arr, path_arr)
            path_arr[i].pop(-1)
            break
        else:
            path_arr[i].append(element)
            partition_arr(input_arr, index + 1, n, k, result_arr, path_arr)
            path_arr[i].pop(-1)


def print_k_sub_set(input_arr: [], k):
    input_arr = sorted(input_arr)
    result_arr = []
    path_arr = []
    for i in range(k):
        path_arr.append([])
    partition_arr(input_arr, 0, len(input_arr), k, result_arr, path_arr)
    return result_arr


def k_subset_possible(input_arr: [], index, n, k, result_arr: [], sum_path_arr: [], required_sum):
    if index > n:
        return
    if index == n:
        for i in range(k):
            element = sum_path_arr[i]
            if element != required_sum:
                return
        result_arr[0] = True
        return

    element = input_arr[index]
    for i in range(k):
        sum_value = sum_path_arr[i]
        if sum_value == 0:
            sum_path_arr[i] = element
            k_subset_possible(input_arr, index + 1, n, k, result_arr, sum_path_arr, required_sum)
            sum_path_arr[i] = sum_path_arr[i] - element
            break
        else:
            sum_path_arr[i] = sum_path_arr[i] + element
            k_subset_possible(input_arr, index + 1, n, k, result_arr, sum_path_arr, required_sum)
            sum_path_arr[i] = sum_path_arr[i] - element


def partition_sum_k_driver(input_arr: [], k):
    n = len(input_arr)
    sum_value = sum(input_arr)
    if k == 1:
        return True

    if k == n:
        for element in input_arr:
            if element != sum_value // k:
                return False
        return True

    required_sum = sum_value // k
    if sum_value % k != 0:
        return
    sum_path_arr = [0] * k
    result_arr = [False]
    k_subset_possible(input_arr, 0, n, k, result_arr, sum_path_arr, required_sum)
    return result_arr[0]


if __name__ == '__main__':
    print(partition_sum_k_driver([3, 2, 4, 11], 2))
