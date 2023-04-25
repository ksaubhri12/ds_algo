# Lets us solve two important fundamental problems
# Nearest smallest element right
# Nearest smallest element left
# We have solved nearest greatest element right (Next greatest element).

def nearest_smallest_element_left(input_stack: [], n):
    result_stack = []
    output_answer = [-1] * n
    for i in range(0, n):
        element = input_stack[i]

        while len(result_stack) > 0 and element <= result_stack[-1]:
            result_stack.pop(-1)

        if len(result_stack) > 0:
            output_answer[i] = result_stack[-1]
            result_stack.append(element)

        else:
            result_stack.append(element)
    return output_answer


def nearest_smallest_element_right(input_stack: [], n):
    data_stack = []
    output_answer = [-1] * n
    for i in reversed(range(0, n)):
        element = input_stack[i]
        while len(data_stack) > 0 and element <= data_stack[-1]:
            data_stack.pop(-1)

        if len(data_stack) > 0:
            output_answer[i] = data_stack[-1]
            data_stack.append(element)
        else:
            data_stack.append(element)

    return output_answer


def nearest_smallest_in_left_index(input_stack: [], n: int):
    data_stack = []
    output_index_answer = [-1] * n
    for i in range(0, n):
        element = input_stack[i]
        while len(data_stack) > 0 and element <= input_stack[data_stack[-1]]:
            data_stack.pop(-1)

        if len(data_stack) > 0:
            output_index_answer[i] = data_stack[-1]
            data_stack.append(i)

        else:
            data_stack.append(i)

    return output_index_answer


def next_smallest_in_right_index(input_stack: [], n: int):
    data_stack = []
    output_index_answer = [n] * n
    for i in reversed(range(0, n)):
        element = input_stack[i]
        while len(data_stack) > 0 and element <= input_stack[data_stack[-1]]:
            data_stack.pop(-1)

        if len(data_stack) > 0:
            output_index_answer[i] = data_stack[-1]
            data_stack.append(i)

        else:
            data_stack.append(i)

    return output_index_answer


def get_rectangle(input_stack: []):
    n = len(input_stack)
    prev_smallest = nearest_smallest_in_left_index(input_stack, n)
    next_smallest = next_smallest_in_right_index(input_stack, n)
    max_area = float('-inf')
    for i in range(0, n):
        curr_area = input_stack[i] * (next_smallest[i] - prev_smallest[i] - 1)
        max_area = max(max_area, curr_area)

    return max_area


if __name__ == '__main__':
    print(get_rectangle([6, 2, 5, 4, 5, 1, 6]))
    print(get_rectangle([7, 2, 8, 9, 1, 3, 6, 5]))

    print(nearest_smallest_element_right([5, 0], 2))
    print(nearest_smallest_element_right([1, 2, 3, 4], 4))
    print(nearest_smallest_element_right([1, 3, 2], 3))
    print(nearest_smallest_element_right([2, 1, 4, 3], 4))
    print(nearest_smallest_element_left([4, 10, 5, 8, 20, 15, 3, 12], 8))
