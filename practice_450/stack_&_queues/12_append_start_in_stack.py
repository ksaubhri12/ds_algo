def append_start_stack(input_stack: [], x):
    if len(input_stack) == 0:
        input_stack.append(x)
        return

    popped_element = input_stack.pop(-1)
    append_start_stack(input_stack, x)
    input_stack.append(popped_element)


def add_bottom(input_stack: [], x):
    append_start_stack(input_stack, x)
    return input_stack


if __name__ == '__main__':
    print(add_bottom([5, 4, 3, 2, 1, 10], 9))
