def sort_stack_using_recursion(input_stack: []):
    if len(input_stack) == 0:
        return

    x = input_stack.pop(-1)
    sort_stack_using_recursion(input_stack)
    add_value_to_stack(input_stack, x)


def add_value_to_stack(input_stack, value: int):
    if len(input_stack) == 0:
        input_stack.append(value)
        return

    if input_stack[-1] <= value:
        input_stack.append(value)
        return

    x = input_stack.pop(-1)
    add_value_to_stack(input_stack, value)
    input_stack.append(x)


def sort_stack_main(input_stack: []):
    sort_stack_using_recursion(input_stack)
    return input_stack


if __name__ == '__main__':
    print(sort_stack_main([11, 2, 32, 3, 41]))
