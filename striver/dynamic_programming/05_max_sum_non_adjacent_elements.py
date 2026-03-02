def max_sum_adj_non_element(arr: []):
    n = len(arr)
    return max_sum_adj_non_element_util(arr, n - 1)


def max_sum_adj_non_element_util(arr: [], index):
    if index < 0:
        return 0
    if index == 0:
        return arr[index]

    pick = arr[index] + max_sum_adj_non_element_util(arr, index - 2)
    non_pick = 0 + max_sum_adj_non_element_util(arr, index - 1)
    return max(pick, non_pick)


def max_sum_adj_non_element_mem(arr: []):
    n = len(arr)
    dp_arr = [-1] * n
    dp_arr[0] = arr[0]
    return max_sum_adj_non_element_mem_util(arr, dp_arr, n - 1)


def max_sum_adj_non_element_mem_util(arr: [], dp_arr, index):
    if index < 0:
        return 0

    if index == 0:
        return arr[index]

    if dp_arr[index] != -1:
        return dp_arr[index]

    pick = arr[index] + max_sum_adj_non_element_mem_util(arr, dp_arr, index - 2)
    non_pick = 0 + max_sum_adj_non_element_mem_util(arr, dp_arr, index - 1)

    dp_arr[index] = max(pick, non_pick)
    return dp_arr[index]


def max_sum_adj_non_element_tab(arr: []):
    n = len(arr)
    if n == 1:
        return arr[0]
    dp_arr = [-1] * n
    dp_arr[0] = arr[0]
    dp_arr[1] = max(arr[1], arr[0])
    for i in range(2, n):
        pick = arr[i] + dp_arr[i - 2]
        non_pick = 0 + dp_arr[i - 1]
        dp_arr[i] = max(pick, non_pick)
    return dp_arr[n - 1]


def max_sum_adj_non_element_space_optimized(arr: []):
    n = len(arr)
    if n == 1:
        return arr[0]
    if n == 2:
        return max(arr[0], arr[1])
    prev_prev = arr[0]
    prev = max(arr[0], arr[1])
    for i in range(2, n):
        pick = arr[i] + prev_prev
        non_pick = 0 + prev
        curr = max(pick, non_pick)
        prev = curr
        prev_prev = prev
    return prev


if __name__ == '__main__':
    print(max_sum_adj_non_element([5, 5, 10, 100, 10, 5]))
    print(max_sum_adj_non_element([3, 2, 7, 10]))
    print(max_sum_adj_non_element([9, 1, 6, 10]))
    print(max_sum_adj_non_element_mem([5, 5, 10, 100, 10, 5]))
    print(max_sum_adj_non_element_mem([3, 2, 7, 10]))
    print(max_sum_adj_non_element_mem([9, 1, 6, 10]))
    print(max_sum_adj_non_element_tab([5, 5, 10, 100, 10, 5]))
    print(max_sum_adj_non_element_tab([3, 2, 7, 10]))
    print(max_sum_adj_non_element_tab([9, 1, 6, 10]))
    print(max_sum_adj_non_element_space_optimized([5, 5, 10, 100, 10, 5]))
    print(max_sum_adj_non_element_space_optimized([3, 2, 7, 10]))
    print(max_sum_adj_non_element_space_optimized([9, 1, 6, 10]))
