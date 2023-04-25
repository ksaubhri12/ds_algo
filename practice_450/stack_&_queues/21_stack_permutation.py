def check_if_stack_permutation(input_arr: [], output_arr: []):
    if len(input_arr) != len(output_arr):
        return False
    n = len(input_arr)
    i = 0
    j = 0
    data_stack = []
    while i < n:
        input_element = input_arr[i]
        if input_element == output_arr[j]:
            i = i + 1
            j = j + 1
            continue

        if len(data_stack) > 0 and output_arr[j] == data_stack[-1]:
            data_stack.pop(-1)
            j = j + 1
            continue

        data_stack.append(input_element)
        i = i + 1

    if j >= n - 1 and len(data_stack) == 0:
        return True
    while len(data_stack) > 0 and j < n:
        if output_arr[j] == data_stack[-1]:
            j = j + 1
            data_stack.pop()
        else:
            return False

    return True


def main_code(input_arr: [], output_arr: []):
    return 'YES' if check_if_stack_permutation(input_arr, output_arr) else 'NO'


if __name__ == '__main__':
    input_arr = [2, 4, 6]
    print(main_code([2, 29, 11, 8], [11, 29, 2, 8]))

    print(main_code([1, 2, 3], [2, 1, 3]))
    print(main_code([1, 2, 3], [3, 1, 2]))
    print(main_code(input_arr, [6, 2, 4]))
    print(main_code(input_arr, [2, 6, 4]))
    print(main_code(input_arr, [2, 4, 6]))
    print(main_code(input_arr, [4, 2, 6]))
    print(main_code(input_arr, [4, 6, 2]))
    print(main_code(input_arr, [6, 4, 2]))
    print(main_code(input_arr, [2, 3, 4]))
