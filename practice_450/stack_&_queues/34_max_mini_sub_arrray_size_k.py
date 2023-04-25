def next_greater_element_index(input_arr: [], n):
    output_arr = [float('inf')] * n
    data_stack = []
    for i in reversed(range(n)):
        element = input_arr[i]
        while len(data_stack) > 0 and element >= input_arr[data_stack[-1]]:
            data_stack.pop(-1)

        if len(data_stack) > 0:
            output_arr[i] = data_stack[-1]
            data_stack.append(i)
        else:
            data_stack.append(i)

    return output_arr


def next_smallest_element_index(input_arr: [], n):
    output_arr = [float('inf')] * n
    data_stack = []
    for i in reversed(range(n)):
        element = input_arr[i]
        while len(data_stack) > 0 and element <= input_arr[data_stack[-1]]:
            data_stack.pop(-1)

        if len(data_stack) > 0:
            output_arr[i] = data_stack[-1]
            data_stack.append(i)

        else:
            data_stack.append(i)

    return output_arr


def max_sub_array_sum_size_k(input_arr: [], n: int, k: int):
    next_greater_element_index_arr = next_greater_element_index(input_arr, n)
    i = 0
    j = 0
    end = k - 1
    output_arr = []
    while end < n:
        if j < i:
            j = i
        ans = j
        while next_greater_element_index_arr[j] <= end:
            ans = j
            j = next_greater_element_index_arr[j]
        output_arr.append(input_arr[j])

        i = i + 1
        end = end + 1

    return output_arr


def min_sub_array_size_k(input_arr: [], n: int, k: int):
    next_smallest_element_index_arr = next_smallest_element_index(input_arr, n)
    i = 0
    j = 0
    end = k - 1
    output_arr = []
    while end < n:
        if j < i:
            j = i

        while next_smallest_element_index_arr[j] <= end:
            j = next_smallest_element_index_arr[j]

        output_arr.append(input_arr[j])

        i = i + 1
        end = end + 1

    return output_arr


def driver_main_code(input_arr: [], n, k):
    max_sub_arr = max_sub_array_sum_size_k(input_arr, n, k)
    min_sub_arr = min_sub_array_size_k(input_arr, n, k)
    answer = 0
    for i in range(len(max_sub_arr)):
        answer = answer + max_sub_arr[i] + min_sub_arr[i]

    return answer


if __name__ == '__main__':
    print(driver_main_code([2, 5, -1, 7, -3, -1, -2], 7, 4))
    print(driver_main_code([1, 2, 3, 4, 5], 5, 3))
    print(driver_main_code([2, 4, 7, 3, 8, 1], 6, 4))
