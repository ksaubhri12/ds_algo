def next_greater_element(input_arr: [], n):
    output_arr = [-1] * n
    input_stack = []
    for i in reversed(range(0, n)):

        element = input_arr[i]

        while len(input_stack) > 0 and input_stack[-1] < element:
            input_stack.pop(-1)

        if len(input_stack) > 0:

            output_arr[i] = input_stack[-1]
            input_stack.append(element)

        else:
            output_arr[i] = -1
            input_stack.append(element)

    return output_arr


if __name__ == '__main__':
    print(next_greater_element([6, 8, 0, 1, 3], 5))
    print(next_greater_element([1, 3, 2, 4], 4))
