def reverse_stack_using_recursion(input_stack: []):
    if len(input_stack) == 0:
        return
    x = input_stack.pop(-1)
    reverse_stack_using_recursion(input_stack)
    append_start_stack(input_stack, x)


def reverse_main(input_stack: []):
    reverse_stack_using_recursion(input_stack)
    return input_stack


def append_start_stack(input_stack: [], x):
    if len(input_stack) == 0:
        input_stack.append(x)
        return

    popped_element = input_stack.pop(-1)
    append_start_stack(input_stack, x)
    input_stack.append(popped_element)


if __name__ == '__main__':
    print(reverse_main([5, 4, 3, 2, 1]))
